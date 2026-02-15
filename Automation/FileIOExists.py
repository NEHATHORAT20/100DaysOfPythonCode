import os

def main():
    FileName = input("Enter the Name of File : ")

    Ret = os.path.exists(FileName)

    if Ret == True:
        fobj = open(FileName, "r")
        print("File gets suceesfully opened")

    else:
        print("There is no such File")
        
if __name__ == "__main__":
    main()