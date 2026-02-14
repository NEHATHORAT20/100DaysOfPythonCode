import sys

def main():
    Border = "-"*40
    print(Border)

    print("----------Marvellous Automation---------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform____")
            print("This is the Automation Script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
                print("Use the gives script as")
                print("ScriptName.py Argument1 Argument2")
                print("Argument1 : ______________")
                print("Argument2 : ______________")

        else:
            print("Use the gives flags as")
            print("--u : Used to display the usage")
            print("--h : Used to display the help")

    else:
        print("Invalid  number of command line arguments")
        print("Use the gives flags as")
        print("--u : Used to display the usage")
        print("--h : Used to display the help")

    print(Border)
    print("--------Thank for using our script------")
    print("----------Marvellous Infosystems--------")
    print(Border)

if __name__ == "__main__":
    main()