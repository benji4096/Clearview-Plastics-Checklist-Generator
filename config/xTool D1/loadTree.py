
import sys
sys.path.append("../../")
from Item import *

def main(enclosureType, options):
    print("Loading tree for:", enclosureType)

    ######## --ITEM INIT-- ########
    #def __init__(self, title, parameter = None, itemType = None):
    
    #print(options)

    rtn = Item("root")



    panelThickness = options["Panel Thickness"]

    rtn.push(Item("Panels" + " " + panelThickness + " " + options["Panel Type"]))

    
    
    bag1 = rtn.push(Item("Bag #1", ItemType.BAG))
    bag2 = rtn.push(Item("Bag #2", ItemType.BAG))
    bag3 = rtn.push(Item("Bag #3", ItemType.BAG))



    if (options["Printed Parts"] == "true"):
        bag1.push(Item("2x Corner Brackets" + " " + panelThickness, ItemType.CHECK_BOX))
        bag1.push(Item("2x Magnetic Brackets" + " " + panelThickness, ItemType.CHECK_BOX))
    else:
        bag1.push(Item("4x Magnets", ItemType.CHECK_BOX))
        
    if (options["Spoil Board"] == "true"):
        bag1.push(Item("Spoil Board Hardware", ItemType.CHECK_BOX))
        bag2.push(Item("Hardware" + " " + panelThickness, ItemType.CHECK_BOX))

    if (options["Lift Kit"] == "true"):
        rtn.push(Item("Lift Kit", ItemType.CHECK_BOX))
    

    return rtn
