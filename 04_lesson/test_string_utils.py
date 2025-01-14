import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize("input_str, expected", [
    ("goal", "Goal"),
    ("Goal", "Goal"),
    ("", ""),
    ("1goal", "1goal"),
])
def test_capitilize(input_str, expected):
    assert string_utils.capitilize(input_str) == expected


@pytest.mark.parametrize("input_str", [
    None
])
def test_capitilize_none(input_str):
    with pytest.raises(AttributeError):
        string_utils.capitilize(input_str)


@pytest.mark.parametrize("input_str, expected", [
    ("   goal", "goal"),
    ("     123", "123"),
    ("   ", ""),
    ("  \tsample", "\tsample"),  # Пример с табуляцией.
    (" 11 января 2025", "11 января 2025"),
])
def test_trim(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, delimiter, expected", [
    ("Goal,Pass,Foul,Corner", ",", ["Goal", "Pass", "Foul", "Corner"]),
    ("1:2:3", ":", ["1", "2", "3"]),
    ("", ",", []),
    ("a b c", " ", ["a", "b", "c"]),
])
def test_to_list(input_str, delimiter, expected):
    assert string_utils.to_list(input_str, delimiter) == expected


@pytest.mark.parametrize("input_str", [
    None
])
def test_to_list_none(input_str):
    with pytest.raises(AttributeError):
        string_utils.to_list(input_str)


@pytest.mark.parametrize("input_str, sub_str, expected", [
    ("Goal", "G", True),
    ("Goal", "f", False),
    ("", "a", False),
    ("123", "2", True),
])
def test_contains(input_str, sub_str, expected):
    assert string_utils.contains(input_str, sub_str) == expected


@pytest.mark.parametrize("input_str", [
    None
])
def test_contains_none(input_str):
    with pytest.raises(AttributeError):
        string_utils.contains(input_str, "a")


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Goal", "o", "Gal"),
    ("Goal", "al", "Go"),
    ("Goal", "d", "Goal"),
    ("Goal", "", "Goal"),
    ("", "a", ""),
    ("11 января 2025", "11", " января 2025"),
])
def test_delete_symbol(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, prefix, expected", [
    ("Goal", "G", True),
    ("Goal", "P", False),
    ("", "S", False),
    ("123Test", "123", True),
])
def test_starts_with(input_str, prefix, expected):
    assert string_utils.starts_with(input_str, prefix) == expected


@pytest.mark.parametrize("input_str, suffix, expected", [
    ("Goal", "l", True),
    ("Goal", "h", False),
    ("", "o", False),
    ("Test123", "123", True),
])
def test_end_with(input_str, suffix, expected):
    assert string_utils.end_with(input_str, suffix) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("", True),
    (" ", True),
    ("Goal", False),
])
def test_is_empty(input_str, expected):
    assert string_utils.is_empty(input_str) == expected


@pytest.mark.parametrize("input_list, delimiter, expected", [
    ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
    (["Goal", "Ole"], ", ", "Goal, Ole"),
    (["Goal", "Goal", "Goal"], "-", "Goal-Goal-Goal"),
    ([], ", ", ""),
    ([100, "Тест", "11 января 2025"], ", ", "100, Тест, 11 января 2025"),
])
def test_list_to_string(input_list, delimiter, expected):
    assert string_utils.list_to_string(input_list, delimiter) == expected


@pytest.mark.parametrize("input_list", [
    None
])
def test_list_to_string_none(input_list):
    with pytest.raises(TypeError):
        string_utils.list_to_string(input_list)
