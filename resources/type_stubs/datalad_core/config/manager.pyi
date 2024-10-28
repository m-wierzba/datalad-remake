from collections.abc import Generator, Hashable
from datalad_core.config.defaults import ImplementationDefaults as ImplementationDefaults, get_defaults as get_defaults
from datalad_core.config.git import GlobalGitConfig as GlobalGitConfig, SystemGitConfig as SystemGitConfig
from datalad_core.config.gitenv import GitEnvironment as GitEnvironment
from datalad_core.config.item import ConfigItem as ConfigItem
from datasalad.settings import Setting as Setting, Settings, Source as Source
from typing import Any

class ConfigManager(Settings):
    def __init__(self, defaults: ImplementationDefaults, sources: dict[str, Source] | None = None) -> None: ...
    def overrides(self, overrides: dict[Hashable, Setting | tuple[Setting, ...]]) -> Generator[ConfigManager]: ...
    def get(self, key: Hashable, default: Any = None) -> Setting: ...
    def get_from_protected_sources(self, key: Hashable, default: Any = None) -> Setting: ...
    def declare_source_protected(self, key: str): ...

def get_manager() -> ConfigManager: ...
