

class Item:
    def __init__(self, title, parameter = None, itemType = None):
        self.branches = []
        self.title = title
        self.itemType = None
        self.parameter = parameter

    def print(self, depth = 0):
        print("  "*depth, "»", self.title, sep = "")
        for branch in self.branches:
            branch.print(depth + 1);

    def push(self, item):
        self.branches.append(item)
        return item

class Checklist:
    def __init__(self):
        self.tree = Item("root")

    def loadOptions(self, enclosureType, options):
        with open("config/"+enclosureType+"/convert.txt") as f:
            convert2 = f.read().split('\n')
            convert = []
            for conversion in convert2:
                convert.append(conversion.split('='))
            
        with open("config/"+enclosureType+"/interpret.txt") as f:
            interpret = f.read().replace("\n\n", '\n').split('\n')
        
        for conversion in convert:
            options = options.replace(conversion[0], conversion[1])
        
        

        options = options.split('\n')

        for option in options:
            print(option)
        print()

        for i, line in sorted(enumerate(options), reverse=True):
            containsAnOption = False
            for otherLine in interpret:
                if line.find(otherLine) != -1:
                    containsAnOption = True
            if not containsAnOption:
                options.pop(i)

        for option in options:
            print(option)
        return options

    def printItems(self):
        self.tree.print();


options1 = "xTool D1 Laser Enclosure Fume Hood Kit - Default Title #MWS Options 4247556978\nSKU:\nHide Description\n_mws_required:\n_mws_qty:1\n_mws_cart:1223086\nEstimated between:Apr 28, 2022 - May 5, 2022\nPanel Thickness:Commercial Grade 1/4\" Panels (Strongly Recommended)\nPanel Type: Full Laser Filtering\nPrinted Bracket Kit: Please Include Brackets and Parts\nUSB Exhaust Fan:No USB Exhaust Fan - Includes 4\" Mounting Bracket\nUSB Lighting Kit:No thank you.\nDoor Pulls (2 pieces):Plastic\nFitted MDF Spoil Board:No Thank you\nExtended height lift kit:Yes Please Include the lift kit\nHardware Grade:Nickel Plated Steel\n"

#options.loadOptions("xTool D1", options1)

xToolList = Checklist()

xToolList.loadOptions("xTool D1", options1)

xToolList.printItems()
