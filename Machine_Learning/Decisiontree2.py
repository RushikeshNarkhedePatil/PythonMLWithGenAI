from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
def main():
    iris = load_iris()

    X= iris.data
    Y = iris.target

    x_train,X_test,Y_tain,Y_test = train_test_split(X,Y,test_size=0.2)

    model = DecisionTreeClassifier()

    model.fit(x_train,Y_tain)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test,y_pred)

    print("Accuracy is : ",accuracy*100)

    # Visulizatin
    plt.figure(figsize=(12,8))

    plot_tree(model,filled=True,feature_names=iris.feature_names,class_names=iris.target_names)

    plt.title("Marvellous Decision tree classifier")
    plt.show()


if __name__ == "__main__":
    main()