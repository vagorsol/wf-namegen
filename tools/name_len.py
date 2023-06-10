# finds the average + range of name lengths for the given faction
def avg_name_len(lines):
    name_count = {}

    for line in lines: 
        fmtline = line.replace("\n", "")
        nameslst = []

        # account for names with dashes in corpus/grineer 
        if "-" in fmtline:
            if "-" not in name_count: 
                name_count["-"] = 0
            name_count["-"] += 1
            fmtline = fmtline.split("-")[0]

        # names with spaces
        if " " in fmtline: 
            spltline = fmtline.split(" ")
            nameslst.append(len(spltline[0]))
            nameslst.append(len(spltline[1]))
        else: 
            nameslst.append(len(fmtline))      

        for name_len in nameslst:
            if name_len not in name_count:
                name_count[name_len] = 0
            name_count[name_len] += 1
    
    # sort + output results
    if "-" in name_count:
        print("-: " + str(name_count["-"]))
        del name_count["-"]
    
    avg_len = 0
    amt = 0
    
    for key, value in sorted(name_count.items()): 
        print(str(key) + ": " + str(value))

        # get values to calculate average name length
        avg_len += (key * value)
        amt += key
    print("Average Name Length: " + str(avg_len / amt))

factions = ["corpus", "grineer", "veil", "loka", "suda", "hexis"]

print("Length: Amount\n")
for faction in factions: 
    filename = "data/names/" + faction + ".txt"
    file = open(filename, "r+")
    lines = file.readlines()

    print(faction)
    avg_name_len(lines)
    print()
