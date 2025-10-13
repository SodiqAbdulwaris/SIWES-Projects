userinput = input("Type here: ")
vwlcnt = 0
cnstcnt = 0

for letter in userinput:
    if letter.isalpha():
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            vwlcnt += 1
        else:
            cnstcnt += 1
    continue
if vwlcnt == 1:
    print(f"There is {vwlcnt} vowel in your input")
else:
    print(f"There are {vwlcnt} vowels in your input")
if cnstcnt == 1:
    print(f"There is {cnstcnt} consonant in your input")
else:
    print(f"There are {cnstcnt} consonants in your input")
    