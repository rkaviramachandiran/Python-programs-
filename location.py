order=int(input("Enter order amount:"))
delivery=(input("Enter delivery location(local/national/international):"))
if delivery=="local" and order>=1000:
    local=0+order
    print("Shipping cost:0")
    print("Final amount:",local)
elif delivery=="local":
     local=50+order
     print("Shipping cost:50")
     print("Final amount:",local)
     
elif delivery=="national" and order>=1000:
    nation=0+order
    print("Shipping cost:0")
    print("Final amount",nation)
elif delivery=="national":
    nation=50+order
    print("Shipping cost:50")
    print("Final amount:",nation)
    
elif delivery=="international":
    internation=500+order
    print("Shipping amount:500")
    print("Final amount:",internation)
    
else:
    print("Invalid location.")
