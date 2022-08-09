total = int(input("Hoeveel kosten da\n"))
personen = int(input("Hoeveel personen zijn er\n"))
fooi = int(input("welke fooi wil je geven in %\n"))
print("Je moet " + str("%.2f" %(total/personen*(fooi/100+1))) + " euro betalen.")