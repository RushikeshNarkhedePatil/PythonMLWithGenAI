import os

def DirectoryScanner(DirectoryName ="Marvellous"):

    print("Contents of the directory are : ")
    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        print("Folder name : ",FolderName)

        for Subf in SubFolderName:
            print("Sub Folder Name : ",Subf)

        for fname in FileName:
            print("File Name : ",fname)

def main():
    DirectoryName = input("Enter the name of directory : ")
    Ret = os.path.exists(DirectoryName)
    if(Ret == False):
        print("There is no directory available")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if(Ret == False):
        print("There is no directory")
        return
    DirectoryScanner(DirectoryName)





if __name__ == "__main__":
    main()