import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error,r2_score

#----------------------------------------------------------------------------------------
# Step 1 : Load the dataset
#----------------------------------------------------------------------------------------

df = pd.read_csv("california_housing.csv")
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
# Step 4 : Create Gradient Boosting model
#----------------------------------------------------------------------------------------

boosting_model = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
    )

#----------------------------------------------------------------------------------------
# Step 6 : Train boosting Model
#----------------------------------------------------------------------------------------

boosting_model.fit(X_train,Y_train)

#----------------------------------------------------------------------------------------
# Step 6 : Test boosting model
#----------------------------------------------------------------------------------------

Y_pred = boosting_model.predict(X_test)

#----------------------------------------------------------------------------------------
# Step 7 : Evaluate boosting model
#----------------------------------------------------------------------------------------

print("Mean Sequred Error : ",mean_squared_error(Y_test,Y_pred))
print("R Sequre : ",r2_score(Y_test,Y_pred))

