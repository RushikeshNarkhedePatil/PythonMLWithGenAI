import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)
Border = "-"*40
##############################################################################################
# Step 1 : Load the dataset
##############################################################################################
print(Border)
print("Step 1 : Load The Dataset")
print(Border)

datasetpath = "iris.csv"

df = pd.read_csv(datasetpath)

print("Dataset gets loaded sucessfully...")
print("Initial entries from dataset :")
print(df.head())

##############################################################################################
# Step 2 : Data Analysis (EDA)
##############################################################################################
print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of dataset : ",df.shape)
print("Column Names : ",list(df.columns))

print("Missing values (Per Column)")
print(df.isnull().sum())

print("Class Distribution (Species Count)")
print(df["species"].value_counts())

print("Statistical Report of dataset")
print(df.describe())

##############################################################################################
# Step 3 : Decide Independant and Dependant variable
##############################################################################################
print(Border)
print("Step 3 : Decide Independant and Dependant variable")
print(Border)

# X : Independant variable / Feature
# Y : Dependant variable / Label

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

X = df[feature_cols]
Y = df["species"]

print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape)

##############################################################################################
# Step 4 : Visulization of Dataset
##############################################################################################
print(Border)
print("Step 4 : Visulization of Dataset")
print(Border)

# Scatter plot
plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"], label = sp)

plt.title("Iris : Petal Length vs Petal Width")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid(True)
plt.show()

