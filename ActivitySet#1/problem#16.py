# Databases
# https://www.py4e.com/lessons/database
def score_func():
score=float(input("Enter Score: "))

if score>=0.9:
    print("	A")
elif score>=0.8:
    print("B")
elif score>=0.7:
    print("C")
elif score>=0.6:
    print("D")
elif score<0.6:
    print("F")
 
score_func()