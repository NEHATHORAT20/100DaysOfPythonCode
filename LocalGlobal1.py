No = 11         #Global

def Fun():
    No = 21     #Local
    print("Value of No from Fun is : " , No)        #21

print(f"Value of No is {No}")                       #11
Fun()