

def loadOptions(type, options):
    f = open("config/"+type+"/convert.txt")
    convert2 = f.read().split('\n')
    convert = []
    for conversion in convert2:
        convert.append(conversion.split('='))
    f.close
    f = open("config/"+type+"/interpret.txt")
    interpret = f.read().split('\n')
    f.close()
    
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

    for option in options:
        print(option)
    return options

