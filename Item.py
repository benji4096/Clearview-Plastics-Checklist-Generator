
from enum import Enum

class ItemType(Enum):
    BAG = 0
    CHECK_BOX = 1
    

class Item:
    def __init__(self, text, itemType = None):
        self.branches = []
        self.text = text
        self.itemType = itemType

    def print(self, depth = 0):
        print("  "*depth, "»", sep = "", end="")
        if (self.itemType == ItemType.CHECK_BOX):
            print("[_] ", end="")
        print(self.text)
        
        for branch in self.branches:
            branch.print(depth + 1)

        #    │
        #    ├
        #    └
        #    │
        #    ├
        #    ╰

    def getHtmlChecklistString(self, depth = 0, lastAtDepth = False):
        
        if self.text != "root":
            indent = max(depth - 1, 0) * "│ "

            if lastAtDepth:
                indent += "└ "
            else:
                indent += "├ "

            printTextBegin = f"{indent}"
            printTextEnd = f"{self.text}"

            htmlString = "ERROR: html string not set"
            if self.itemType == ItemType.BAG:
                htmlString = f"<span>{printTextBegin+printTextEnd}</span><br>"
            elif self.itemType == ItemType.CHECK_BOX:
                htmlString = f"<span>{printTextBegin}</span><input type=\"checkbox\" id=\"{self.text}\"><label for=\"{self.text}\"> {printTextEnd}</label><br>"
            elif self.itemType is None:
                htmlString = f"<span>{printTextBegin+printTextEnd}</span><br>"
        else:
            htmlString = ""

        for branch in self.branches:
            htmlString += branch.getHtmlChecklistString(depth + 1, True if branch is self.branches[-1] else False)
        return htmlString

    def push(self, item):
        self.branches.append(item)
        return item
