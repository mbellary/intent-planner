"""
Smoke tests for the XS-00 intent_planner import surface.
"""

from __future__ import annotations

import importlib


def test_intent_planner_root_imports() -> None:
    module = importlib.import_module("intent_planner")
    assert hasattr(module, "__version__")
    assert isinstance(module.__version__, str)
    assert module.__version__


def test_intent_planner_sdk_import() -> None:
    module = importlib.import_module("intent_planner.integrations.sdk")
    assert module is not None


def test_intent_planner_application_import() -> None:
    module = importlib.import_module("intent_planner.application")
    assert module is not None