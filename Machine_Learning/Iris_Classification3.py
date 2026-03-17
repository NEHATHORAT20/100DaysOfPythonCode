from sklearn.datasets import load_iris

def main():
    print("Iris Classification Case Study")

    Dataset = load_iris()

    #Metadata od dataset
    print("Independent variables are : ")
    print(Dataset.feature_names)
    print("Length Independent variables is : " , len(Dataset.feature_names))

    print("Dependent variables are : ")
    print(Dataset.target_names)
    print("Length Dependent variables is : " , len(Dataset.target_names))
    
if __name__ == "__main__":
    main()