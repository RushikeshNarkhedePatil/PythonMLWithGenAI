import sys
import os
import time

def DirectoryScannner(DirName = "Marvellous"):
    Border="-"*60
    time_stamp = time.ctime()

    fobj = open("Marvellous.log","w")

    fobj.write(Border +"\n")
    fobj.write("This is a log file created by marvellous automation\n")
    fobj.write("This is a directory Cleaner script\n")
    fobj.write(Border +"\n")
    Ret = False
    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)

    if(Ret == False):
        print("It is not a directory")
        return
    
    FileCount = 0
    EmptyFileCount = 0
    
    for FolderName,SubFolder,FileName in os.walk(DirName):
        
        for fName in FileName:
            FileCount = FileCount + 1   # File counter

            fName = os.path.join(FolderName,fName)

            if(os.path.getsize(fName) == 0):    # Empty file
                EmptyFileCount = EmptyFileCount + 1
                os.remove(fName)


    fobj.write("Total Files scaned : "+str(FileCount) + "\n")
    fobj.write("Total Empty File found : "+ str(EmptyFileCount) + "\n")
    fobj.write("This log file is created at : "+time_stamp+"\n")
    fobj.write(Border + "\n")

    fobj.close()
            

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

    print(Border)
    print("-------------Marvellous directory automation----------------")
    print(Border)

if __name__ == "__main__":
    main()