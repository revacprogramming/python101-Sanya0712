# Functions

def computepay(hrs,rate):
    if hrs<=40:
        py=(hrs*rate)
    else:
        py=(40*rate)+((hrs-40)*1.5*rate)
    return py
        
#main
h=float(input("enter hours:\n"))
r=float(input("enter rate:\n"))
pay=computepay(h,r)
print("Pay:",pay)


