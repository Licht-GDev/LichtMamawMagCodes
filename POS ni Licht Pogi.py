from tabulate import tabulate
import numpy as np
import sys

print("POS System Prototype")


def order():

    global orders
    global items

    orders = []
    items = []
    while True:

        var_order = (input("Menu \n 1. Burger - 50\n 2. Fries - 25 \n 3. Ice Cream - 10 \n 4. Iced Tea - 5\n 5. Check Out \n 6. Exit \n Please Enter Order: "))
        if var_order == "1":

            menu1_quantity = float(input("Quantity: "))

            orders.append(menu1_quantity * 50)
            items.append("Burger x" + str(menu1_quantity))
            print("Burger x" + str(menu1_quantity) + " added")
            continue

        elif var_order == "2":
            menu2_quantity = float(input("Quantity: "))

                
            orders.append(menu2_quantity * 25)
            items.append("Fries x" + str(menu2_quantity))
            print(orders)
            print("Fries x" + str(menu2_quantity) + " added")
            continue
            
        elif var_order == "3":
            menu3_quantity = float(input("Quantity: "))
                
            orders.append(menu3_quantity * 10)
            items.append("Ice Cream x" + str(menu3_quantity))
            print("Ice Cream x" + str(menu3_quantity) + " added")
            continue
            
        elif var_order == "4":
            menu4_quantity = float(input("Quantity: "))
                
            orders.append(menu4_quantity * 5)
            items.append("Iced Tea x" + str(menu4_quantity))
            print("Iced Tea x" + str(menu4_quantity) + " added")
            continue
            
        elif var_order == "5":
            order_table = [items, orders]
                    
            print(tabulate(order_table))
            var_total = np.sum(orders)
            print("Total: " + str(var_total))
            while True:
                var_payment = float(input("Enter Customer Payment: "))
                var_paymentcondition = bool(var_payment >= var_total)
                if var_paymentcondition == False:
                    print("Insufficient Payment")
                    continue
                else:
                    break
            var_change = var_payment - var_total
            print("Customer Payment: " + str(var_payment))
            print("Change: " + str(var_change))
            while True:
                var_confirm = input("Proceed to another transaction? Press Y: ")
                if var_confirm == "Y" or "y":
                    orders.clear()
                    items.clear()
                    break
                else:
                    print("Error")
                    continue
            continue

        elif var_order == "6":
            exit("Quitting POS System")
            
        else:
            print("Invalid Option, Please Try again")
            continue
order()