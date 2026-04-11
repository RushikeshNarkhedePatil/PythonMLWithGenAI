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

    #------------------------------------------------------------------
    # step 3 : Scale the data
    #------------------------------------------------------------------

    print("step 3 : Scale the data")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("Data after scalling : ")
    print(X_scaled[:5])

    #------------------------------------------------------------------
    # step 4 : Used Elbow method
    #------------------------------------------------------------------

    WCSS = []

    for i in range(1,11):
        model = KMeans(n_clusters=i,random_state=42,n_init=10)
        model.fit(X_scaled)
        WCSS.append(model.inertia_)

    plt.figure(figsize=(8,5))
    plt.plot(range(1,11),WCSS, marker ='o')
    plt.xlabel("Number of clusters")
    plt.ylabel("WCSS")
    plt.title("Elbow method")
    plt.grid(True)
    plt.show()

    #------------------------------------------------------------------
    # step 5 : Train the model
    #------------------------------------------------------------------

    model = KMeans(n_clusters=4,random_state=42,n_init=10)
    Cluesters = model.fit_predict(X_scaled)

    df["Cluesters"] = Cluesters

    print("Dataset with cluster")
    print(df.head(30))





    

if __name__ == "__main__":
    main()