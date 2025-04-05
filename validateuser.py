#we are doing something with programme
username = input("PLEASE ! ENTER YOUR NAME SIR 🧔‍ :️")
a = username.isdigit()
#b = username.isspace()
if len(username) > 12 :
    print(" Sorry sir name is too long :")
elif not username.find(" ") == -1:
    print(" sorry sir ! you cant use space within your name :")
elif a:
        print(" sorry sir! digits cant be used in your name :")
else:
 print(f"welcome mr.{username} , you are welcome to your territory .")