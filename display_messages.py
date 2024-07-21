import tkinter as tk
from tkinter import scrolledtext


def display_clipboard():
        
    def extract_messages(filename):
        messages = []  # list to store all fully extracted messages
        current_message = []  # store current msgs

        with open(filename, "r") as file:
            inside_message = False

            for line in file:
                if line.strip() == "Start":
                    inside_message = True
                    current_message = []  # reset current msg

                elif line.strip() == "UniqueEndMsgLOL":
                    inside_message = False
                    # join with exisiting lines
                    messages.append("".join(current_message))
                    current_message = []  # reset current msg

                elif inside_message:
                    current_message.append(line)

        return messages

    def copy_message(event, root):
        root.clipboard_clear()
        root.clipboard_append(event.widget.get("1.0", "end-1c"))

    def display_messages(messages):
        root = tk.Tk()
        root.title("Extracted Messages")

        text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20)
        text_area.pack(fill="both", expand=True)
        
        for message in messages[::-1]:
            message_text = message + "\n\n"
            text_area.insert(tk.END, message_text)
            text_area.tag_add("copyable", "end-2l", "end-1c")
            text_area.tag_bind("copyable", "<Button-1>", lambda event, root=root: copy_message(event, root))
            

        root.mainloop()

# give message .txt file
    messages = extract_messages("clipboard.txt")
    display_messages(messages)
    # for message in messages:
    #     print("Extracted message:\n", message)
        