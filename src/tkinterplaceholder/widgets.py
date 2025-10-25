import tkinter as tk
import ttkbootstrap as ttk

_DEFAULT_PH_FG_COLOR = "slategrey"

class Combobox(ttk.Combobox):
    __slots__ = ("_ph_text", "_ph_color", "_foreground_color")

    def __init__(self, master=None, **kwargs):
        if "ph_text" in kwargs:
            self._ph_text = kwargs.pop("ph_text")
        else:
            self._ph_text = ""
        
        if "ph_color" in kwargs:
            self._ph_color = kwargs.pop("ph_color")
        else:
            self._ph_color = _DEFAULT_PH_FG_COLOR

        super().__init__(master, **kwargs)

        if "foreground" in kwargs:
            self._foreground_color = kwargs["foreground"]
        else:
            self._foreground_color = ttk.Style().lookup(self.cget("style"), "foreground")

        self.bind("<FocusIn>", self.focus_in)
        self.bind("<FocusOut>", self.focus_out)

        if self.get() == "":
            self.configure(foreground=self._ph_color)
            self.insert(0, self._ph_text)

    def focus_in(self, event):
        if self.get() == self._ph_text:
            self.delete(0, tk.END)
            self.configure(foreground=self._foreground_color)

    def focus_out(self, event):
        if self.get() == "":
            self.insert(0, self._ph_text)
            self.configure(foreground=self._ph_color)

class Entry(ttk.Entry):
    __slots__ = ("_ph_text", "_ph_color", "_foreground_color")

    def __init__(self, master=None, **kwargs):
        if "ph_text" in kwargs:
            self._ph_text = kwargs.pop("ph_text")
        else:
            self._ph_text = ""
        
        if "ph_color" in kwargs:
            self._ph_color = kwargs.pop("ph_color")
        else:
            self._ph_color = _DEFAULT_PH_FG_COLOR

        super().__init__(master, **kwargs)

        if "foreground" in kwargs:
            self._foreground_color = kwargs["foreground"]
        else:
            self._foreground_color = ttk.Style().lookup(self.cget("style"), "foreground")

        self.bind("<FocusIn>", self.focus_in)
        self.bind("<FocusOut>", self.focus_out)

        if self.get() == "":
            self.configure(foreground=self._ph_color)
            self.insert(0, self._ph_text)

    def focus_in(self, event):
        if self.get() == self._ph_text:
            self.delete(0, tk.END)
            self.configure(foreground=self._foreground_color)

    def focus_out(self, event):
        if self.get() == "":
            self.insert(0, self._ph_text)
            self.configure(foreground=self._ph_color)

class Text(ttk.Text):
    __slots__ = ("_ph_text", "_ph_color", "_foreground_color")

    def __init__(self, master=None, **kwargs):
        if "ph_text" in kwargs:
            self._ph_text = kwargs.pop("ph_text")
        else:
            self._ph_text = ""
        
        if "ph_color" in kwargs:
            self._ph_color = kwargs.pop("ph_color")
        else:
            self._ph_color = _DEFAULT_PH_FG_COLOR

        super().__init__(master, **kwargs)

        if "foreground" in kwargs:
            self._foreground_color = kwargs["foreground"]
        else:
            self._foreground_color = ttk.Style().lookup("TEntry", "foreground")

        self.bind("<FocusIn>", self.focus_in)
        self.bind("<FocusOut>", self.focus_out)

        if self.get("1.0", tk.END).strip() == "":
            self.configure(foreground=self._ph_color)
            self.insert("1.0", self._ph_text)

    def focus_in(self, event):
        if self.get("1.0", tk.END).strip() == self._ph_text:
            self.delete("1.0", tk.END)
            self.configure(foreground=self._foreground_color)

    def focus_out(self, event):
        if self.get("1.0", tk.END).strip() == "":
            self.insert("1.0", self._ph_text)
            self.configure(foreground=self._ph_color)
