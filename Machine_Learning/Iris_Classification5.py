
from sklearn.datasets import load_iris

# Rough 1
# Smooth 0
# Cricket 2
# Tennis 1
def main():
    print("Iris Classification case study")

    Dataset = load_iris()

    Border =  "-"*40

    print(Border)

    for i in range(len(Dataset.target)):
        print("Id %d , Features %s , Label %s"%(i,Dataset.data[i],Dataset.target[i]))
    print(Border)

if __name__ =="__main__":
    main()

