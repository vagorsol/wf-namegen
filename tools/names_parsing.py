# converts the list of names to a writable-to-file string
def formatting(lst, string):
    for word in lst:
        string += (word + "\n")
    return string


# writes a string of names to the corresponding output file
def fileout(factname, string):
    filename = "data/names/" + factname + ".txt"

    with open(filename, "w+") as file: 
        file.write(string) 

# names to store later
grineerLst = [] 
corpusLst = []
hexisLst = []
sudaLst = []
veilLst = []
lokaLst = []

grineer_names = ""
corpus_names = ""
hexis_names = ""
suda_names = ""
veil_names = ""
loka_names = ""


# get names
names_file = open("data/names.txt", "r")
lines = names_file.readlines()


# format + sort names
for line in lines: 
    fmtline = line.replace("\n", "").split(", ")
    name = fmtline[0]
    faction = fmtline[1].lower()

    if faction == "grineer":
        grineerLst.append(name)
    elif faction == "corpus":
        corpusLst.append(name)
    elif faction == "hexis":
        hexisLst.append(name)
    elif faction == "suda":
        sudaLst.append(name)
    elif faction == "veil":
        veilLst.append(name)
    elif faction == "loka":
        lokaLst.append(name)
    else:
        print("Cannot sort name: " + name + ", " + faction)

# convert list of names to string
grineer_names = formatting(grineerLst, grineer_names)
corpus_names = formatting(corpusLst, corpus_names)
hexis_names = formatting(hexisLst, hexis_names)
suda_names = formatting(sudaLst, suda_names)
veil_names = formatting(veilLst, veil_names)
loka_names = formatting(lokaLst, loka_names)

# write names to corresponding output files
fileout("grineer", grineer_names)
fileout("corpus", corpus_names)
fileout("suda", suda_names)
fileout("hexis", hexis_names)
fileout("veil", veil_names)
fileout("loka", loka_names)

print("Finished!")