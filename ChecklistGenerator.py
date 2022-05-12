
import re

import enclosureOptions as options

def removeWhiteSpace(string):
    pieces = string.split('\"')
    for i, item in enumerate(pieces):
        if not i % 2:
            pieces[i] = re.sub("\s+", "", item)
    return '\"'.join(pieces)

def parseConfig(string):
    bags = {}
    
    string = removeWhiteSpace(string)

    bagsRaw = string.split('}')
    for bag in bagsRaw:
        bagRaw = bag.split('{')
        if (len(bag) > 0):
            bagName = bagRaw[0].replace("\"", "")
            bags[bagName] = []
            bagItems = bagRaw[1].split(',')
            for item in bagItems:
                bags[bagName].append(item.replace("\"", ""))

    for bagName in bags:
        print(bagName)
        for item in bags[bagName]:
            print("\t"+item)
            



def readConfiguration(type):
    f = open("config/"+type+"/items.txt")
    parseConfig(f.read())
    f.close()

#readConfiguration("xTool D1")

options1 = "xTool D1 Laser Enclosure Fume Hood Kit - Default Title #MWS Options 4247556978\nSKU:\nHide Description\n_mws_required:\n_mws_qty:1\n_mws_cart:1223086\nEstimated between:Apr 28, 2022 - May 5, 2022\nPanel Thickness:Commercial Grade 1/4\" Panels (Strongly Recommended)\nPanel Type: Full Laser Filtering\nPrinted Bracket Kit: Please Include Brackets and Parts\nUSB Exhaust Fan:No USB Exhaust Fan - Includes 4\" Mounting Bracket\nUSB Lighting Kit:No thank you.\nDoor Pulls (2 pieces):Plastic\nFitted MDF Spoil Board:No Thank you\nExtended height lift kit:Yes Please Include the lift kit\nHardware Grade:Nickel Plated Steel\n"

options.loadOptions("xTool D1", options1)
