#python3 CommandLine5.py 11 10

import sys

def main():
    #if(len(sys.argv) < 3 or len(sys.argv) > 3):        #logical
    if((len(sys.argv) < 3) | (len(sys.argv) > 3)):      #bitwise
        print("Invalid Number of Arguments")
    else:
        print(int(sys.argv[1]) + int(sys.argv[2]))
    
if __name__ == "__main__":
    main()

    