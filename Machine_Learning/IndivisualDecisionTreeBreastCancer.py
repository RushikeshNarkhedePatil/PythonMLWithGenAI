import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

#----------------------------------------------------------------------------------------
# Step 1 : Load the dataset
#----------------------------------------------------------------------------------------

df = pd.read_csv("breast_cancer.csv")
print("Shape of dataset : ",df.shape)
print("First Five records : ",df.head())

#----------------------------------------------------------------------------------------
# Step 2 : Seperate features and label
#----------------------------------------------------------------------------------------

X = df.drop("target",axis=1)
Y = df["target"]

#----------------------------------------------------------------------------------------
# Step 3 : Split dataset for training and testing
#----------------------------------------------------------------------------------------

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#----------------------------------------------------------------------------------------
# Step 4 : Create model
#----------------------------------------------------------------------------------------

model = DecisionTreeClassifier(random_state=42)

#----------------------------------------------------------------------------------------
# Step 5 : Train  Model
#----------------------------------------------------------------------------------------

model.fit(X_train,Y_train)

#----------------------------------------------------------------------------------------
# Step 6 : Test model
#----------------------------------------------------------------------------------------

Y_pred = model.predict(X_test)

#----------------------------------------------------------------------------------------
# Step 7 : Evaluate  model
#----------------------------------------------------------------------------------------

print("Bagging Accurecy : ",accuracy_score(Y_test,Y_pred))
print("Confusion Matrix :")
print(confusion_matrix(Y_test,Y_pred))
