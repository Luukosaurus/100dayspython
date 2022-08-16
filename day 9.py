print("welkom bij silent ah")
done = False
ah_dic = {}
oldbet = 0
while not done:
    username = input("Wat is je naam\n")
    bet = int(input("Wat is je bet\n"))
    ah_dic[username] = bet
    areyoudone = input("Ben je klaar ja of nee\n")
    if areyoudone in "ja":
        done = True
print(ah_dic)
for i in ah_dic:
    if ah_dic[i] > oldbet:
        oldbet = ah_dic[i]
        bestuser = i
print(f"{bestuser} heeft gewonnen met een bet van {str(oldbet)} euro")

