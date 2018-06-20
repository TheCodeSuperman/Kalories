products = {"rice" : int(344),
            "boiled rice" : int(116),
            "carrot" : int(32)}
print("WARNING: When you write product without prefix it means that it is the raw product")
kilokalories_answ = None
product = input("Write your product >>> ")
grames = int(input("Write the count of grames >>> "))
if product in products:
    kilokalories_answ = products[product] / 100 * grames
    print("You've got %s kilokalories" % kilokalories_answ)
