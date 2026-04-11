import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

def MarvellousClassifier(datapath):
    border = "-"*40
    #Step 1 : Load the Dataset from CSV File
    print(border)
    print("Step 1 : Load the Dataset from CSV File")
    print(border)

    df = pd.read_csv(datapath)

    print(border)
    print("Some enties from dataset")
    print(df.head())
    print(border)

    # Step 2 : Clean empty row
    print(border)
    print("Step 2 : Clean the dataset by removing empty rows")
    print(border)

    df.dropna(inplace = True)
    print("Total Record : ",df.shape[0])
    print("Total Colomns : ",df.shape[1])
    print(border)

    # Step 3 : Seprate independant and dependant variables
    print(border)
    print("Step 3 : Seprate independant and dependant variables")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)
    print(border)

    print("Input Columns : ",X.columns.tolist())
    print("Output Columns :  Class")



    



def main():
    border = "-"*40

    print(border)
    print("Wine Classifier using KNN")
    print(border)

    MarvellousClassifier("WinePredictor.csv")



if __name__ =="__main__":
    main()