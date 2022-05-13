
import sys
import importlib
import json

from Item import *

class Checklist:
    def __init__(self):
        self.tree = None
        self.modules = {}
        
    def loadOptions(self, enclosureType, options):
        with open("config/"+enclosureType+"/convert.json", 'r') as f:
            convert = json.load(f)
        with open("config/"+enclosureType+"/interpret.json", 'r') as f:
            interpret = json.load(f)

        for key in convert:
            options = options.replace(key, convert[key])
            
        options = options.split('\n')
            
        for i, line in sorted(enumerate(options), reverse=True):
            containsAnOption = False
            for otherLine in interpret:
                if line.find(otherLine) != -1:
                    containsAnOption = True
            if not containsAnOption:
                options.pop(i)

        optionsDict = {}

        for option in options:
            optionPair = option.split(':')
            optionsDict[optionPair[0]] = optionPair[1]

        sys.path.insert(0, "config/"+enclosureType)
        self.modules[enclosureType] = importlib.import_module("loadTree")
        self.tree = self.modules[enclosureType].main(enclosureType, optionsDict)

    def printItems(self):
        if self.tree is not None:
            self.tree.print()

    def saveFile(self):
        if self.tree is not None:
            with open("templates/print.html", 'r') as f:
                htmlText = f.read()

        htmlText = htmlText.replace("${checkboxes}", self.tree.getHtmlChecklistString())
        
        with open("out/print.html", 'w', encoding="utf-8") as f:
            f.write(htmlText)

