import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix

#------------------------------------------------------------
#   Function name : PreserveModel
#   Description :   It is used to preserve model on secondary
#   Parameters :    model, filename
#   Return :        None
#   Date :          14/03/2026
#   Author :        Piyush Manohar Khairnar
#------------------------------------------------------------

def PreserveModel(model,filename):
    joblib.dump(model,filename)

    print("Model preserved successfully with name : " , filename)

#------------------------------------------------------------
# Function Name : TrainTitanicModel
# Description : It does split X , Y , training data  , testing data
# Parameters : df
# Return : None
# Date : 14/03/2026
# Author : Neha Thorat
#------------------------------------------------------------

def TrainTitanicModel(df):
    #split features and labels
    X = df.drop("Survived" , axis = 1)
    Y = df["Survived"]

    print("\n Features :")
    print(X.head())

    print("\n Labels :")
    print(Y.head())

    print("Shape of X : " , X.shape)
    print("Shape of Y : " , Y.shape)

    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    print("Xtrain Shape : " , X_train.shape)
    print("Xtest Shape : " , X_test.shape)
    print("Ytrain Shape : " , Y_train.shape)
    print("Ytest Shape : " , Y_test.shape)

    model = LogisticRegression(max_iter = 1000)
    model.fit(X_train , Y_train)

    print("Model trained succesfully")

    print("\n Intercept of model : ")
    print(model.intercept_)

    print("\n Coefficient of model")
    for feature , coefficient in zip (X.columns , model.coef_[0]):
        print(feature ,":", coefficient)

    PreserveModel(model,"marvelloustitanic.pkl")

#------------------------------------------------------------
# Function Name : DisplayInfo
# Description : It displays the formatted title
# Parameters : title (str)
# Return : None
# Date : 14/03/2026
# Author : Neha Thorat
#------------------------------------------------------------

def DisplayInfo(title):
    print("\n" + "-"*70)
    print(title)
    print("-"*70)

#------------------------------------------------------------
# Function Name : ShowData
# Description : It shows basic information about dataset
# Parameters : Dataset (df) 
#              df -> P  andas dataframe object
#              message    
#              message -> Heading text to display
# Return : None
# Date : 14/03/2026
# Author : Neha Thorat
#------------------------------------------------------------

def ShowData(df , message):

    DisplayInfo(message)

    print("\nFirst 5 rows of dataset")
    print(df.head())

    print("\nShape of dataset")
    print(df.shape)

    print("\nColumn names")
    print(df.columns.tolist())

    print("\nMissing values in each column")
    print(df.isnull().sum())

#------------------------------------------------------------
# Function Name : CleanTitanicData
# Description : It does preprocessing
#               It removes unnecessary columns
#               It handles misssing values
#               It converts text data to numeric format
#               IT does encoding to categorical columns
# Parameters : df -> Pandas Dataframe
# Return : df -> Clean Pandas Dataframe
# Date : 14/03/2026
# Author : Neha Thorat
#------------------------------------------------------------

def CleanTitanicData(df):

    DisplayInfo("Step 2 : Original Data")
    print(df.head())

    #Remove unnecessary columns
    drop_columns = ["Passengerid" , "zero"]
    existing_columns = [col for col in drop_columns if col in df.columns]

    print("\n Columns to be dropped : ")
    print(existing_columns)

    #Drop the unwanted columns
    df = df.drop(columns = existing_columns)
    DisplayInfo("Step 2 : Data after column removal")
    print(df.head())

    #Handle age column
    if "Age" in df.columns:
        print("Age column before filling missing values")
        print(df["Age"].head(10))

        # coerce -> Inavlid value gets converted as NaN
        df["Age"] = pd.to_numeric(df["Age"] , errors = "coerce")
        age_median = df["Age"].median()

        # Replace missing values with median
        df["Age"] = df["Age"].fillna(age_median)

        print("\n Age Column after prepocessing : ")
        print(df["Age"].head(10))

    # Handle fare column 
    if "Fare" in df.columns:
        print("\n Fare column before preprocessing")
        print(df["Fare"].head(10))

        df["Fare"] = pd.to_numeric(df["Fare"] , errors = "coerce")
        fare_median = df["Fare"].median()

        print("Median of Fare column is : " , fare_median)

        # Replace missing values with median
        df["Fare"] = df["Fare"].fillna(fare_median)

        print("\n Fare Column after prepocessing : ")
        print(df["Fare"].head(10))

    #Handle Embarked Column
    if "Embarked" in df.columns:
        print("\n Embarked column before preprocessing")
        print(df["Embarked"].head(10))

        # Convert the data into string
        df["Embarked"] = df["Embarked"].astype(str).str.strip()

        #Remove missing values
        df["Embarked"] = df["Embarked"].replace(['nan','None',''],np.nan)

        #Get most frequent value
        embarked_mode = df["Embarked"].mode()[0]
        print("\n Mode of embarked column : " , embarked_mode)

        df["Embarked"] = df["Embarked"].fillna(embarked_mode)

        print("\n Embarked Column after prepocessing : ")
        print(df["Embarked"].head(10))

    # Handle sex column 
    if "Sex" in df.columns:
        print("\n Sex column before preprocessing")
        print(df["Sex"].head(10))

        df["Sex"] = pd.to_numeric(df["Sex"] , errors = "coerce")

        print("\n Sex Column after prepocessing : ")
        print(df["Sex"].head(10))

    DisplayInfo("Data after preprocessing : ")
    print(df.head())

    print("\n Missing values after preprocessing")
    print(df.isnull().sum())

    #Encode Embarked Column 
    df = pd.get_dummies(df,columns = ["Embarked"])
    print("\n Data after encoding")

    print(df.head())

    print("Shape pf dataset : " , df.shape)

    #Convert boolean column into integer
    for col in df.columns:
        if df[col].dtype == bool:
            df[col] = df[col].astype(int)

    print("\n Data after encoding")

    print(df.head())

    return df

#------------------------------------------------------------
# Function Name : MarvellousTitanicLogistic
# Description : This is main pipeline controller
#               It loads the Dataset and shows the raw data
#               It preprocess the dataset and train the model
# Parameters : Data path of Dataset File
# Return : None
# Date : 14/03/2026
# Author : Neha Thorat
#------------------------------------------------------------

def MarvellousTitanicLogistic(DataPath):
    DisplayInfo("Step 1 : Loading the Dataset")
    df = pd.read_csv(DataPath)

    ShowData(df, "Initial Dataset")
    df = CleanTitanicData(df)

    TrainTitanicModel(df)

#------------------------------------------------------------
# Function Name : main
# Description : Starting point of the application
# Parameters : None
# Return : None
# Date : 14/03/2026
# Author : Neha Thorat
#------------------------------------------------------------

def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()