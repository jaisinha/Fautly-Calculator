choice=input("Enter the operator")
a=int(input("First No."))
b=int(input("Second No."))
if(a==90 and b==9 and choice=="+"):
    print("The sum is 90 ")
elif(a==8 and b==90 and choice=="/"):
    print("The division is 90  ")
elif(choice=="+"):
    print("The answer is",a+b)
elif(choice=="-"):
    print("The answer is",a-b)
elif(choice=="*"):
    print("The answer is",a*b)
elif(choice=="/"):
    print("The answer is",a/b)
else:
    print("out of range")
