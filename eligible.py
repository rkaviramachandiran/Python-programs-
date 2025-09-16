mark=int(input("Enter marks percentage:"))
income=int(input("Enter family income:"))
if mark>=75 and income<=200000:
    print("Full scholarship")
elif mark>=70 and income<=500000:
    print("Half scholarship")
else:
    print("No scholarship")