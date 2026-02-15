def main():
    try:
        open("Hello.txt","w")
        print("File gets successfully open")

    except FileNotFoundError:
        print("Unable to find file as there is no such file")

    finally:
        print("End of Application")

if __name__ == "__main__":
    main()