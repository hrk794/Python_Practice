def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.", "It's really very, VERY runny, sir.", shopkeeper="Michael Palin", client="john Cleese", sketch="Cheese Shop Sketch")

print()
print("*" * 50)
print()

def halwai_ki_dukaan(chiz, *samvaad, **menu):
    print(chiz, "hai kya Babuji?")
    print("Arey nahi nahi; saari", chiz, "toh abhi thodi der pahile khatam ho gayi")
    for vakya in samvaad:
        print(vakya)
    print("-" * 40)
    for item in menu:
        print(item, ":", menu[item], "rupaye")

halwai_ki_dukaan("kaju katli", "Oho, ab kya lu?", "Baki sab to milega, usme kuch bhi le lijiye", "Accha. Abhi kya mile wo bataiye na zara", samose=15, wadapaav=12, Pede=100, KesarPede=120, Barfi=150, Rasmalai=100, Rabdi=80)

# Note that the order of the entries in the dictionary is arbitrary. I am using Python 3.5.2

