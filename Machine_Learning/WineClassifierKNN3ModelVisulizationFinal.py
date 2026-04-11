import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler

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

    # Step 4 : Split the dataset from training and testing
    print(border)
    print("Step 4 : Split the dataset from training and testing")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42, stratify=Y)

    print(border)
    print("Information of Training and testing data :")
    print("X_train shape : ",X_train)
    print("X_test shape : ",X_test)
    print("Y_train shape : ",Y_train)
    print("Y_test shape : ",Y_test)
    print(border)

    # Step 5 : Features Scaling
    print(border)
    print("Step 5 : Feature Scaling")
    print(border)

    scaler = StandardScaler()
    # Independant variable  scaling
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    print("Feature scaling is done")

    # Step 6 : Explore the multiple values of k
    # Hyper parameter tuning (K)
    print(border)
    print("Step 6 : Explore the multiple values of k")
    print(border)

    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)
        accurecy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accurecy)

    print(border)
    print("Accuecy report of all K values from 1 to 20")

    for value in accuracy_scores:
        print(value)

    print(border)

    # Step 7 : Plot graph 
    print(border)
    print("Step 7 : Plot graph of k vs accurecy")
    print(border)

    plt.figure(figsize=(8,5))
    plt.plot(K_values,accuracy_scores,marker = 'o')
    plt.title("K Values vs Accurecy")
    plt.xlabel("Value of K")
    plt.ylabel("Accurecy")
    plt.grid(True)

    plt.xticks(list(K_values))
    plt.show()

    # Step 8 : Find best value of k
    print(border)
    print("Step 8 : Find best value of k")
    print(border)

    best_k = list(K_values)[accuracy_scores.index(max(accuracy_scores))]

    print("Best value of K is : ",best_k)

    # Step 9 : Build final model using final model of k
    print(border)
    print("Step 9 : Build final model using final model of k")
    print(border)

    final_Model = KNeighborsClassifier(n_neighbors=best_k)

    final_Model.fit(X_train_scaled,Y_train)
    Y_pred = final_Model.predict(X_test_scaled)
    
    # Step 10 : Calculate final accurecy
    print(border)
    print("Step 10 : Calculate final accurecy")
    print(border)

    accurecy = accuracy_score(Y_test,Y_pred)
    print("Accurecy of model is : ",accurecy * 100)

    # Step 11 : Display Confusion matrix
    print(border)
    print("Step 11 : Display Confusion matrix")
    print(border)

    cm = confusion_matrix(Y_test,Y_pred)

    print(cm)

    # Step 12 : Display Classification Report
    print(border)
    print("Step 12 : Display Classification Report")
    print(border)

    print(classification_report(Y_test,Y_pred))




def main():
    border = "-"*40

    print(border)
    print("Wine Classifier using KNN")
    print(border)

    MarvellousClassifier("WinePredictor.csv")



if __name__ =="__main__":
    main()