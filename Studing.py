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
def setgrams(set):
    try:
        qsetgrams = int(input("Write the count of grams >>> "))
        setlist.append(round(int(products[set]) / 100 * qsetgrams))
        startset()
    except ValueError:
        print("Grams should be number. Try again")
        setgrams(set)
def startset():
    set = None
    while True:
        set = input("Write your product or \"stop\" when set is done >>> ")
        if set in products and set != "stop":
            setgrams(set)
        elif set == "stop":
            print("Here's count of kilokalories in your set: %s kk" % sum(setlist))
            firstquiz()
            break
        else:
            print("There isn't such product in our list")
def calculation(grams, product):
    kk_answ = int(round(products[product] / 100 * grams))
    print("You've got %s kilokalories" % kk_answ)
    firstquiz()
def startgrams(product):
    try:
        grams = int(input("Write the count of grames >>> "))
        calculation(grams, product)
    except ValueError:
        print("Grams should be number. Try again")
        startgrams(product)
def start():
    product = input("Write your product >>> ")
    if product in products:
        startgrams(product)
    else:
        print("There isn't such product in list. You may try again")
        start()
def firstquiz():
    startq = input('''Write \"set\" to calculate several products
or \"product\" to calculate a product
or \"exit\" to exit program >>> ''')
    if startq == "set":
        startset()
    elif startq  == "product":
        start()
    elif startq  == "exit":
        exit(0)
    else:
        print("Write \"set, product or exit\" >>> ")
        firstquiz()
firstquiz()