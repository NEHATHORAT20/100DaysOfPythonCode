import sys
import os

def DirectoryScanner(DirName = "Marvellous"):
    Border = "_"*50

    fobj = open("Marvellous.log" , "w")

    fobj.write(Border+"\n")
    fobj.write("This is a Log file created by Marvellous Automation\n")
    fobj.write("This is the directory Cleaner Script\n")
    fobj.write(Border+"\n")

    Ret = False
    
    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    FileCount = 0
    EmptyFileCount = 0

    for FolderName, SubFolder, FileName in os.walk(DirName):
        
        for Fname in FileName:
            FileCount = FileCount + 1

            Fname = os.path.join(FolderName, Fname)

            if(os.path.getsize(Fname) == 0):        #empty file
                EmptyFileCount = EmptyFileCount + 1
                os.remove(Fname)    
    
    fobj.write("Total files scanned : " +str(FileCount)+"\n")
    fobj.write("Total empty files found : " +str(EmptyFileCount)+"\n")
    fobj.write(Border+"\n")
    fobj.close()

def main():
   Border = "_"*50

   print(Border)
   print("----------Marvellous Directory Automation---------")
   print(Border)

   if(len(sys.argv) != 2):
       print("Invalid Number of Arguments")
       print("Please psecify the name of directory")
       return 
   
   DirectoryScanner(sys.argv[1])

if __name__ == "__main__":
    main()