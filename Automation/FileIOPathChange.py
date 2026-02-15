import os

def main():
    FileName = input("Enter the Name of File : ")

    if(os.path.exists(FileName)):

        Ret = os.path.isabs(FileName)

        if Ret == True:
            print("It is Absolute path")

        else:
            print("It is Relative Path")
            NewPath = os.path.abspath(FileName)
            print("Updated Path : " , NewPath)

    else:
        print("There is no such file")
        
if __name__ == "__main__":
    main()