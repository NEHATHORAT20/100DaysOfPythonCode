def EmployeeInfo(Name, Age, Salary, City):
    print("Name : ", Name)
    print("Age : ", Age)
    print("Salary : ", Salary)
    print("City : ", City)

def main():
    #Positional
    #EmployeeInfo("Neha", 21, 200000, "Tokyo")       #Correct
    #EmployeeInfo(21, "Neha", "Tokyo", 200000)       #Wrong

    #Keyword Arguments
    EmployeeInfo(Age = 21, Name = "Neha", City = "Tokyo", Salary = 200000)  #Correct

if __name__ == "__main__":
    main()