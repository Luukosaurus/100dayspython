from tracemalloc import stop


print("__________████████_____██████\n_________█░░░░░░░░██_██░░░░░░█\n________█░░░░░░░░░░░█░░░░░░░░░█\n_______█░░░░░░░███░░░█░░░░░░░░░█\n_______█░░░░███░░░███░█░░░████░█\n______█░░░██░░░░░░░░███░██░░░░██\n\
_____█░░░░░░░░░░░░░░░░░█░░░░░░░░███\n____█░░░░░░░░░░░░░██████░░░░░████░░█\n____█░░░░░░░░░█████░░░████░░██░░██░░█\n___██░░░░░░░███░░░░░░░░░░█░░░░░░░░███\n__█░░░░░░░░░░░░░░█████████░░█████████\n\
_█░░░░░░░░░░█████_████___████_█████___█\n_█░░░░░░░░░░█______█_███__█_____███_█___█\n█░░░░░░░░░░░░█___████_████____██_██████\n░░░░░░░░░░░░░█████████░░░████████░░░█\n░░░░░░░░░░░░░░░░█░░░░░█░░░░░░░░░░░░█\n\
░░░░░░░░░░░░░░░░░░░░██░░░░█░░░░░░██\n░░░░░░░░░░░░░░░░░░██░░░░░░░███████\n░░░░░░░░░░░░░░░░██░░░░░░░░░░█░░░░░█\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n\
░░░░░░░░░░░█████████░░░░░░░░░░░░░░██\n░░░░░░░░░░█▒▒▒▒▒▒▒▒███████████████▒▒█\n░░░░░░░░░█▒▒███████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█\n░░░░░░░░░█▒▒▒▒▒▒▒▒▒█████████████████\n░░░░░░░░░░████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█\n\
░░░░░░░░░░░░░░░░░░██████████████████\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n██░░░░░░░░░░░░░░░░░░░░░░░░░░░██\n▓██░░░░░░░░░░░░░░░░░░░░░░░░██\n▓▓▓███░░░░░░░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░░░░██\n\
▓▓▓▓▓▓▓▓▓███████████████▓▓█\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█")
print("Welcome to L Bozo island")
print("Het is je taak om te vinden wie vroeg")
q1 = input("Je komt in de buurt van Erik en hij wil al je geld stelen.\nWat doet je, Je geeft je geld of je rent weg. Type 'geef' of 'ren'\n")
if q1 == "ren":
    print("Dat was slim je bent weg gekomen en je hebt al je geld nog")
    q2 = input("Je komt Sven tegen en hij ziet er uit alsof hij je wat te vertellen heeft. \nWat doe je, negeer je hem of zeg je wat is er Sven. Type 'negeer' of 'wat is er sven'\n")
    if q2 == "negeer":
        print("Poeh op het nippertje hij had bijna een 2 uur verhaal verteld over zijn nieuwe plugin die hij had gemaakt met enkel commandblocks")
        q3 = input("Onee Ole komt op je af hij ziet er gevaarlijk uit en op basis van ervaring weet je dat het niet slim is om in contact met hem te komen.\nWat doe je, Je zegt hi, je rent of je steelt zijn geld. Type `hi` of `ren` of 'steel'\n")
        if q3 == "hi":
            print("Slim je zij hi tegen Ole doneerde je 30 euro ondanks dat hij zij dat hij ging stoppen met geld doneren")
            print("Je taak is helaas niet voltooid want je hebt nog steeds niemand gevonden die vroeg")
        elif q3 == "steel":
            print("Ojee dat was gevaarlijk Ole heeft je beschoten en nu bloed je dood")
            print("Je hebt niemand gevonden die vroeg")
        else:
            print("Je liep door en je ziet achter je dat Ole 30 euro geeft aan Erik.\nJe blijft achter je kijken en ziet niet waar je loopt en je valt in een gad rip bozo")
            print("Je hebt niemand gevonden die vroeg")
    else:
        print("Onee na dat je vroeg wat er was heeft sven je een zes daagse uitleg gegeven over zijn zelf gemaakte commandblock plugin je hebt zelfmoord gepleegd")
        stop
else:
    print("rip bozo Erik heeft al je geld en heeft er 1000 euro webstore icoontjes van gekocht en toen je er wat van zij shankde hij je")
    stop

