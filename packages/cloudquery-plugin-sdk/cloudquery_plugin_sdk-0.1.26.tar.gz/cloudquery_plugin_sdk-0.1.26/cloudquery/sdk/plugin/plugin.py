from dataclasses import dataclass
from typing import List, Generator

from cloudquery.sdk import message
from cloudquery.sdk.schema import Table

MIGRATE_MODE_STRINGS = ["safe", "force"]


@dataclass
class TableOptions:
    tables: List[str] = None
    skip_tables: List[str] = None
    skip_dependent_tables: bool = False


@dataclass
class BackendOptions:
    connection: str = None
    table_name: str = None


@dataclass
class SyncOptions:
    deterministic_cq_id: bool = False
    skip_dependent_tables: bool = False
    skip_tables: List[str] = None
    tables: List[str] = None
    backend_options: BackendOptions = None


@dataclass
class BuildTarget:
    os: str = None
    arch: str = None


@dataclass
class Options:
    dockerfile: str = None
    build_targets: List[BuildTarget] = None
    team: str = None
    kind: str = None
    json_schema: str = None


class Plugin:
    def __init__(self, name: str, version: str, opts: Options = None) -> None:
        self._name = name
        self._version = version
        self._opts = Options() if opts is None else opts
        if self._opts.dockerfile is None:
            self._opts.dockerfile = "Dockerfile"
        if self._opts.build_targets is None:
            self._opts.build_targets = [
                BuildTarget("linux", "amd64"),
                BuildTarget("linux", "arm64"),
            ]

    def init(self, spec: bytes, no_connection: bool = False) -> None:
        pass

    def set_logger(self, logger) -> None:
        pass

    def name(self) -> str:
        return self._name

    def version(self) -> str:
        return self._version

    def team(self) -> str:
        return self._opts.team

    def kind(self) -> str:
        return self._opts.kind

    def json_schema(self) -> str:
        return self._opts.json_schema

    def dockerfile(self) -> str:
        return self._opts.dockerfile

    def build_targets(self) -> List[BuildTarget]:
        return self._opts.build_targets

    def get_tables(self, options: TableOptions) -> List[Table]:
        raise NotImplementedError()

    def sync(self, options: SyncOptions) -> Generator[message.SyncMessage, None, None]:
        raise NotImplementedError()

    def write(self, writer: Generator[message.WriteMessage, None, None]) -> None:
        raise NotImplementedError()

    def close(self) -> None:
        raise NotImplementedError()
