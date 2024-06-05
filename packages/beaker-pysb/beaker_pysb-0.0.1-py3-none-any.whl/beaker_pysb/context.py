
from beaker_bunsen.bunsen_context import BunsenContext

from .agent import PySbAgent


class PySbContext(BunsenContext):

    agent_cls = PySbAgent
    enabled_subkernels = ["python3"]

    @classmethod
    def default_payload(cls) -> str:
        return "{}"
