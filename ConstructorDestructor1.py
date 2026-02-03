import gc 

class Demo:
    def __init__(self):
        print("Inside Constuctor")

    def __del__(self):
        print("Inside Destructor")

obj = Demo()

# Allocate
del obj

# Use

# Deallocate
gc.collect()

print("End of Applicatoion")