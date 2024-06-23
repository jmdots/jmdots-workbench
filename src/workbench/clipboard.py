
import pyperclip

class Clipboard:
    """A class to handle clipboard operations."""

    def copy(self, text):
        """Copy the given text to the clipboard."""
        pyperclip.copy(text)

    def paste(self):
        """Paste the current clipboard contents."""
        return pyperclip.paste()
