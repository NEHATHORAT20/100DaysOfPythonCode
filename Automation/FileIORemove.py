import os

def main():
    FileName = input("Enter the Name of File : ")

    if(os.path.exists(FileName)):

        os.remove(FileName)
        print("File gets Deleted")

    else:
        print("There is no such file")
        
if __name__ == "__main__":
    main()