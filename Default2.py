def EmployeeInfo(Name, Age, Salary, City = "Pune"):
    print("Name : ", Name)
    print("Age : ", Age)
    print("Salary : ", Salary)
    print("City : ", City)

def main():
    EmployeeInfo("Neha", 21, 500000)
    EmployeeInfo("Neha", 21, 500000, "Tokyo")

if __name__ == "__main__":
    main()