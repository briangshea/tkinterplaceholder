import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from tkinterplaceholder.widgets import *

class MainWindows(ttk.Window):
    def __init__(self, *args, **kwargs):
        if not "themename" in kwargs:
            kwargs["themename"] = "darkly"

        super().__init__(*args, **kwargs)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.title("Placeholder Test")

        entry1 = Combobox(self, ph_text="Enter your name", width=40)
        entry1.pack(pady=5, padx=5)

        entry2 = Entry(self, ph_text="Enter your email", width=40)
        entry2.pack(pady=5, padx=5)

        entry3 = Entry(self, ph_text="Enter your phone", width=40)
        entry3.pack(pady=5, padx=5)

        text = Text(self, ph_text="Enter your message", width=40)
        text.pack(pady=5, padx=5)

    def on_closing(self):
        self.destroy()

if __name__ == "__main__":
    app = MainWindows()
    app.mainloop()