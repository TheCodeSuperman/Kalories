kalories_answ = None
products = {'rice' : 90}
product = input("Write your product >>> ")
kalories = int(input("Write the count of grames >>> "))
if product in products:
    kalories_answ = products[product] / 100 * kalories
    print("You've got %s kalories" % kalories_answ)