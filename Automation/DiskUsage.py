import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):

    Border = "-"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to create folder")
            return
    else:
        os.mkdir(FolderName)
        print("Directory for log Files get created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    print(timestamp)
    FileName = os.path.join(FolderName , "Marvellous_%s.log" %timestamp)
    print(FileName)

    fobj = open(FileName , "w")

    fobj.write(Border+"\n")
    fobj.write("Marvellous Platform Surveillance System\n")
    fobj.write("Log created at : " +time.ctime()+"\n")
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+"\n")
    fobj.write("------------------End of Log file-----------------\n")
    fobj.write(Border+"\n")

    print("CPU usage : " , psutil.cpu_percent())

    mem = psutil.virtual_memory()
    print("Ram usage : " , mem.percent)

    for part in psutil.disk_partitions():
        usage = psutil.disk_usage(part.mountpoint)
        print(f"{part.mountpoint} used {usage.percent}%%")

def main():
    Border = "-"*50

    print(Border)
    print("-----Marvellous Platform Surveillance System------")
    print(Border)

    if (len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to :")
            print("1: Create automatic logs")
            print("2: Executes periodically")
            print("3: Sends mail with log")
            print("4: Store information about processes")
            print("5: Store information about CPU")
            print("6: Store information about RAM usage")
            print("7: Store information about secondary storage")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval DirectoryName")
            print("Time Interval: The time in minutes for periodic scheduling")
            print("Directory Name: Name of Directory to create auto logs")

        else:
            print("Unable to proceed as there is no such directory")
            print("Please use --u or --h to get more details")

    #python Demo.py 5 MarvellousProcess
    elif(len(sys.argv) == 3):
        print("Inside Projects Logic")
        print("Time Interval : " , sys.argv[1])
        print("Directory Name : " , sys.argv[2])
        
        #Apply the scheduler
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        print("Platform Surveillance System started successfully")
        print("Directory created with name : " , sys.argv[2])
        print("Time interval in minutes : " , sys.argv[1])
        print("Press Ctrl + C to stop execution")

        #Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such directory")
        print("Please use --u or --h to get more details")

    print(Border)
    print("----------Thank you for using our script----------")
    print(Border)

if __name__ == "__main__":
    main()