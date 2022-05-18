
import tkinter as tk
import ChecklistGenerator as ch

class WindowApplication(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.pack()

        self.textbox = tk.Entry()
        self.textbox.pack()

        self.textBoxContents = tk.StringVar()
        self.textBoxContents.set("Default Text")
        self.textbox["textvariable"] = self.textBoxContents
        self.textbox["fg"] = "grey"

        self.textbox.bind('<Key-Return>', self.generateChecklist)
    def generateChecklist(self, event):
        print("Textbox value", "\""+str()+"\"")
        options1 = self.textbox.get()

        checklist = ch.Checklist()
        checklist.loadOptions("xTool D1", options1)
        checklist.printItems()

        checklist.saveFile()

        

root = tk.Tk()
app = WindowApplication(root)
app.mainloop()
