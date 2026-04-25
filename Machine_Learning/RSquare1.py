from sklearn.metrics import r2_score

def main():

    Y_Actual = [3,4,2,4,5]                          # Y
    Y_Predicted = [2.8 , 3.2 , 3.6 , 4.0 , 4.4]     # Yp

    r2 = r2_score(Y_Actual , Y_Predicted)

    print("Actual Values : " , Y_Actual)
    print("Predicted Values : " , Y_Predicted)
    print("R Square Value : " , r2)                 # 0.307

if __name__ == "__main__":
    main()