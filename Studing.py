products = {"rice" : int(344),
            "boiled rice" : int(116),
            "carrot" : int(32)}
print("WARNING: When you write product without prefix it means that it is the raw product")
kk_answ = None
def start():
    product = input("Write your product >>> ")
    grames = int(input("Write the count of grames >>> "))
    if product in products:
        kk_answ = products[product] / 100 * grames
        print("You've got %s kilokalories" % kk_answ)
    else:
        print("There isn't such product in list. You may try again")
        start()
    q = input("Do you want to make another one? y/n >>> ")
    if  q == "y":
        start()
    elif q == "n":
        exit(0)
start()

