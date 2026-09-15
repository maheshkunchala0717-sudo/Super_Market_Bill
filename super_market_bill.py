name = input("Enter your Name:")
from datetime import date
today=date.today()


lists = '''
Rice       Rs 10/kg
Sugar      Rs 8/kg
Oil        Rs 30/liter
Salt       Rs 25/kg
Paneer     Rs 40/kg
Maggie     Rs 12/pack
Boost      Rs 200/bottle
'''

price = 0
pricelist = []
totalprice = 0
Finalprice = 0
ilist = []
qlist = []
plist = []


items = {'rice': 10, 'sugar': 8, 'oil': 30, 'salt': 25, 'paneer': 40, 'maggie': 12, 'boost': 200}

while True:
    option = input("Press 1 for list or 2 to exit: ")
    if option == '2':
        print("Thank you for shopping")
        break
    elif option == '1':
        print(lists)

        while True:
            inp1 = input("To buy press 1 or press 2 to exit: ")
            if inp1 == '2':
                print("Thank you for shopping")
                break
            elif inp1 == '1':
                item = input("Choose your items: ").lower()
                while True:
                    quantity_input = input("Enter quantity: ")
                    if quantity_input.isdigit(): 
                        quantity = int(quantity_input)
                        break
                    else:
                        print("Please enter a valid quantity.")

                if item in items:
                    price = quantity * items[item]
                    pricelist.append((item, quantity, items[item], price))
                    totalprice += price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print("Selected item is not available.")

        if totalprice > 0:
            tax = (totalprice * 18) / 100
            finalamount = tax + totalprice

            print(25 * "=", "Mahesh Kunchala Super Market", 25 * "=")
            print(25 * " ", "Hyderabad")
            print("Name:", name, 25 * " ",today)
            print(50 * "-")
            print("sno", 10 * " ", 'items', 10 * " ", 'quantity', 10 * " ", 'price')
            for i in range(len(pricelist)):
                print(i, 10 * " ", ilist[i], 10 * " ", qlist[i], 10 * " ", plist[i])
            print(25 * "-")
            print(25 * " ", 'Total amount:', 'Rs', totalprice)
            print("Tax amount", 25 * " ", 'Rs', tax)
            print(50 * "-")
            print(50 * " ", 'Final amount:', 'Rs', finalamount)
            print(50 * "-")
            print(50 * " ", "Thank you & Visit again")
            print(50 * "-")
