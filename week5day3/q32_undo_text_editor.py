# 32. Implement Undo functionality in a text editor using a Stack


class TextEditor:
    def __init__(self, text=""):
        self.text = text
        self.undo_stack = []

    def type_text(self, new_text):
        self.undo_stack.append(self.text)
        self.text += new_text

    def undo(self):
        if self.undo_stack:
            self.text = self.undo_stack.pop()
            return self.text
        return None


if __name__ == "__main__":
    editor = TextEditor("Hello")
    editor.type_text(" World")
    print("After typing:", editor.text)
    editor.undo()
    print("After undo:", editor.text)
