import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousAdvertice(DataPath):
    Border = "-"*40
    #---------------------------------------------------------------------------------
    # Step 1 : Load Data Set
    #---------------------------------------------------------------------------------
    print(Border)
    print("Step 1 : Load Data Set")
    print(Border)
    df = pd.read_csv(DataPath)

    print("Fev records from the dataset. :")
    print(df.head())

    #---------------------------------------------------------------------------------
    # Step 2 : Remove Unwanted Column
    #---------------------------------------------------------------------------------
    print(Border)
    print("Step 2 : Remove Unwanted Column")
    print(Border)

    print("Shape of dataset before removeval :",df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)

    print("Shape of dataset after removeval :",df.shape)

    print(Border)
    print("Clean Data Set : ")
    print(Border)

    print(df.head())

    #---------------------------------------------------------------------------------
    # Step 3 : Check Missing Values
    #---------------------------------------------------------------------------------

    print(Border)
    print("Step 3 : Check Missing Values")
    print(Border)

    print("Missing Values Count :\n",df.isnull().sum())

    #---------------------------------------------------------------------------------
    # Step 4 : Display Statistical summery
    #---------------------------------------------------------------------------------

    print(Border)
    print("Step 4 : Display Statistical summery")
    print(Border)

    print(df.describe())

    #---------------------------------------------------------------------------------
    # Step 5 : Correlation Between Column
    #---------------------------------------------------------------------------------

    print(Border)
    print("Step 5 : Correlation Between Column")
    print(Border)

    print("Correlation Matrix :")
    print(df.corr())



def main():
    MarvellousAdvertice("Advertising.csv")





if __name__ =="__main__":
    main()
