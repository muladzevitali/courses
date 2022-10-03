import shutil
import sys


class Singleton(type):
    _instances = dict()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class EscapeSequence(metaclass=Singleton):
    @staticmethod
    def save_cursor_position():
        sys.stdout.write("\0337")

    @staticmethod
    def restore_cursor_position():
        sys.stdout.write("\0338")

    @staticmethod
    def move_to_top_of_screen():
        sys.stdout.write("\033[H")

    @staticmethod
    def delete_line():
        sys.stdout.write("\033]2k")

    @staticmethod
    def clear_line():
        sys.stdout.write("\033]2K\033[0G")

    @staticmethod
    def move_back_one_char():
        sys.stdout.write("\033[1D")

    @staticmethod
    def move_to_bottom_of_screen() -> int:
        _, total_rows = shutil.get_terminal_size()
        input_row = total_rows - 1
        sys.stdout.write(f"\033[{input_row}E")
        return total_rows
