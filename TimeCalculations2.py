import time 

def Factorial(No):
    Fact = 1

    for i in range(1 , No + 1):
        Fact = Fact * i

    return Fact

def main():
    Value = int(input("Enter Number : "))

    start_time = time.time()
    print(start_time)

    Ret = Factorial(Value)

    end_time = time.time()
    print(end_time)

    print("Factorial is " , Ret)

    print("Total Execution time is " , end_time - start_time)
    
if __name__ == "__main__":
    main()