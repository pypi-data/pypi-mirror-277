from functools import lru_cache
from pathlib import Path

from griff.settings.griff_settings import GriffSettings
from pydantic import Field


@lru_cache
def get_root_dir():
    return str(Path(__file__).resolve().parent.parent)


class PytestSettings(GriffSettings):
    project_dir: str = Field(default_factory=get_root_dir)
