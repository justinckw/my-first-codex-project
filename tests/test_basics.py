"""Tests for the introductory variables exercise."""

import importlib
import types

import pytest

MODULE_PATH = "exercises.basics.variables"


def load_module() -> types.ModuleType:
    """Import the user's variables exercise fresh for each test."""
    return importlib.reload(importlib.import_module(MODULE_PATH))


def test_my_name_is_a_non_empty_string():
    mod = load_module()
    assert isinstance(mod.my_name, str)
    assert mod.my_name.strip(), "my_name should not be empty"


def test_my_age_is_an_integer():
    mod = load_module()
    assert isinstance(mod.my_age, int)
    assert mod.my_age >= 0, "my_age should be zero or positive"


def test_favorite_numbers_has_at_least_three_entries():
    mod = load_module()
    assert isinstance(mod.favorite_numbers, list)
    assert len(mod.favorite_numbers) >= 3
    assert all(isinstance(num, int) for num in mod.favorite_numbers)


def test_describe_person_returns_sentence():
    mod = load_module()
    sentence = mod.describe_person("Alex", 30)
    assert "Alex" in sentence
    assert "30" in sentence


def test_add_favorite_number_appends():
    mod = load_module()
    numbers = [1, 2, 3]
    updated = mod.add_favorite_number(numbers, 4)
    assert updated[-1] == 4
    assert updated is numbers, "The function should modify the list in place and return it"


def test_add_favorite_number_rejects_non_int():
    mod = load_module()
    with pytest.raises(TypeError):
        mod.add_favorite_number([1, 2], "not a number")
