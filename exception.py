import sys 
try :
    x = int(input("x"))
    y = int(input("y"))
except ValueError :
    print("oops innvalid input ")
    sys.exit(1)

try :
    c = x/y
except ZeroDivisionError :
    print("opps can't divide by zero ")
    sys.exit(1)



print(f"{x}/{y} = {c}")