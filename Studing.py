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
def start():
    product = input("Write your product >>> ")
    if product in products:
        grames = int(input("Write the count of grames >>> "))
        kk_answ = int(round(products[product] / 100 * grames))
        print("You've got %s kilokalories" % kk_answ)
        q = input("Do you want to make another one? y/n >>> ")
    else:
        print("There isn't such product in list. You may try again")
        start()
    if  q == "y":
        start()
    elif q == "n":
        exit(0)
    else:
        print("It isn't the correct answer. Write y/n >>>")
start()