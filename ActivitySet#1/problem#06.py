# Loops & Iterators

minimum=None
maximum=None
while True:
    n=input("enter a number:\n")
    if(n=="done"):
        break
    try:
        num=int(n)
    except:
        print("invalide input\n")
    if minimum==None:
        minimum=num
    elif minimum>num:
        minimum=num
    if maximum==None:
        maximum=num
    elif maximum<num:
        maximum=num
        
print("minimum is:",minimum)
print("maximum is:",maximum)