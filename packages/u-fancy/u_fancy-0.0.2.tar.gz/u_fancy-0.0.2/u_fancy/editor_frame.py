import tkinter as tk
from tkinter import ttk

from pygments import lex
from pygments.lexers import PythonLexer
from pygments.styles import get_style_by_name

class Editor:
    STYLE = "default"
    TITLE = "Code Submission"
    
    def __init__(self, master, starter_text: str = "", main: bool = False):
        self.root = master
        self.main = main
        self.editor = None
        self.starter_text = starter_text
        self.text = None
        self.font = ("Ubuntu", 14, "bold")
        
        self.frame = ttk.LabelFrame(self.root) #, width=200, height=200
        self.add_widgets()
        
    def set_grid(self, _row: int = 0, _column: int = 0):
        self.frame.grid(row=_row, column=_column, padx=(20,10), pady=(5,0), sticky="nsew")
        
    def get_text(self):
        if self.editor:
            return self.editor.get("1.0", "end-1c")
        print("")
        return ""
    
    # Horizontal scroll bar goes here as well!
    def add_widgets(self):
        # self.root.title("Problem Z")
        self.yscrollbar = ttk.Scrollbar(self.frame, orient="vertical")
        self.editor = tk.Text(self.frame, yscrollcommand=self.yscrollbar.set)
        self.editor.insert(tk.INSERT, self.starter_text)
        self.editor.grid(column=1, row=0, sticky="nsew") #pack(side="left", fill="both", expand=1)
        self.editor.config(wrap="word",  # use word wrapping
                           undo=True,  # Tk 8.4
                           width=40,
                           height=15,
                           tabs="1c")
        self.editor.configure(font = self.font, tabs="1c")
        self.editor.focus()
        # self.yscrollbar.pack(side="right", fill="y")
        self.yscrollbar.grid(row=3, column=5, sticky="nsew")
        self.yscrollbar.config(command=self.editor.yview)
        # self.frame.pack(fill="both", expand=1)
        
        self.editor.bind("<Control-y>", self.redo)
        self.editor.bind("<Control-Y>", self.redo)
        self.editor.bind("<Control-Z>", self.undo)
        self.editor.bind("<Control-z>", self.undo)
        self.editor.bind("<KeyRelease>", self.syntax_highlight_update)
        
        if self.main:
            self.get_text_button = ttk.Button(self.root, text="Send Submission", command=self.get_text)
            self.get_text_button.grid(row=5, column=0)

        self.syntax_highlight_init()
        # No menu
        
    def syntax_highlight_init(self):
        style = get_style_by_name(self.STYLE)
        for t, s in style:
            name = str(t)
            for k,v in s.items():
                if k == "color" and v:
                    self.editor.tag_configure(name, foreground="#{}".format(v))
                elif k == "bgcolor" and v:
                    pass # self.editor.tag_configure(name, background="#{}".format(v))
        
    def syntax_highlight_update(self, event=None):
        self.editor.mark_set("range_start", "1.0")
        data = self.editor.get("1.0", "end-1c")
        
        for token, content in lex(data, PythonLexer()):
            self.editor.mark_set("range_end", "range_start + %dc" % len(content))
            self.editor.tag_add(str(token), "range_start", "range_end")
            self.editor.mark_set("range_start", "range_end")
            
    """
    def add_text(self):
        self.text = Text(self.root, wrap="none", width=50, height = 100, tabs='    ')
        xscrollbar = Scrollbar(self.root, orient=HORIZONTAL)
        xscrollbar.pack(side=BOTTOM, fill=X)

        yscrollbar = Scrollbar(self.root)
        yscrollbar.pack(side=RIGHT, fill=Y)

        self.text.config(
            xscrollcommand=xscrollbar.set,
            yscrollcommand=yscrollbar.set)
        xscrollbar.config(command=self.text.yview)
        yscrollbar.config(command=self.text.xview)

        self.text.pack()
    """
    
    def undo(self, event = None):
        self.editor.edit_undo()
        
    def redo(self, event = None):
        self.editor.edit_redo()
        
    def edit_copy(self):
        text = self.editor.get(SEL_FIRST, SEL_LAST)
        self.root.clipboard_clear()
        self.root.clipboard_append(text)

    def edit_paste(self):
        self.editor.insert(INSERT, root.clipboard_get())
        
if __name__ == "__main__":
    root = tk.Tk()
    
    root.tk.call("source", "/usr/Sphinx/themes/Azure-ttk-theme-main/azure.tcl")
    root.tk.call("set_theme", "dark")
    
    editor_frame = Editor(root)
    editor_frame.set_grid()
    
    root.mainloop()
