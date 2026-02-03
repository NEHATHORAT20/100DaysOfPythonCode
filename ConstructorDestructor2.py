import gc 

class Demo:
    def __init__(self):
        print("Inside Constuctor")

    def __del__(self):
        print("Inside Destructor")

obj1 = Demo()
obj2 = Demo()

# Allocate
del obj1
del obj2

# Use

# Deallocate
gc.collect()

print("End of Applicatoion")