#  [A,B,C,D]
# X[1,2,3,5]
# Y[2,3,1,6]
#  [R,R,B,B]

# Predict (3,3) -->?

def MarvellousKNeighoberClassifier():
    Border = "-"*50
    data =[
            {'point' : 'A','X':1,'Y':2,'label' :"Red"},
           {'point' : 'B','X':2,'Y':3,'label' :"Red"},
            {'point' : 'C','X':3,'Y':1,'label' :"Blue"},
             {'point' : 'D','X':5,'Y':6,'label' :"Blue"}
           ]
    
    print(Border)
    print("Marvellous user define knn")
    print(Border)

    print(Border)
    print("Training Data set")
    print(Border)

    for i in data:
        print(i)

def main():
    MarvellousKNeighoberClassifier()
    



if __name__ == "__main__":
    main()