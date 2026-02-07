import sys
import os
def DirectoryScannner(DirName = "Marvellous"):
    Ret = False
    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)

    if(Ret == False):
        print("It is not a directory")
        return
    
    for FolderName,SubFolder,FileName in os.walk(DirName):
        for fName in FileName:
            print(fName)
            

def main():
    Border="-"*60
    print(Border)
    print("-------------Marvellous directory automation----------------")
    print(Border)

    if(len(sys.argv)!=2):
        print("Invalid number of agruments")
        print("Please specify the name of directory")
        return
    
    DirectoryScannner(sys.argv[1])

if __name__ == "__main__":
    main()