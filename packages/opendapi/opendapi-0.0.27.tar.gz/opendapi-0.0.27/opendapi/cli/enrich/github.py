"""Enricher to work from Github as part of `opendapi enrich` CLI command."""

from typing import Optional

import click

from opendapi.adapters.git import add_untracked_opendapi_files, run_git_command
from opendapi.adapters.github import GithubAdapter
from opendapi.cli.enrich.local import Enricher
from opendapi.logging import LogCounterKey, increment_counter


class GithubEnricher(Enricher):
    """Enricher to work from Github as part of `opendapi enrich` CLI command."""

    def setup_objects(self):
        """Initialize the adapter."""
        self.github_adapter: GithubAdapter = GithubAdapter(
            self.trigger_event.repo_api_url,
            self.trigger_event.auth_token,
            exception_cls=click.ClickException,
        )
        super().setup_objects()

    def should_enrich(self) -> bool:
        """Should we enrich the DAPI files?"""
        return (
            self.dapi_server_config.suggest_changes
            and self.trigger_event.is_pull_request_event
        )

    def should_register(self) -> bool:
        """Should we register the DAPI files?"""
        if (
            self.dapi_server_config.register_on_merge_to_mainline
            and self.trigger_event.is_push_event
            and self.trigger_event.git_ref
            == f"refs/heads/{self.dapi_server_config.mainline_branch_name}"
        ):
            return True

        self.print_markdown_and_text(
            "Registration skipped because the conditions weren't met",
            color="yellow",
        )
        return False

    def should_analyze_impact(self) -> bool:
        return self.trigger_event.is_pull_request_event

    def print_dapi_server_progress(self, progressbar, progress: int):
        """Print the progress bar for validation."""
        progressbar.update(progress)
        self.print_text_message(
            f"\nFinished {round(progressbar.pct * 100)}% with {progressbar.format_eta()} remaining",
            color="green",
            bold=True,
        )

    def get_current_branch_name(self):
        """Get the current branch name."""
        return (
            run_git_command(self.root_dir, ["git", "rev-parse", "--abbrev-ref", "HEAD"])
            .decode("utf-8")
            .strip()
        )

    def get_autoupdate_branch_name(self):
        """Get the autoupdate branch name."""
        return f"opendapi-autoupdate-for-{self.trigger_event.pull_request_number}"

    def get_base_for_changed_files(self):
        """
        Get the base branch for the changed files.

        On Github and PRs, first check if an earlier autoupdate PR was merged,
        and use that as the base commit
        if not, use the base branch of the current PR.
        """
        if self.trigger_event.is_pull_request_event:
            merged_prs = self.github_adapter.get_merged_pull_requests(
                self.trigger_event.repo_owner,
                self.get_current_branch_name(),
                self.get_autoupdate_branch_name(),
            )
            if merged_prs:
                merge_commit = merged_prs[0]["merge_commit_sha"]
                # check if the merge commit is in the current PR
                try:
                    git_merge_commit = run_git_command(
                        self.root_dir,
                        [
                            "git",
                            "merge-base",
                            merge_commit,
                            self.trigger_event.after_change_sha,
                        ],
                    )
                    if git_merge_commit.decode("utf-8").strip() == merge_commit:
                        return merge_commit
                except RuntimeError:
                    # if the merge commit is not in the current PR, use the base branch
                    pass
        return super().get_base_for_changed_files()

    def create_pull_request_for_changes(self) -> Optional[int]:
        """
        Create a pull request for any changes made to the DAPI files.
        """
        # Check status for any uncommitted changes
        git_status = run_git_command(self.root_dir, ["git", "status", "--porcelain"])
        if not git_status:
            return None

        self.print_markdown_and_text(
            "Creating a pull request for the changes...",
            color="green",
        )

        # Set git user and email
        git_config_map = {
            "user.email": self.validate_response.server_meta.github_user_email,
            "user.name": self.validate_response.server_meta.github_user_name,
        }
        for config, value in git_config_map.items():
            run_git_command(self.root_dir, ["git", "config", "--global", config, value])

        # get current branch name
        current_branch_name = self.get_current_branch_name()

        # Unique name for the new branch
        update_branch_name = self.get_autoupdate_branch_name()

        # Checkout new branch. Force reset if branch already exists,
        # including uncommited changes
        run_git_command(self.root_dir, ["git", "checkout", "-B", update_branch_name])

        # Add the relevant files
        added_opendapi_files = add_untracked_opendapi_files(self.root_dir)
        autoupdate_pr_number = None

        if added_opendapi_files:
            # Commit the changes
            run_git_command(
                self.root_dir,
                [
                    "git",
                    "commit",
                    "-m",
                    f"OpenDAPI updates for {self.trigger_event.pull_request_number}",
                ],
            )

            # Push the changes. Force push to overwrite any existing branch
            run_git_command(
                self.root_dir,
                [
                    "git",
                    "push",
                    "-f",
                    "origin",
                    f"HEAD:refs/heads/{update_branch_name}",
                ],
            )

            # construct the PR body

            # NOTE: current iteration no longer includes Title markdown
            # please reference commits before 2024-06-05 for the previous implementation

            # IMPORTANT section
            body = (
                "> [!IMPORTANT]\n"
                "> **This PR was auto-generated to sync your metadata with "
                f"schema changes in PR #{self.trigger_event.pull_request_number}.** Please review, "
                "revise[^HowToEditDAPI], and merge this PR to your branch.\n"
                ">\n"
                "> Code-synced metadata instills trust[^WhyMetadataMatters] in "
                "data discovery, quality, and compliance. If you have "
                "questions, reach out to Data Engineering.[^Feedback]\n\n"
            )

            # Footer
            body += (
                "[^WhyMetadataMatters]: Learn more about why code-synced metadata matters "
                "[here](https://www.wovencollab.com/docs)\n"
                "[^HowToEditDAPI]: Watch "
                "[a quick video](https://www.wovencollab.com/howto/edit-metadata-in-github) "
                "to see how to revise metadata suggestions\n"
                "[^Feedback]: Did you find this useful? If you found a bug or have an idea to "
                "improve the DevX, [let us know](https://www.wovencollab.com/feedback)"
            )

            autoupdate_pr_number = self.github_adapter.create_pull_request_if_not_exists(
                self.trigger_event.repo_owner,
                title=(
                    f"Metadata updates for #{self.trigger_event.pull_request_number}"
                ),
                body=body,
                base=current_branch_name,
                head=update_branch_name,
            )

        # ALWAYS Reset by checking out the original branch
        run_git_command(self.root_dir, ["git", "checkout", current_branch_name])
        return autoupdate_pr_number

    def create_summary_comment_on_pull_request(
        self,
        autoupdate_pull_request_number: Optional[int] = None,
    ):
        """Create a summary comment on the pull request."""

        # NOTE: current iteration no longer includes Title markdown
        # please reference commits before 2024-06-05 for the previous implementation

        # WARNING section
        pr_comment_md = (
            "> [!WARNING]\n"
            "> This PR updates a data schema. You are responsible for keeping schema metadata "
            "in-sync with source code and keeping stakeholders informed.\n\n"
        )

        # metadata suggestions - PR unmerged or not updated
        if autoupdate_pull_request_number:
            # Update schema section
            pr_comment_md += (
                "# Update your schema metadata\n\n"
                f"This PR contains a schema change. PR #{autoupdate_pull_request_number} "
                "was auto-generated to keep your metadata in-sync with these changes. "
                "Please review, revise, and merge this metadata update into this branch.\n\n"
            )

            # Review suggestion button
            pr_comment_md += (
                f'<a href="{self.trigger_event.repo_html_url}/'
                f'pull/{autoupdate_pull_request_number}">'
                f'<img src="{self.validate_response.server_meta.suggestions_cta_url}" '
                'width="140"/></a>'
                "\n\n"
            )

        # No metadata suggestions - the metadata PR is merged/updated
        else:
            pr_comment_md += "# Schema metadata synced! :tada:\n\n"
            merged_prs = self.github_adapter.get_merged_pull_requests(
                self.trigger_event.repo_owner,
                self.get_current_branch_name(),
                self.get_autoupdate_branch_name(),
            )

            # if we are in the else clause, there should be a merged PR, but just in case
            pr_stanza = (
                f"PR #{merged_prs[0]['number']}"
                if merged_prs
                else "A Woven-generated PR"
            )

            pr_comment_md += (
                f"This PR contains a schema change. {pr_stanza} was merged into this branch "
                "to keep your metadata in-sync with these changes.\n\n"
            )

        # NOTE: current iteration no longer includes Validation Response markdown
        # please reference commits before 2024-06-05 for the previous implementation

        # No registration response for Pull requests

        # Impact Response
        if self.analyze_impact_response.markdown:
            pr_comment_md += self.analyze_impact_response.markdown
            pr_comment_md += "\n\n<hr>\n\n"

        # Footer
        pr_comment_md += (
            "<sup>Did you find this useful? If you found a bug or have an idea to improve the "
            "DevX, [let us know](https://www.wovencollab.com/feedback)</sup>"
        )

        self.github_adapter.add_pull_request_comment(
            self.trigger_event.pull_request_number, pr_comment_md
        )

    def should_run(self) -> bool:
        """Check if we should run the action."""
        # if there were any merges, we want to communicate this even if there
        # were not more DAPI changes
        if super().should_run():
            return True

        merged_prs = self.github_adapter.get_merged_pull_requests(
            self.trigger_event.repo_owner,
            self.get_current_branch_name(),
            self.get_autoupdate_branch_name(),
        )
        if merged_prs:
            # Check if the merge commit was the most recent one. We want to update then.
            # After that, if there are no more updates to DAPI related stuff, we need
            # create new comments
            # NOTE: This matters much less when we edit/update a comment. This is in place
            # to ensure that we do not spam folks in the interim
            merge_commit = merged_prs[0]["merge_commit_sha"]
            return merge_commit == self.trigger_event.after_change_sha

        return False

    def post_run_actions(self):
        """
        In PRs, spin up another Auto-generated Github PR with new changes
        and leave a comment with that PR number and details on downstream impact
        """
        if not self.validate_response:
            # doesn't look like there were any activity here
            return

        if self.trigger_event.is_pull_request_event:
            metrics_tags = {"org_name": self.config.org_name_snakecase}
            increment_counter(LogCounterKey.SUGGESTIONS_PR_CREATED, tags=metrics_tags)
            suggestions_count = len(self.validate_response.suggestions)
            increment_counter(
                LogCounterKey.SUGGESTIONS_FILE_COUNT,
                value=suggestions_count,
                tags=metrics_tags,
            )
            autoupdate_pr_number = self.create_pull_request_for_changes()
            self.create_summary_comment_on_pull_request(autoupdate_pr_number)

    def run(self):
        if self.trigger_event.event_type == "pull_request":
            metrics_tags = {"org_name": self.config.org_name_snakecase}
            increment_counter(LogCounterKey.USER_PR_CREATED, tags=metrics_tags)
        super().run()
