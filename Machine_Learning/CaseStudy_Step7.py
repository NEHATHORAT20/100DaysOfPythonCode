import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import(
    accuracy_score,
    confusion_matrix, 
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*50

###############################################################
# Step 1 : Load the Dataset
###############################################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DatasetPath = "iris.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded successfully")
print("Initial entries from dataset")
print(df.head())

###############################################################
# Step 2 : Data Analysis (EDA - Exploratory Data Analysis)
###############################################################

print(Border)
print("Step 2 : Data Analysis EDA")
print(Border)

print("Shape of Dataset : " , df.shape)
print("Column Names" , list(df.columns))
print("Missing Values {Per Column}")
print(df.isnull().sum())

print("Class Distribution (Species Count)")
print(df["Species"].value_counts())

print("Statistical Report of Dataset")
print(df.describe())

###############################################################
# Step 3 : Decide Independent & Dependent Variables
###############################################################

print(Border)
print("Step 3 : Decide Independent & Dependent Variables")
print(Border)

# X : Independent Variables / Features
# Y : Dependent Variables / Labels

Feature_Cols = [
    "Sepal Length(cm)",
    "Sepal Width(cm)",
    "Petal Length(cm)",
    "Petal Width(cm)"
]
X = df[Feature_Cols]
Y = df["Species"]

print("X shape : " , X.shape)
print("Y shape : " , Y.shape)

###############################################################
# Step 4 : Visualization of Dataset
###############################################################

print(Border)
print("Step 4 : Visualization of Dataset")
print(Border)

# Scatter Plot 
plt.figure(figsize = (7,5))

for sp in df["Species"].unique():
    temp = df[df["Species"] == sp]
    plt.scatter(temp["Petal Length(cm)"] , temp["Petal Width(cm)"] , label = sp)

plt.title("Iris : Petal Length Vs Petal Width")
plt.xlabel("Petal Length(cm)")
plt.ylabel("Petal Width(cm)")

plt.legend()
plt.grid(True)
plt.show()

###############################################################
# Step 5 : Split Dataset for Training & Testing
###############################################################

print(Border)
print("Step 5 : Split Dataset for Training & Testing")
print(Border)

# Total Dataset : 150,5
# X : 150,4
# Y : 150,1
# Test Size = 20%
# Train Size = 80%

X_train , X_test , Y_train , Y_test = train_test_split(
    X, 
    Y,
    test_size = 0.2,
    random_state = 42
)

print("Data Splitting Activity Done")

print("X - Independent : " , X.shape)       #(150,4)
print("Y - Dependent : " , Y.shape)         #(150,)

print("X_train : " , X_train.shape)         #(120,4)
print("X_test : " , X_test.shape)           #(30,4)

print("Y_train : " , Y_train.shape)         #(120,)
print("Y_test : " , Y_test.shape)           #(30,)

###############################################################
# Step 6 : Build the Model
###############################################################

print(Border)
print("Step 6 : Build the Model")
print(Border)

print("We are going to use DecisionTreeClassifier")

model = DecisionTreeClassifier(
    criterion = "gini",
    max_depth = 3,
    random_state = 42
)

print("Model successfully created : " , model)

###############################################################
# Step 7 : Train the Model
###############################################################

print(Border)
print("Step 7 : Train the Model")
print(Border)

model.fit(X_train ,Y_train)

print("Model training completed")