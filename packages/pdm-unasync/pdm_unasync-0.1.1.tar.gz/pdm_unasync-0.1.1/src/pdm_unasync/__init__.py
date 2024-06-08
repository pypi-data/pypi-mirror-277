import argparse
import dataclasses
import pathlib
from typing import Any, Self, cast

import unasync  # type: ignore
from pdm.cli.commands.base import BaseCommand  # type: ignore
from pdm.core import Core
from pdm.project import Project  # type: ignore
from pdm.project.toml_file import TOMLBase  # type: ignore
from pdm.signals import pre_build

DEFAULT_REPLACEMENTS = {
    "AsyncClient": "Client",
    "aclose": "close",
    "async_return_one_or_raise": "return_one_or_raise",
    "atimeout": "timeout",
    "asleep": "sleep",
    "AsyncApi": "Api",
    "TaskGroup": "SyncTaskGroup",
    "detect_scopes": "sync_detect_scopes",
    "_async": "_sync",
    "load_asyncclient": "load_client",
    "as_async": "as_sync",
}


@dataclasses.dataclass
class PathSetting:
    path: str
    src: str
    dst: str

    @classmethod
    def from_dct(cls, dct: dict[str, Any]) -> Self:
        return cls(dct["path"], dct["src"], dct["dst"])


@dataclasses.dataclass
class Settings:
    replacements: dict[str, str] = dataclasses.field(default_factory=dict)
    paths: list[PathSetting] = dataclasses.field(default_factory=list)

    @classmethod
    def from_dct(cls, dct: dict[str, Any]) -> Self:
        paths = [PathSetting.from_dct(path) for path in dct.get("paths", [])]
        replacements = cast(dict[str, str], dct.get("replacements", DEFAULT_REPLACEMENTS))
        return cls(replacements, paths)

    @classmethod
    def from_project(cls, project: Project) -> Self:
        base = TOMLBase(project.root / project.PYPROJECT_FILENAME, ui=project.core.ui).read()
        dct = cast(dict[str, Any], base.get("tool", {}).get("unasync", {}))  # type: ignore
        return cls.from_dct(dct)


def run(project: Project):
    settings = Settings.from_project(project)
    add_repla = settings.replacements

    for path in settings.paths:
        rules = (unasync.Rule(fromdir=path.src, todir=path.dst, additional_replacements=add_repla),)
        files = [str(p) for p in pathlib.Path(path.path).iterdir() if p.is_file()]
        unasync.unasync_files(files, rules)  # type: ignore


@pre_build.connect
def on_pre_build(project: Project, dest: str, config_settings: dict[str, str] | None, hooks: Any):
    run(project)


class UnasyncCommand(BaseCommand):
    """Configure via pyproject.toml:

    [tool.unasync]
    paths = [
        {path = "examples/async", src = "/async/", dst = "/sync/"},
        {path = "src/dnac/dnac_sdk/_async", src = "/_async/", dst = "/_sync/"},
    ]
    [tool.unasync.replacements]
    AsyncClient= "Client"
    aclose= "close"
    async_return_one_or_raise= "return_one_or_raise"
    atimeout= "timeout"
    asleep= "sleep"
    AsyncApi= "Api"
    TaskGroup= "SyncTaskGroup"
    detect_scopes= "sync_detect_scopes"
    _async= "_sync"
    load_asyncclient= "load_client"
    as_async= "as_sync"
    """

    def handle(self, project: Project, options: argparse.Namespace):
        run(project)


def unasync_plugin(core: Core):
    core.register_command(UnasyncCommand, "unasync")
