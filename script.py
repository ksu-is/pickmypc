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
