import re 

# get names
names_file = open("data/names.txt", "r")
lines = names_file.readlines()

count = 0
total_lines = 0

# find duplicates
for line in lines: 
    fmtline = line.replace("\n", "").split(", ")
    name = fmtline[0]
    
    repeat = re.findall(r'(.)\1', name)
    # if len(repeat) > 0:
    #     print(len(repeat))
    count = count + len(repeat)
    total_lines = total_lines + len(name)
    

print("Number of consecutive repeated letters occurances: " + str(count)) # 62 / 208 (loosely <- doesn't need to be super accurate)
print("Total letters: " + str(total_lines)) # no letters minus repeats: 2028