import platform
import sys
from typing import Tuple, Union


class Key:
    """Represents a keypress event with associated attributes."""

    def __init__(self, key: str, key_codes: Tuple[int, ...], is_printable: bool, description: str) -> None:
        """
        Initialize a Key object.

        Args:
            key (str): The string representation of the key.
            key_codes (Tuple[int, ...]): The tuple of integer key codes associated with the key.
            is_printable (bool): Whether the key is a printable character.
            description (str): A human-readable description of the key.
        """
        self.key = key
        self.key_codes = key_codes
        self.is_printable = is_printable
        self.description = description

    def __str__(self) -> str:
        return self.key

    def __repr__(self) -> str:
        return f"Key(key='{self.key}', description='{self.description}')"

    def __eq__(self, other: Union[Tuple[int, ...], str]) -> bool:
        """
        Compare the Key object with another Key, string, or tuple of key codes.

        Args:
            other (Union[Tuple[int, ...], str]): The other object to compare against.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if isinstance(other, str):
            return self.key == other
        if isinstance(other, tuple) and all(isinstance(item, int) for item in other):
            return self.key_codes == other
        if isinstance(other, Key):
            return (
                self.key == other.key and self.key_codes == other.key_codes and self.is_printable == other.is_printable
            )
        raise ValueError(f"Cannot compare with {other}. Expected `Tuple[int, ...]` or `str`.")

    def __ne__(self, other: Union[Tuple[int, ...], str]) -> bool:
        return not self.__eq__(other)


class _PlatformIndependentKeys:
    """Platform-independent key codes for common keys."""

    CTRL_LETTERS = {chr(i + 96): i for i in range(1, 27)}  # Ctrl + A-Z
    ENTER = (13,)
    ESC = (27,)
    TAB = (9,)
    SPACEBAR = (32,)

    # Alphabets
    ALPHABETS = {chr(i): i for i in range(65, 91)}  # A-Z
    ALPHABETS.update({chr(i): i for i in range(97, 123)})  # a-z

    # Numbers
    NUMBERS = {str(i): i + 48 for i in range(0, 10)}  # 0-9

    # Function keys
    FUNCTION_KEYS = {f"F{i}": 111 + i for i in range(1, 13)}  # F1-F12

    # Special characters
    SPECIAL_CHARACTERS = {
        33: "!",
        34: '"',
        35: "#",
        36: "$",
        37: "%",
        38: "&",
        39: "'",
        40: "(",
        41: ")",
        42: "*",
        43: "+",
        44: ",",
        45: "-",
        46: ".",
        47: "/",
        58: ":",
        59: ";",
        60: "<",
        61: "=",
        62: ">",
        63: "?",
        64: "@",
        91: "[",
        92: "\\",
        93: "]",
        94: "^",
        95: "_",
        96: "`",
        123: "{",
        124: "|",
        125: "}",
        126: "~",
    }

    BACKSPACE: Union[Tuple[int, ...], None] = None
    DELETE: Union[Tuple[int, ...], None] = None
    HOME: Union[Tuple[int, ...], None] = None
    END: Union[Tuple[int, ...], None] = None
    UP_ARROW: Union[Tuple[int, ...], None] = None
    DOWN_ARROW: Union[Tuple[int, ...], None] = None
    RIGHT_ARROW: Union[Tuple[int, ...], None] = None
    LEFT_ARROW: Union[Tuple[int, ...], None] = None
    NUMPAD_UP_ARROW: Union[Tuple[int, ...], None] = None
    NUMPAD_DOWN_ARROW: Union[Tuple[int, ...], None] = None
    NUMPAD_RIGHT_ARROW: Union[Tuple[int, ...], None] = None
    NUMPAD_LEFT_ARROW: Union[Tuple[int, ...], None] = None
    CTRL_ENTER: Union[Tuple[int, ...], None] = None
    OPTION_ENTER: Union[Tuple[int, ...], None] = None


class Keys(_PlatformIndependentKeys):
    """Platform-specific key codes with common mappings from _PlatformIndependentKeys."""

    if platform.system() in ("Linux", "Darwin", "FreeBSD"):
        BACKSPACE = (127,)
        DELETE = (27, 91, 51, 126)
        HOME = (27, 91, 72)
        END = (27, 91, 70)
        UP_ARROW = (27, 91, 65)
        DOWN_ARROW = (27, 91, 66)
        RIGHT_ARROW = (27, 91, 67)
        LEFT_ARROW = (27, 91, 68)
        NUMPAD_UP_ARROW = (27, 91, 65)
        NUMPAD_DOWN_ARROW = (27, 91, 66)
        NUMPAD_RIGHT_ARROW = (27, 91, 67)
        NUMPAD_LEFT_ARROW = (27, 91, 68)
        CTRL_ENTER = (27, 13)
        OPTION_ENTER = CTRL_ENTER

    elif platform.system() in ("Windows", "CYGWIN"):
        BACKSPACE = (8,)
        DELETE = (224, 83)
        HOME = (224, 71)
        END = (224, 79)
        UP_ARROW = (224, 72)
        DOWN_ARROW = (224, 80)
        RIGHT_ARROW = (224, 77)
        LEFT_ARROW = (224, 75)
        NUMPAD_UP_ARROW = (0, 72)
        NUMPAD_DOWN_ARROW = (0, 80)
        NUMPAD_RIGHT_ARROW = (0, 77)
        NUMPAD_LEFT_ARROW = (0, 75)
        CTRL_ENTER = (10,)
        OPTION_ENTER = CTRL_ENTER

    else:
        raise NotImplementedError(f"Platform `{platform.system()}` is not supported")

    @staticmethod
    def get_key_name(key_code: int) -> str:
        """
        Returns the human-readable name of a key given its code.

        Args:
            key_code (int): The key code to lookup.

        Returns:
            str: The human-readable name of the key.
        """
        if key_code in Keys.SPECIAL_CHARACTERS:
            return Keys.SPECIAL_CHARACTERS[key_code]
        for key_name, key_value in {
            "ENTER": Keys.ENTER,
            "TAB": Keys.TAB,
            "ESC": Keys.ESC,
            "SPACEBAR": Keys.SPACEBAR,
            "BACKSPACE": Keys.BACKSPACE,
            "DELETE": Keys.DELETE,
            "HOME": Keys.HOME,
            "END": Keys.END,
            "UP_ARROW": Keys.UP_ARROW,
            "DOWN_ARROW": Keys.DOWN_ARROW,
            "RIGHT_ARROW": Keys.RIGHT_ARROW,
            "LEFT_ARROW": Keys.LEFT_ARROW,
        }.items():
            if key_value and key_code == key_value[0]:
                return key_name
        if 32 <= key_code <= 126:
            return chr(key_code)
        return f"Unknown({key_code})"

    def __init__(self):
        raise RuntimeError("`Keys` class cannot be instantiated")


def get_key() -> Key:
    """
    Reads a single keypress and returns a Key object.

    Returns:
        Key: A Key object representing the keypress event.
    """
    if platform.system() in ("Windows", "CYGWIN"):
        import msvcrt

        ch = msvcrt.getch()
        key_codes = [ord(ch)]
        if ch in (b"\x00", b"\xe0"):
            key_codes.append(ord(msvcrt.getch()))
        key = "".join(chr(c) for c in key_codes)
        is_printable = ch.isprintable()
        description = get_description(tuple(key_codes), is_printable)
        return Key(key, tuple(key_codes), is_printable, description)

    else:
        import termios
        import tty

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            key_codes = [ord(ch)]

            # If the first character is an escape character, read more bytes
            if key_codes[0] == 27:  # ESC character
                ch = sys.stdin.read(2)  # Read the next two characters
                key_codes.extend(ord(c) for c in ch)

            key_codes_tuple = tuple(key_codes)
            is_printable = len(key_codes_tuple) == 1 and chr(key_codes_tuple[0]).isprintable()
            description = get_description(key_codes_tuple, is_printable)
            key = "".join(chr(c) for c in key_codes_tuple)
            return Key(key, key_codes_tuple, is_printable, description)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def get_description(key_codes: Tuple[int, ...], is_printable: bool) -> str:
    """
    Returns a description for the key based on its key codes and printability.

    Args:
        key_codes (Tuple[int, ...]): A tuple of integer key codes.
        is_printable (bool): Whether the key is a printable character.

    Returns:
        str: A human-readable description of the key.
    """

    if len(key_codes) == 1 and key_codes[0] in Keys.CTRL_LETTERS.values():
        letter = chr(key_codes[0] + 96)  # Convert back to the letter
        return f"Ctrl + {letter.upper()}"

    if not is_printable:
        if key_codes == Keys.ENTER:
            return "Enter"
        if key_codes == Keys.TAB:
            return "Tab"
        if key_codes == Keys.ESC:
            return "Esc"
        if key_codes == Keys.SPACEBAR:
            return "Spacebar"
        if key_codes == Keys.BACKSPACE:
            return "Backspace"
        if key_codes == Keys.DELETE:
            return "Delete"
        if key_codes == Keys.HOME:
            return "Home"
        if key_codes == Keys.END:
            return "End"
        if key_codes == Keys.UP_ARROW:
            return "Up Arrow"
        if key_codes == Keys.DOWN_ARROW:
            return "Down Arrow"
        if key_codes == Keys.RIGHT_ARROW:
            return "Right Arrow"
        if key_codes == Keys.LEFT_ARROW:
            return "Left Arrow"

        return f"Special ({key_codes})"

    if key_codes[0] in Keys.SPECIAL_CHARACTERS:
        return Keys.SPECIAL_CHARACTERS[key_codes[0]]

    return chr(key_codes[0])
