from datalad_core.config import ConfigItem as ConfigItem, UnsetValue as UnsetValue, get_manager as get_manager
from datalad_core.repo import Repo as Repo, Worktree as Worktree
from datalad_core.tests.fixtures import magic_marker as magic_marker

def test_manager_setup() -> None: ...
def test_manager_overrides() -> None: ...
def test_manager_fordataset(gitrepo) -> None: ...
def test_manager_forbaredataset(baregitrepo) -> None: ...
def test_manager_protected_query(gitrepo) -> None: ...
