alphabet = "abcdefghijklmnopqrstuvwxyz"
def encrypt(text,change):
    code = ""
    for letter in text:
        pos = alphabet.index(letter)
        newpos = pos + change
        while newpos > 25:
            newpos -= 26
        code += alphabet[newpos]
    return code
def decrypt(text,change):
    code = ""
    for letter in text:
        pos = alphabet.index(letter)
        newpos = pos - change
        while newpos < 0:
            newpos += 26
        code += alphabet[newpos]
    return code
while True:
    todo = input("Wat wil je doen encrypt of decrypt\n")
    if todo == "encrypt":
        text = input("Welke text wil je decrypten\n")
        change = int(input("Wat is de verandering\n"))
        newtext = encrypt(text,change)
        print(newtext)
    elif todo == "decrypt":
        text = input("Welke text wil je decrypten\n")
        change = int(input("Wat is de verandering\n"))
        newtext = decrypt(text,change)
        print(newtext)
    stop = input("Wil je stoppen 'Ja' of 'nee'")
    if stop in "ja":
        exit()
