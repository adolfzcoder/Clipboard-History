import pyperclip

def write_paste():
    # get text from clipboard
    clipboard_text = pyperclip.paste()
    # write to file every copied text
    with open("clipboard.txt", "a") as file:
        print("Text from clipboard:", clipboard_text)
        file.write("Start\n\n")
        file.write(f"{clipboard_text}\n")
        file.write("UniqueEndMsgLOL\n\n")