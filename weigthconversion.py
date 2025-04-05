#we are going to convert lbs into kgs or kgs into lbs
a = input("ENTER THE UNIT OF WEIGHT YOU ARE ENTERING(K/L) 🏋️:")
b = float(input("enter your weight 😒:"))
if a == "k":
    b = b*2.205
    print(f"your weight is : {b}  lbs")
elif a == "l" :
    b = b/2.205
    print(f"your weight is :{b} kgs")
else:
    print("WHAT YOU ARE WRITING DUMBASS 🤬")