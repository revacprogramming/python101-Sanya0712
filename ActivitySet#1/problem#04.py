# Conditional Execution

hrs=float(input("Enter Hours:\n"))
rate=float(input("enter the rate per hour:\n"))
if hrs<=40:
    print("gross pay = ",(hrs*rate))
else:
    print("gross pay = ",(40*rate)+((hrs-40)*1.5*rate))