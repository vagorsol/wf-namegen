# names to store later
grineer = [] 
corpus = []
hexis = []
suda = []
veil = []
loka = []


# get names
names_file = open("data/names.txt", "r")
lines = names_file.readlines()


# format + sort names
for line in lines: 
    fmtline = line.replace("\n", "").split(", ")
    name = fmtline[0]
    faction = fmtline[1].lower()
    
    if faction == "grineer":
        grineer.append(name)
    elif faction == "corpus":
        corpus.append(name)
    elif faction == "hexis":
        hexis.append(name)
    elif faction == "suda":
        suda.append(name)
    elif faction == "veil":
        veil.append(name)
    elif faction == "loka":
        loka.append(name)
    else:
        print("Cannot sort name: " + name + ", " + faction)

# write names to corresponding output files
with open("data/names/grineer.txt", "w+") as file:
    file.write(str(grineer))