import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

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