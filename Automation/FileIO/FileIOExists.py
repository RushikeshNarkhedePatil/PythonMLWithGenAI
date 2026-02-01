import os

def main():
    FileName = input("Enter the name of file : ")

    Ret = os.path.exists(FileName)

    if(Ret == True):
        print("Files gets sucessfully opened")
        fobj = open(FileName,"r")
    else:
        print("Threre is no such files")

      

if __name__ == "__main__":
    main()