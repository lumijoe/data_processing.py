#初めてのファイルです
money=10000
count=input("How many buy? Please enter here:")
snack=400

if money>int(count)*snack:
    print("You can buy it.")

elif money>=snack*int(count):
    print("You can buy but your money will no apear foever.")

else:
    print("Sorry your place no here.")