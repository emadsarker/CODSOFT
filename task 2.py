a=int(input("enter first number:"))
b=int(input("enter second number:"))
print("choose an option :")
print("1.addition(+)")
print("2.subtraction(-)")
print("3.multiplication(*)")
print("4.division(/)")
choose=input("choose:")
if choose=="1":
    print(a+b)
elif choose=="2":
    print(a-b)
elif choose=="3":
    print(a*b)
elif choose=="4":
    print(a/b)
else:
    print("invalid choosing")