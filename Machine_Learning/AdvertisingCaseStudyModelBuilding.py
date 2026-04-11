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

    #---------------------------------------------------------------------------------
    # Step 6 : Split Dataset into independant and dependant variables
    #---------------------------------------------------------------------------------

    print(Border)
    print("Step 6 : Split Dataset into independant and dependant variables")
    print(Border)

    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    print("Shape of Independant variable : ",X.shape)
    print("Shape of Dependant variable : ",Y.shape)

    #---------------------------------------------------------------------------------
    # Step 7 : Split Dataset for training and testing
    #---------------------------------------------------------------------------------

    print(Border)
    print("Step 7 : Split Dataset for training and testing")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("XTrain shape :",X_train.shape)
    print("X_test shape :",Y_test.shape)
    print("Y_train shape :",Y_train.shape)
    print("Xtest shape :",X_test.shape)

    #---------------------------------------------------------------------------------
    # Step 8 : Create and train the model
    #---------------------------------------------------------------------------------

    print(Border)
    print("Step 8 : Create and train the model")
    print(Border)

    model = LinearRegression()

    model.fit(X_train,Y_train)

    #---------------------------------------------------------------------------------
    # Step 9 : Test the model
    #---------------------------------------------------------------------------------

    print(Border)
    print("Step 9 : Test the model")
    print(Border)

    Y_pred= model.predict(X_test)

    #---------------------------------------------------------------------------------
    # Step 10 : Evaluate the model
    #---------------------------------------------------------------------------------

    print(Border)
    print("Step 10 : Evaluate the model")
    print(Border)

    MSE = mean_squared_error(Y_test,Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test,Y_pred)

    print("Mean Squared Error :",MSE)
    print("Root Squared Error :",RMSE)
    print("R Squar Value :",R2)

    #---------------------------------------------------------------------------------
    # Step 11 : Calculate Model coefficient
    #---------------------------------------------------------------------------------

    print(Border)
    print("Step 11 : Calculate Model coefficient")
    print(Border)

    for column, value in zip(X.columns,model.coef_):
        print(f"{column} : {value}")

    print("Intercept : ",model.intercept_)

    #---------------------------------------------------------------------------------
    # Step 12 : Compare the actual and predicted values
    #---------------------------------------------------------------------------------

    print(Border)
    print("Step 12 : Compare the actual and predicted values")
    print(Border)

    Result = pd.DataFrame({
                            'Actual sale' : Y_test.values,
                           'Predicted sale' : Y_pred
                           })

    print(Result.head())






def main():
    MarvellousAdvertice("Advertising.csv")





if __name__ =="__main__":
    main()
