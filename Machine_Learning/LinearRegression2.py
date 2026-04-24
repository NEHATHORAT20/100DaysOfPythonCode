import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():

    #Load the Data
    X = [1 , 2 , 3 , 4 , 5]
    Y = [3 , 4 , 2 , 4 , 5]

    print("Values of Independent Variables : X - " , X)
    print("Values of Dependent Variables : Y - " , Y)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("X_Mean is : " , mean_x)  # 3.0
    print("Y_Mean is : " , mean_y)  # 3.6

    n = len(X)  # 5

    # Y = mX + C

    # m = (Summation (X-X_mean) * (Y-Y_mean)) / ((Summation (X-X_mean) ** 2))

    numerator = 0
    denominator = 0

    for i in range(n):

        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator =  denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator

    print("Slope of line (m) : " , m)   # 0.4

    C = mean_y - (m * mean_x) 

    print("Y intercept of line (C) : " , C) # 2.4

def main():

    MarvellousPredictor()

if __name__ == "__main__":
    main()