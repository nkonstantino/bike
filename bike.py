import enchant
d = enchant.Dict("en_US")
let1 = ["b","s","p","h","m","t","w","d","l","f"]
let2 = ["a","i","l","e","y","h","n","r","u","o"]
let3 = ["r","t","a","o","s","k","e","n","m","l"]
let4 = ["s","n","m","p","y","l","k","t","e","d"]


words = []
realwords = []

for letter1 in let1:
    for letter2 in let2:
        for letter3 in let3:
            for letter4 in let4:
                words.append(str(letter1) + str(letter2) + str(letter3) + str(letter4))

for word in words:
    if d.check(word):
        realwords.append(word)
    else:
        continue

print(realwords)