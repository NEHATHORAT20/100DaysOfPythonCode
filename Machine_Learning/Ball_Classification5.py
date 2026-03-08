from sklearn import tree

#Rough : 1
#Smooth : 0

#Tennis : 1
#Cricket : 2

def main():
    print("Ball Classification Case Study")

    #Original Encoded Dataset
    #Independent Variables
    X = [[35 , 1] , [47 , 1] , [90 , 0] , [48 , 1] , [90 , 0] , [35 , 1] , [92 , 0] , [35 , 1] , [35 , 1] , [35 , 1] , [96 , 0] , [43 , 1] , [110 , 0] , [35 , 1] , [95 , 0]]

    #Dependent Variables
    Y = [1 , 1 , 2 , 1 , 2 , 1 , 2 , 1 , 1 , 1 , 2 , 1 , 2 , 1 , 2]

    #Independent Variables for training
    Xtrain = [[35 , 1] , [47 , 1] , [90 , 0] , [48 , 1] , [90 , 0] , [35 , 1] , [92 , 0] , [35 , 1] , [35 , 1] , [35 , 1] , [96 , 0] , [43 , 1] , [110 , 0]]
    
    #Independent Variables for testing
    Xtest = [[35 , 1] , [95 , 0]]

    #Dependent Variables for training
    Ytrain = [1 , 1 , 2 , 1 , 2 , 1 , 2 , 1 , 1 , 1 , 2 , 1 , 2]
    
    #Dependent Variables for testing
    Ytest = [1 , 2]

    modelobj = tree.DecisionTreeClassifier()

    trainedmodel = modelobj.fit(Xtrain , Ytrain)

    Result = trainedmodel.predict(Xtest)        

    print("Model Predicts the object as : " , Result)

if __name__ == "__main__":
    main()

#Dataset Size : 15