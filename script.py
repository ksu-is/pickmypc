def lord():
    typestr = input("do you need a desktop (1) or laptop (2)?")
    typeof = int(typestr)
    if typeof == 1:
        print("desktop selected!")
    elif typeof == 2:
        print("laptop selected!")
    else:
        print("invalid submission. please restart")
    return typeof
def gaming():
    gamingstr = input("do you plan on using the system for gaming or video editing? 1 for yes, 2 for no")
    gaming = int(gamingstr)
    if gaming == 1:
        print("gaming/editing system selected")
    elif gaming == 2:
        print("non-gaming/editing system selected")
    else:
        print("invalid selection. please restart")
    return gaming
        

def budget():
    budgetstr = input("input 1 if your max budget is $100, 2 if max budget is $200, and so on (max is 10 or $1000)")
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
        print("budget $900 selected")
    elif budget == 10:
        print("budget $1000 selected")
    else:
        print("invalid budget selection, please try again")
    return budget
def cad():
    cadstr = input("do you plan on using the system for CAD software or intense photo editing? 1 for yes, 2 for no")
    cad = int(cadstr)
    if cad == 1:
        print("CAD/photo editing system selected!")
    elif cad == 2:
        print("NON CAD/photo editing system selected!")
    return cad

isbudget=budget()
islord=lord()
isgaming=gaming()
iscad=cad()

if isbudget == 1 and isgaming == 1 and islord == 1:
    print("you are in a difficult spot. \n your best best is looking for a local deal where someone's getting rid of an older system. you should look for a system with no older than a 2nd generation i5, 8GB of memory, a small solid state drive, and a video card with no less than 1GB of VRAM. Ask the seller if their system meets these requirements. Good luck.")
if isbudget == 1 and isgaming == 1 and islord == 2:
    print("your only chance of finding a suitable system is a good deal on an older Dell Precision, HP ZBook, or Lenovo W series system using 2nd-5th generation Intel processors (years 2012-2015). Anything newer will likely exceed your budget.")
if isbudget == 1 and isgaming == 2 and islord == 1 and iscad == 1:
    print("you may be able to find a local deal for an older system. look for something with a 2nd-6th generation i5, at least 8GB of memory, and a solid state hard drive. Bonus points if you can find a system that has a video card.")
if isbudget == 1 and isgaming == 2 and islord == 2 and iscad == 1:
    print("you may be able to find a local deal for an older system. look for something with a 2nd-6th generation i5, at least 8GB of memory, and a solid state hard drive.")
if isbudget == 1 and isgaming == 2 and islord == 1 and iscad == 2:
    print("look locally or on ebay for a system with a 2nd-4th generation i5/17, at least 8GB of memory, and a solid state hard drive with at least 120GB of storage. You may be able to find one with extra storage, or an additional HDD.")
if isbudget == 1 and isgaming == 2 and islord == 2 and iscad == 2:
    print("look locally/on ebay for a laptop with a 2nd-5th generation i5/i7, at least 8GB of memory, and a solid state hard drive with at least 120GB of storage.")


if isbudget == 2 and isgaming == 1 and islord == 1:
    print("for under $200, you should be able to find an older system with a 2nd-6th generation i5-i7, at least 8GB of memory, a solid state hard drive, and a video card with at least 2GB of VRAM. First, try looking for a system with a 4GB video card.")
if isbudget == 2 and isgaming == 1 and islord == 2:
    print("for under $200, try to find a 6th generation Intel Dell Precision, HP ZBook, or Lenovo P50 series laptop.")
if isbudget == 2 and isgaming == 2 and islord == 2 and iscad == 1:
    print("for under $200, try to find a 6th generation Intel Dell Precision, HP ZBook, or Lenovo P50 series laptop.")
if isbudget == 2 and isgaming == 2 and islord == 1 and iscad == 1:
    print("for under $200, try to find a system with a 6th-7th generation Intel processor, at least 8GB of memory, a solid state drive, and a video card with at least 1GB of VRAM.")
if isbudget == 2 and isgaming == 2 and islord == 2 and iscad == 2:
    print("for under $200, you should be able to find a laptop with a 6th-8th generation Intel processor, at least 8GB of memory, and a solid state hard drive. This will be a good user experience.")
if isbudget == 2 and isgaming == 2 and islord == 1 and iscad == 2:
    print("for under $200, you should be able to find a desktop with a 6th-8th generation Intel processor, at least 8GB of memory, and a solid state hard drive. This will be a good user experience.")
