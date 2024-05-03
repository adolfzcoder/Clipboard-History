"""
This allows you to view your whole clipboard history, and select to copy them

"""

from write_paste import write_paste
import display_messages as dm

# write this to txt file


def main():
    write_paste()

    dm.display_clipboard()


if __name__ == "__main__":
    main()