#Mall_Customers

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    #------------------------------------------------------------------
    # step 1 : Load the Dataset
    #------------------------------------------------------------------

    print("Step : 1 Load the dataset")
    df = pd.read_csv("Mall_Customers.csv")

    print("First few records")
    print(df.head())

    print("Shape of dataset : ")
    print(df.shape)

    print("Missing values : ")
    print(df.isnull().sum())

    #------------------------------------------------------------------
    # step 2 : LSelect features (Independant)
    #------------------------------------------------------------------

    print("step 2 : LSelect features (Independant)")

    X = df[["AnnualIncome","SpendingScore"]]

    print("Selected Features : ")
    print(X.head())

    print("Shape of Selected features : ")
    print(X.shape)




    

if __name__ == "__main__":
    main()