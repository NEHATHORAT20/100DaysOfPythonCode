def EmployeeInfo(Name = "Chimkandi", Age = 21, Salary = 500, City = "Delhi"):
    print("Name : ", Name)
    print("Age : ", Age)
    print("Salary : ", Salary)
    print("City : ", City)

def main():
    #EmployeeInfo(Age = 21, Name = "Neha", City = "Tokyo", Salary = 200000)  #Correct
    EmployeeInfo()

if __name__ == "__main__":
    main()