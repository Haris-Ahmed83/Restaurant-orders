menu=  {
    "piza" :60,
    "coffee" : 80,
    "tea" : 90,
    "Burger" : 170,
    "Chiken" : 200,
}

print("WELLCOME TO OUR RESTRUNT")
print("piza :RS= 60\ncoffee: RS= 80\ntea: Rs= 90\nBurger:170\nchiken:200")
order_total= 0
item_1 = input("Enter your first order")
if item_1 in menu:
    order_total =+ menu[item_1]
    print(f"your item {item_1} has been added in menu")

else :
    print(f"order_item {item_1} is not avalible yet:")
another_order = input("Do you want to order something else? (yes/no)")
if another_order == "yes":
    item_2 = input("Enter a second order")
    if item_2 in menu:
        order_total += menu [item_2]
        print(f"your item {item_2} has been added in menu")
    else:
        print(f"order_item {item_2} is not avalible yet:")
print(f"The total amount of item to pay is {order_total}")





    
