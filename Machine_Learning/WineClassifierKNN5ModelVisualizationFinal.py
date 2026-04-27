import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score , confusion_matrix , classification_report
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):

    Border = "-"*50
    
    ##################################################################
    # Step 1 :- Load the Dataset 
    ##################################################################

    print(Border)
    print("Step 1 - Load the dataset from CSV File")
    print(Border)

    df = pd.read_csv(DataPath)

    print("Some entries from dataset")
    print(df.head())
    print(Border)

    ##################################################################
    # Step 2 :- Clean the Dataset by removing empty rows
    ##################################################################

    print(Border)
    print("Step 2 - Clean the Dataset by removing empty rows")
    print(Border)

    df.dropna(inplace = True)
    print("Total records : " , df.shape[0])
    print("Total columns : " , df.shape[1])
    print(Border)

    ##################################################################
    # Step 3 :- Separate independent and dependent varialbles
    ##################################################################

    print(Border)
    print("Step 3 - Separate independent and dependent varialbles")
    print(Border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X : " , X.shape)
    print("Shape of Y : " , Y.shape)

    print(Border)
    print("Input Columns : " , X.columns.tolist())
    print("Output Columns : Class")
    print(Border)

    ##################################################################
    # Step 4 :- Split the dataset for training and testing
    ##################################################################

    print(Border)
    print("Step 4 - Split the dataset for training and testing")
    print(Border)

    X_train , X_test , Y_train , Y_test = train_test_split(X , Y ,test_size=0.2 , random_state=42 , stratify=Y)

    print(Border)
    print("Information on training and testing data")
    print("X_train shape : " , X_train.shape)
    print("X_test shape : " , X_test.shape)
    print("Y_train shape : " , Y_train.shape)
    print("Y_test shape : " , Y_test.shape)
    print(Border)

    ##################################################################
    # Step 5 :- Feature Scaling
    ##################################################################

    print(Border)
    print("Step 5 - Feature Scaling")
    print(Border)

    Scaler = StandardScaler()
    #Independent variable scaling
    X_train_scaled = Scaler.fit_transform(X_train)
    X_test_scaled = Scaler.fit_transform(X_test)

    print("Feature Scaling is done")

    ##################################################################
    # Step 6 :- Explore multiple values of K
    # Hyperparameter tuning (K)
    ##################################################################

    print(Border)
    print("Step 6 - Explore multiple values of K")
    print(Border)

    accuracy_scores = []
    K_Values = range(1,21)

    for k in K_Values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled , Y_train)
        Y_pred = model.predict(X_test_scaled)
        Accuracy = accuracy_score(Y_test , Y_pred)
        accuracy_scores.append(Accuracy)

    print(Border)
    print("Accuracy report of all k values from 1 to 20")
    for value in accuracy_scores:
        print(value)
    print(Border)

    ##################################################################
    # Step 7 :- Plot graph of K vs Accuracy
    ##################################################################

    print(Border)
    print("Step 7 - Plot graph of K vs Accuracy")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.plot(K_Values , accuracy_scores , marker = 'o')
    plt.title("K Values vs Accuracy")
    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.grid(True)
    plt.xticks(list(K_Values))
    plt.show()

    ##################################################################
    # Step 8 :- Find best value of K
    ##################################################################

    print(Border)
    print("Step 8 - Find best value of K")
    print(Border)

    best_k = list(K_Values)[accuracy_scores.index(max(accuracy_scores))]

    print("Best value of k is :" , best_k)

    ##################################################################
    # Step 9 :- Build Final Model using best value of k
    ##################################################################

    print(Border)
    print("Step 9 - Build Final Model using best value of k")
    print(Border)

    Final_Model = KNeighborsClassifier(n_neighbors=best_k)
    Final_Model.fit(X_train_scaled , Y_train)
    Y_pred = Final_Model.predict(X_test_scaled)

    ##################################################################
    # Step 10 :- Calculate final Accuracy
    ##################################################################

    print(Border)
    print("Step 10 - Calculate final Accuracy")
    print(Border)

    accuracy = accuracy_score(Y_test , Y_pred)
    print("Accuracy of model is : " , accuracy * 100)

    ##################################################################
    # Step 11 :- Display Confusion Matrix
    ##################################################################

    print(Border)
    print("Step 11 - Display Confusion Matrix")
    print(Border)

    cm = confusion_matrix(Y_test , Y_pred)
    print(cm)

    ##################################################################
    # Step 12 :- Dispaly Classification Report
    ##################################################################

    print(Border)
    print("Step 12 - Dispaly Classification Report")
    print(Border)

    print(classification_report(Y_test , Y_pred))

def main():

    Border = "-"*50

    print(Border)
    print("Wine Classifier using KNN")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()