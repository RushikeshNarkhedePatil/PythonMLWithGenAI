import hashlib
import os

def DirectoryWatcher(DirectoryName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret  = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("there is no directory")
        return
    
    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):

        for fName in FileName:
           fName = os.path.join(FolderName,fName)
           CheckSum = CalculateCheckSum(fName)

           print(f"File name : {fName} CheckSum : {CheckSum}")
    

def CalculateCheckSum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()
        

def main():
    DirectoryWatcher()
    
if __name__ =="__main__":
    main()