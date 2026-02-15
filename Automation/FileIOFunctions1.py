import os

def main():
    FileName = input("Enter the Name of File : ")

    if(os.path.exists(FileName)):

        fobj = open(FileName, "r")
        
        print(fobj.name)
        print(fobj.mode)
        print(fobj.closed)

    else:
        print("There is no such file")
        
if __name__ == "__main__":
    main()