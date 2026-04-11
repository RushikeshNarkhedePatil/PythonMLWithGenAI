import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

#----------------------------------------------------------------------------------------
# Function Name : LoadPreserveModel
# Description  : It is used to LoadPreserveModel
# Parameters : df
# Return : None
# Date : 14/3/26
# Author : Rushikesh Dilip Narkhede
#----------------------------------------------------------------------------------------

def LoadPreserveModel(filename):
    loaded_model = joblib.load(filename)

    print("Model sucessfully loaded")
    return loaded_model

#----------------------------------------------------------------------------------------
# Function Name : PreserveModel
# Description  : It is used to preserve model in secondary
# Parameters : df
# Return : None
# Date : 14/3/26
# Author : Rushikesh Dilip Narkhede
#----------------------------------------------------------------------------------------

def PreserveModel(model,filename):
    joblib.dump(model,filename)

    print("Model Preserved sucessfully with name : ",filename)


#----------------------------------------------------------------------------------------
# Function Name : TrainTitanicModel
# Description  : It does split X, Y, training data , testing data
# Parameters : df
# Return : None
# Date : 14/3/26
# Author : Rushikesh Dilip Narkhede
#----------------------------------------------------------------------------------------

def TrainTitanicModel(df):
    # Split features and label
    X = df.drop("Survived",axis = 1)
    Y = df["Survived"]

    print("Features :")
    print(X.head())

    print("\n Labels : ")
    print(Y.head())

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    X_Train, X_Test,Y_Train,Y_Test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("X_Train Shape : ",X_Train.shape)
    print("X_Test Shape : ",X_Test.shape)
    print("Y_Train Shape : ",Y_Train.shape)
    print("Y_Test Shape : ",Y_Test.shape)

    model = LogisticRegression(max_iter=1000)

    model.fit(X_Train,Y_Train)

    print("Model trained sucessfully")

    print("\n Intercept of model :")
    print(model.intercept_)

    print("\n Coeficent of model ")

    for feature,coeficent in zip(X.columns,model.coef_[0]):
        print(feature, " :",coeficent)

    PreserveModel(model,"MarvellousTitanic.pkl")

    loaded_model = LoadPreserveModel("MarvellousTitanic.pkl")

    Y_pred = loaded_model.predict(X_Test)

    accuracy = accuracy_score(Y_pred,Y_Test)
    print(accuracy)

    cm = confusion_matrix(Y_pred,Y_Test)

    print("Confusion matrix is : ")
    print(cm)




#----------------------------------------------------------------------------------------
# Function Name : DisplayInfo
# Description  : It display formated title
# Parameters : Title(str)
# Return : None
# Date : 14/3/26
# Author : Rushikesh Dilip Narkhede
#----------------------------------------------------------------------------------------

def DisplayInfo(title):
    print("\n"+"="*70)
    print(title)
    print("="*70)


#----------------------------------------------------------------------------------------
# Function Name : ShowData
# Description  : It shows basic information about dataset
# Parameters : df
#              df ->    pandas dataframe object
#              Message
#              message -> Heading text to display
# Return : None
# Date : 14/3/26
# Author : Rushikesh Dilip Narkhede
#----------------------------------------------------------------------------------------

def ShowData(df,message):
    DisplayInfo(message)
    print("First five rows of dataset : ")
    print(df.head())

    print("\n Shape of dataset : ")
    print(df.shape)

    print("\n Column Name : ")
    print(df.columns.tolist())

    print("Missing values in each column :")
    print(df.isnull().sum())

#----------------------------------------------------------------------------------------
# Function Name : CleanTitanicData
# Description  : It does preprocessing
#                It remove unnnessesory columns
#                It handle missing values
#                It convert text data to numeric format
#                It does encoding to the catagorical columns
# Parameters : df -> pandas dataframe
# Return : df -> Clean pandas dataframe
# Date : 14/3/26
# Author : Rushikesh Dilip Narkhede
#----------------------------------------------------------------------------------------

def CleanTitanicData(df):
    DisplayInfo("Step 2 : Original Data")

    print(df.head())

    # Remove unnnesesory column
    drop_column = ["Passengerid","zero","Name","Cabin"]

    existing_column =  [col for col in drop_column if col in df.columns]

    print("\n Column to be drop : ")
    print(existing_column)

    # drop the unwanted column
    df = df.drop(columns = existing_column)
    DisplayInfo("Step 2 : Data after column removal")
    print(df.head())

    # Handle Age Column
    if "Age" in df.columns:
        print("Age Column before filling missing values")
        print(df["Age"].head(10))
        
        # coerce -> Invalid value get converted NaN
        df["Age"] = pd.to_numeric(df["Age"],errors="coerce")

        age_median = df["Age"].median()

        # Replace missing values with median
        df["Age"] = df["Age"].fillna(age_median)

        print("\nAge column after preprocessing : ")
        print(df["Age"].head(10))

        # Handle fare column

        if "Fare" in df.columns:
            print("\n Fare column before preprocessin")
            print(df["Fare"].head(10))
            df["Fare"] = pd.to_numeric(df["Fare"],errors="coerce")

            fare_median = df["Age"].median()

            # Replace missing values with median
            df["Fare"] = df["Fare"].fillna(fare_median)
            print("\nFare column after preprocessing : ")
            print(df["Fare"].head(10))
            print("Median of fire column is :",fare_median)

        # Handle Embarked column
        if "Embarked" in df.columns:
            print("\n Embarked column before preprocessin")
            print(df["Embarked"].head(10))

            # Convert the data into string
            df["Embarked"] = df["Embarked"].astype(str).str.strip()

            # Remove missing values
            df["Embarked"] = df["Embarked"].replace(['nan','None',''],np.nan)

            # get most frequent value
            embarked_mode = df["Embarked"].mode()[0]
            print("Mode of Embarked Column :",embarked_mode)

            df["Embarked"] = df["Embarked"].fillna(embarked_mode)
            print("\nEmbarkedcolumn after preprocessing : ")
            print(df["Embarked"].head(10))

        # Handle Sex column

        if "Sex" in df.columns:
            print("\n Sex column before preprocessin")
            print(df["Sex"].head(10))
            df["Sex"] = pd.to_numeric(df["Sex"],errors="coerce")

            print("\n Sex column After preprocessin")
            print(df["Sex"].head(10))

        DisplayInfo("Data after preprocessing")
        print(df.head())
        
        print("\n Missing value after preprocessing")
        print(df.isnull().sum())

        #Encode Embarked column

        df = pd.get_dummies(df,columns=["Embarked"],drop_first=True)
        print("\n Data after Encodding")
        print(df.head())

        print("Shape of dataset : ",df.shape)

        # Convert boolean column into integer
        # 1 hot encodding

        for col in df.columns:
            if df[col].dtype == bool:
                df[col] = df[col].astype(int)

        print("\n Data after Encodding")
        print(df.head())


    return df



#----------------------------------------------------------------------------------------
# Function Name : MarvellousTitanicLogistic
# Description  : This is main pipeline controller.
#                It loads the dataset, show row data
#                It preprocess the dataset & train the model.
# Parameters : Data path of dataset file
# Return : None
# Date : 14/3/26
# Author : Rushikesh Dilip Narkhede
#----------------------------------------------------------------------------------------

def MarvellousTitanicLogistic(datapath):
    DisplayInfo("Step 1 : Loading the Dataset")
    df = pd.read_csv(datapath)

    ShowData(df,"Initial dataset")

    df = CleanTitanicData(df)

    TrainTitanicModel(df)






#----------------------------------------------------------------------------------------
# Function Name : main
# Description  : starting point of the application
# Parameters : None
# Return : None
# Date : 14/3/26
# Author : Rushikesh Dilip Narkhede
#----------------------------------------------------------------------------------------

def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")


if __name__ =="__main__":
    main()