"""Wrapper class."""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from arlbench.core.environments import Environment


class Wrapper:
    """Base class for ARLBench wrappers."""

    def __init__(self, env: Environment):
        """Wraps an ARLBench Environment.

        Args:
            env (Environment): Environment to wrap
        """
        self._env = env

    # provide proxy access to regular attributes of wrapped object
    def __getattr__(self, name):
        return getattr(self._env, name)
