
from sklearn.datasets import load_iris

# Rough 1
# Smooth 0
# Cricket 2
# Tennis 1
def main():
    print("Iris Classification case study")

    Dataset = load_iris()
    # Meta data of dataset
    print("Independent variables are :")
    print(Dataset.feature_names)

    print("Dependant Variables are : ")
    print(Dataset.target_names)


if __name__ =="__main__":
    main()

