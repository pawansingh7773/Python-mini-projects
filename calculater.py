# we are to make basic calculater using python
a = int(input("Enter your first  number 😊 :"))
b = int(input("Enter your second number 😊 :"))
print("Your options are:")
print(" 1.ADDITION"  
                "2.SUBSTRACTION"
                             "3.MULTIPLICATION"
                                           "4.DIVIDE")
select = int(input("Enter your choice :"))
if select == 1 :

    c = a+b
    print(f"addition is ➕ : {c}")
elif select == 2 :
    c = a-b
    print(f"substraction is ➖ :{c}")
elif select == 3:
    c = a*b
    print(f" multiplication is ✖️ : {c}")
elif select == 4 :
    c = a/b
    print(f"division is  ➗: {c}")
else :
    print("you are writing wrong dumbass 🤬🤬")

