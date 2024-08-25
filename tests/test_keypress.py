import pytest

from keypress.key import Key, Keys, get_description


def test_key_initialization():
    """Test initialization of the Key class."""
    key = Key(key="a", key_codes=(97,), is_printable=True, description="a")
    assert key.key == "a"
    assert key.key_codes == (97,)
    assert key.is_printable is True
    assert key.description == "a"


def test_key_equality():
    """Test equality of Key instances."""
    key1 = Key(key="a", key_codes=(97,), is_printable=True, description="a")
    key2 = Key(key="a", key_codes=(97,), is_printable=True, description="a")
    key3 = Key(key="b", key_codes=(98,), is_printable=True, description="b")

    assert key1 == key2
    assert key1 != key3
    assert key2 != key3


def test_keys_class():
    """Test the Keys class constants."""
    assert Keys.CTRL_LETTERS["a"] == 1
    assert Keys.ALPHABETS["A"] == 65
    assert Keys.NUMBERS["0"] == 48
    assert Keys.FUNCTION_KEYS["F1"] == 112
    assert Keys.SPECIAL_CHARACTERS[33] == "!"
    assert Keys.UP_ARROW == (27, 91, 65)  # Example for Linux/Mac
    assert Keys.BACKSPACE == (127,)  # Example for Linux/Mac


def test_get_description_printable():
    """Test description for a printable character."""
    description = get_description((65,), True)  # A
    assert description == "A"


def test_get_description_non_printable():
    """Test description for a non-printable character."""
    description = get_description((13,), False)  # Ctrl + M
    assert description == "Ctrl + M"


def test_get_description_special():
    """Test description for a special character."""
    description = get_description((33,), False)  # !
    assert description == "Special ((33,))"


def test_get_description_ctrl():
    """Test description for Ctrl + Letter."""
    description = get_description((1,), False)  # Ctrl + A
    assert description == "Ctrl + A"


if __name__ == "__main__":
    pytest.main()
