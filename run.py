
import ChecklistGenerator as ch

try:
    with open("options.txt", 'r') as f:
        options = f.read()
except:
    print("[********** WARNING **********]: Using default options")
    options = "xTool D1 Laser Enclosure Fume Hood Kit - Default Title #MWS Options 4247556978\nSKU:\nHide Description\n_mws_required:\n_mws_qty:1\n_mws_cart:1223086\nEstimated between:Apr 28, 2022 - May 5, 2022\nPanel Thickness:Commercial Grade 1/4\" Panels (Strongly Recommended)\nPanel Type: Full Laser Filtering\nPrinted Bracket Kit: Please Include Brackets and Parts\nUSB Exhaust Fan:No USB Exhaust Fan - Includes 4\" Mounting Bracket\nUSB Lighting Kit:No thank you.\nDoor Pulls (2 pieces):Plastic\nFitted MDF Spoil Board:No Thank you\nExtended height lift kit:Yes Please Include the lift kit\nHardware Grade:Nickel Plated Steel\n"

checklist = ch.Checklist()

checklist.loadOptions("xTool D1", options)

checklist.printItems()

checklist.saveFile()
