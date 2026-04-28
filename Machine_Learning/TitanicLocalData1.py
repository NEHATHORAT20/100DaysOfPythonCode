import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score , confusion_matrix

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