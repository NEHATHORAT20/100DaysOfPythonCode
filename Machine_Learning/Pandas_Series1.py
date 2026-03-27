import pandas as pd

def main():
    Data = [11, 21, 51, 101, 111]

    sobj = pd.Series(Data)

    print(Data)

    print(sobj)

if __name__ == "__main__":
    main()