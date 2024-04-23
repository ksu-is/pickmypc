def pickmypc():
    typestr = input("do you need a desktop (1) or laptop (2)?")
    type = int(typestr)
    if type == 1:
        print("desktop selected!")
    elif type == 2:
        print("laptop selected!")
    else:
        print("invalid submission. please try again")
    gamingstr = input("do you plan on using the system for gaming or video editing? 1 for yes, 2 for no")
    gaming = int(gamingstr)
    if gaming == 1:
        print("gaming/editing system selected")
    elif gaming == 2:
        print("non-gaming/editing system selected")

def budget():
    budgetstr = input("input 1 if your max budget is $100, 2 if max budget is $200, and so on5 (max is 10 or $1000)")
    budget = int(budgetstr)
    if budget == 1:
        print("budget $100 selected")
    elif budget == 2:
        print("budget $200 selected")
    elif budget == 3:
        print("budget $300 selected")
    elif budget == 4:
        print("budget $400 selected")
    elif budget == 5:
        print("budget $500 selected")
    elif budget == 6:
        print("budget $600 selected")
    elif budget == 7:
        print("budget $700 selected")
    elif budget == 8:
        print("budget $800 selected")
    elif budget == 9:
        print("budget $900selected")
    elif budget == 10:
        print("budget $1000 selected")
    else:
        print("invalid budget selection, please try again")

budget()
pickmypc()
