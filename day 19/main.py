whatgame = input("Wat wil je doen gokken of tekenen\n")
if whatgame == "gokken":
    import turtlerace
    turtlerace.Race()
elif whatgame == "tekenen":
    import sketch