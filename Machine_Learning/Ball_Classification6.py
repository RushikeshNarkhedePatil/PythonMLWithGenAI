
from sklearn import tree

# Rough 1
# Smooth 0
# Cricket 2
# Tennis 1
def main():
    print("Ball Classification case study")

    # Original encoded data set
    # Independant variable
    X = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    # Dependant variables
    Y =[1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    # Independant variables for training.
    XTrain = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0]]
    # Independant variables for Testing.
    XTest = [[35,1],[95,0]]

    # Dependant variable for training
    YTrain = [1,1,2,1,2,1,2,1,1,1,2,1,2]
    # Dependant variable for Testing
    YTest = [1,2]

    modelobj = tree.DecisionTreeClassifier()
    # Training
    trainedModel = modelobj.fit(XTrain,YTrain)
    # Testing
    Result = trainedModel.predict([[35,1]])  # 1    2

    print(type(Result))

    if Result == 1:
        print("Object look like tennis ball")
    elif(Result == 2):
        print("Object looks like cricket ball")

    print("Model predict the object as : ",Result)







if __name__ =="__main__":
    main()

