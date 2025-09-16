num1,num2,num3=map(int,input("Enter three number:").split())
if num1>=num2:
    if num1>=num3:
        print("Largest number:",num1)
    else :
        print("Largest number:",num3)
else:
    if num2>=num3:
        print("Largest number:",num2)
    else:
        print("Largest number:",num3)