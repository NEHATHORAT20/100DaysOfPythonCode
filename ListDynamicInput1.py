def main():
    Size = 0
    Value = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)      #Data[i] = Value

    print(Data)

    #Data.append(10)
    #Data.append(20)
    #Data.append(30)
    #Data.append(40)

    #print(Data)

if __name__ == "__main__":
    main()