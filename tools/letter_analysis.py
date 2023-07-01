import re 

# get names
names_file = open("data/names.txt", "r")
lines = names_file.readlines()

count = 0
repeat_occur = 0
total_letters = 0
vowel_count = 0
letters = {} 

for line in lines: 
    fmtline = line.replace("\n", "").split(", ")
    name = fmtline[0].lower()
    
    for letter in name:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1

    # duplicate letters
    # repeat = re.findall(r'(.)\1', name)
    # if len(repeat) > 0:
    #     print(name)
    #     repeat_occur = repeat_occur + 1
    # count = count + len(repeat)
    # total_letters = total_letters + len(name)
    # vowel_count = vowel_count + len(re.findall(r'[aeiou]', name))
    # vowels = re.findall(r'[aeiou]', name)

    

# print("Number of consecutive repeated letters occurances: " + str(count)) # 62 / 208 (loosely <- doesn't need to be super accurate)
# print("Number of Vowels: " + str(vowel_count))
# print("Number of Constonants: " + str(total_letters - vowel_count)) # 662:1490 vowel to const ratio (a bit off bc Titles BUT this is not a high-accuracy thing lbr)
# print("Total letters: " + str(total_letters)) # no letters minus repeats: 2028
# print(str(repeat_occur) + " " + str(len(lines)))

for key, value in sorted(letters.items()):
    print(str(key) + ": " + str(value))