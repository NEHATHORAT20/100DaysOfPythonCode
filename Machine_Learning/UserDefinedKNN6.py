#  [A,B,C,D]
# X[1,2,3,5]
# Y[2,3,1,6]
#  [R,R,B,B]

#Predict(3,3) -> ?

import numpy as np
import math

def EuclideanDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)

    return Ans

def MarvellousKNeighborsClassifier():

    Border = "-"*50

    Data = [
        
                {'point' : 'A' , 'X' : 1 , 'Y' : 2 , 'label' : 'Red'},
                {'point' : 'B' , 'X' : 2 , 'Y' : 3 , 'label' : 'Red'},
                {'point' : 'C' , 'X' : 3 , 'Y' : 1 , 'label' : 'Blue'},
                {'point' : 'D' , 'X' : 5 , 'Y' : 6 , 'label' : 'Blue'}
           ]
    print(Border)
    print("Marvellous User Defined KNN")
    print(Border)

    print(Border)
    print("Training Dataset")
    print(Border)

    for i in Data:
        print(i)

    print(Border)

    new_point = {'X' : 3 , 'Y' : 3}

    #Calculate all distances
    for d in Data:
        d['distance'] = EuclideanDistance(d , new_point)

    print(Border)
    print("Calculated distances are : ")
    print(Border)

    for d in Data:
        print(d)

    sorted_data = sorted(Data , key = lambda item : item['distance'])

    print(Border)
    print("Sorted Data is : ")
    print(Border)

    for d in sorted_data:
        print(d)

    k = 3

    nearest = sorted_data[:k]

    print(Border)
    print("Nearest 3 elements are : ")
    print(Border)

    for d in nearest:
        print(d)

    #Voting
    Votes = {}

    for neighbor in nearest:
        label = neighbor['label']
        Votes[label] = Votes.get(label,0) + 1

    print(Border)
    print("Voting Result is : ")
    print(Border)

    for d in Votes:
        print("Name : " , d , "Number of Votes : " , Votes[d]) 

    print(Border)

    predicted_class = max(Votes , key = Votes.get)

    print("Predicted Class of (3,3) : " , predicted_class)

def main():

    MarvellousKNeighborsClassifier()

if __name__ == "__main__":
    main()