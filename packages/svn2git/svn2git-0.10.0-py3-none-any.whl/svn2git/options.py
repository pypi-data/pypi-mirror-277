from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SVN2GitOptions:
    """Static for keeping track of the options passed to svn2git"""

    svn_url: str
    """SVN repository URL"""
    revision: Optional[str] = None
    """Start importing from SVN revision START_REV; optionally end at END_REV. Format: START_REV:[END_REV]"""
    authors: Optional[str] = None
    """Path to file containing svn-to-git authors mapping"""
    rebase: bool = False
    """Instead of cloning a new project, rebase an existing one against SVN"""
    rebase_branch: Optional[str] = None
    """Rebase only specified branch"""
    automatic: bool = False
    """Enable automatic switching between clone and rebase commands"""
    username: Optional[str] = None
    """Username for transports that needs it (http(s), svn)"""
    password: Optional[str] = None
    """Password for transports that needs it (http(s), svn)"""
    allow_store_plaintext_password: bool = False
    """Allow passwords to be stored in plaintext"""
    realm: Optional[str] = None
    """SVN server authentication realm"""
    root_is_trunk: bool = False
    """Use this if the root level of the repo is equivalent to the trunk and there are no tags or branches"""
    trunk: str = "trunk"
    """Subpath to trunk from repository URL (default: trunk)"""
    no_trunk: bool = False
    """Do not import anything from trunk"""
    branches: list[str] = field(default_factory=lambda: ["branches"])
    """Subpath to branches from repository URL (default: ["branches"])"""
    no_branches: bool = False
    """Do not try to import any branches"""
    tags: list[str] = field(default_factory=lambda: ["tags"])
    """Subpath to tags from repository URL (default: ["tags"])"""
    no_tags: bool = False
    """Do not try to import any tags"""
    no_minimize_url: bool = False
    """Accept URLs as-is without attempting to connect to a higher level directory"""
    include_metadata: bool = False
    """Include metadata in git logs (git-svn-id)"""
    exclude: list[str] = field(default_factory=list)
    """Specify a Perl regular expression to filter paths when fetching"""
    verbose: bool = False
    """Be verbose in logging -- useful for debugging issues"""
    cwd: Optional[str] = None
    """The current working directory to run the command in."""
    push: bool = False
    """Push the repository to the git remote after the conversion is complete."""
    git_remote: str = "origin"
    """The name of the git remote to push to."""
    git_remote_url: Optional[str] = None
    """The URL of the git remote to push to. If not specified, no git remote will be added."""
    large_repository_mode: bool = False
    """Enable large repository mode. This will split the git push command into
    separate pushes of <push_commit_limit> commits each."""
    push_commit_limit: int = 1000
    """The number of commits to push per push command when large repository mode is enabled."""
