menu = {"Samosa":10,
        "pepsi":30,
        "kachori":15,
        "juice":20,
        "chai":10,
        "chips":17,
        "popcorn":70}
cart = []
total = 0
print("------------- MENU ITEMS -------------")
for key in menu:
    print(f"{key}=₹{menu.get(key)}")
print("--------------------------------------")

while True:
    food = input("enter what you want to eat(enter q to quit ) :").lower()
    if food == "q":
        break
    elif menu.get(food):
        cart.append(food)
print()
print("============* YOUR BILL IS READY *==============")
for x in cart:
    print(x , end=" ")
    total = total + menu.get(x)
print(f"your total amount is  :₹{total}")
print(">>>>>>>>>>>* THANK YOU FOR VISIT *<<<<<<<<<<<<<<<")


