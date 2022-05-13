
import sys
import importlib

from Item import *

class Checklist:
    def __init__(self):
        self.tree = None
        self.modules = {}

    def loadOptions(self, enclosureType, options):
        with open("config/"+enclosureType+"/convert.txt") as f:
            convert2 = f.read().split('\n')
            convert = []
            for conversion in convert2:
                convert.append(conversion.split('='))
            
        with open("config/"+enclosureType+"/interpret.txt") as f:
            interpret = f.read().replace("\n\n", '\n').split('\n')
        
        options = options.replace(": ", ':').replace(" :", ':').replace(" : ", ':')

        for conversion in convert:
            options = options.replace(conversion[0], conversion[1])

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
        self.tree.print()



