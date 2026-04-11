
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score,r2_score,confusion_matrix,classification_report

# Step 1 : Load Dataset
data = load_breast_cancer()

X = data.data
Y = data.target

print("Shape of X : ",X.shape)
print("Shape of Y : ",Y.shape)

# Step 2 : Split the dataset

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

# Step 3 : Create base models
model_LR  = LogisticRegression(max_iter=5000) 
model_DT  = DecisionTreeClassifier(random_state=42)
model_KNN = KNeighborsClassifier(n_neighbors=5)

# Step 4 : Train base models
model_LR.fit(X_train,Y_train)
model_DT.fit(X_train,Y_train)
model_KNN.fit(X_train,Y_train)

# Step 5 : Calculate Individual accurecy
pred_lr = model_LR.predict(X_test)
pred_dt = model_DT.predict(X_test)
pred_knn = model_KNN.predict(X_test)

acc_lr = accuracy_score(pred_lr,Y_test)
acc_dt = accuracy_score(pred_dt,Y_test)
acc_knn = accuracy_score(pred_knn,Y_test)

print("Individual model accurecy")
print("Logistic Regration :",acc_lr)
print("Decision tree :",acc_dt)
print("KNN:",acc_knn)