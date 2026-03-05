
from sklearn import tree

# Rough 1
# Smooth 0
# Cricket 2
# Tennis 1
def main():
    print("Ball Classification case study")

    #Data Loading Step 1
    # Independant variable
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    # Dependant variables
    Labels =[1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    modelobj = tree.DecisionTreeClassifier()
    # Training
    trainedModel = modelobj.fit(Features,Labels)
    # Testing
    Result = trainedModel.predict([[37,1],[94,0]])  # 1    2

    print("Model predict the object as : ",Result)





if __name__ =="__main__":
    main()

