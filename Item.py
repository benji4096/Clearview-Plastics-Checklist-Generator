﻿
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

    def getHtmlChecklistString(self, depth = 0):
        htmlString = f"<input type=\"checkbox\" id=\"{self.text}\"><label for=\"{self.text}\"> {self.text}</label><br>"
        for branch in self.branches:
            htmlString += branch.getHtmlChecklistString(depth + 1)
        return htmlString

    def push(self, item):
        self.branches.append(item)
        return item
