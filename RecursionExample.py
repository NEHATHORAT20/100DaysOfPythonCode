print(" ---- Marvellous Infosystems by Piyush Khairnar ----- ")

print("Demonstration of Scope of Recursion")

import sys

print ("Maximum number of recursive call are {} in python".format(sys.getrecursionlimit()))

# Changing recursion limit
sys.setrecursionlimit(1500)

print ("Maximum number of recursive call are {} in python".format(sys.getrecursionlimit()))

# Recursive function which goes into infinite recursive calls
def fun():
    print("Inside fun")
    fun()

i=1

# Recursive function which performs recursive calls 10 times
def gun():
    global i
    if(i <= 10):
        print(i)
        i+=1
        gun()

gun()

def fact(no):
    if(no == 0):
        return 1
    return no * fact(no-1)

value = 5
ret = fact(value)
print("Factorial of {} is {}".format(value,ret))