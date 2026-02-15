# seek(Kuthe, Kuthun)
# Kuthun - 0 / 1 / 2
# 0 - Starting
# 1 - Current Position 
# 2 - End of File 

def main():
    try:
        fobj = open("Hello.txt","r")
        print("File gets successfully open")

        print("Current offset is : " , fobj.tell())     #0

        fobj.seek(6, 1)
        
        print("Current offset is : " , fobj.tell())     #11


        Data = fobj.read(6)
        print("Current offset is : " , fobj.tell())     #17
        
        print("Data from file is : " , Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to find file as there is no such file")

    finally:
        print("End of Application")

if __name__ == "__main__":
    main()