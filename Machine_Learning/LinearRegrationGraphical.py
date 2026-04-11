import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def MarvellousPredictor():
    #Load the Data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independant variable : ",X)
    print("Values of Dependant variable : ",Y)

    mean_x =np.mean(X)
    mean_y = np.mean(Y)

    print("X_Mean is :",mean_x) # 3.0
    print("Y_Mean is :",mean_y) # 3.6

    n = len(X)  # 5
    # Y=mX+C

    # m = (summ(x-X_bar) * (Y-Y_Bar)) / (summ (X-X_Bar) **2)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x) **2)

    m = numerator / denominator

    print("Slope of line i.e m : ",m)   # 0.4

    C = mean_y - (m*mean_x)

    print("Y Intercept of line i.e C : ",C) # 2.4

    # Graph

    x = np.linspace(1,6,n)
    y = C + m * x

    plt.plot(x,y,color='g',label="Regrassion Line")
    plt.scatter(X,Y,color='r',label="Scatter plot")
    plt.xlabel("X : Independant variables")
    plt.ylabel("Y : Dependant variables")
    plt.legend()
    plt.show()

    # Calculate YP
    # Calculate R **2




def main():
    MarvellousPredictor()
    

if __name__ =="__main__":
    main()