products = {"rice" : 344,
            "boiled rice" : 116,
            "carrot" : 29,
            "orange juice" : 36,
            "chicken sausages" : 229,
            "milk sausages" : 260,
            "pig sausages" : 284,
            "cow sausages": 229,
            "sunflower oil" : 899,
            "green pea" : 75,
            "garlic" : 103,
            "honey" : 312,
            "sugar" : 377,
            "black chocolate" : 546,
            "milk chocolate" : 552,
            "black tea with lemon and sugar" : 41,}
print("Created by Artem Khodak, Anton Khodak, Stas Dubov")
print("WARNING: When you write product without prefix it means that it is the raw product")
kk_answ = None
kkset_answ = None
setlist = []
def setgrames(set):
    qsetgrames = int(input("Write the count o grames >>> "))
    setlist.append(round(int(products[set]) / 100 * qsetgrames))
    startset()
def startset():
    set = None
    while True:
        set = input("Write your product or \"stop\" when set is done >>>")
        if set in products:
            setgrames(set)
        elif set == "stop":
            print(sum(setlist))
            break
        else:
            print("There isn't such product in our list")
def restart():
    q = input("Do you want to make another one? y/n >>> ")
    if  q == "y":
        start()
    elif q == "n":
        exit(0)
    else:
        print("It isn't the correct answer. Write y/n >>>")
        restart()
def calculation(grames, product):
    kk_answ = int(round(products[product] / 100 * grames))
    print("You've got %s kilokalories" % kk_answ)
    restart()
def startgrames(product):
    try:
        grames = int(input("Write the count of grames >>> "))
        calculation(grames, product)
    except ValueError:
        print("Grames should be number. Try again")
        startgrames(product)
def start():
    product = input("Write your product >>> ")
    if product in products:
        startgrames(product)
    else:
        print("There isn't such product in list. You may try again")
        start()
def firstquiz():
    startq = input("Write \"set\" to calculate several products or \"product\" to calculate a product >>> ")
    if startq == "set":
        startset()
    elif startq  == "product":
        start()
    else:
        print("Write \"set\" or \"product\" >>> ")
        firstquiz()
firstquiz()