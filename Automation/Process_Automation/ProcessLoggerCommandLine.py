# Command Line Input

import psutil
import sys



def main():
    Border = "-"*50
    print(Border)
    print("------Marvellous Platform Surveillance System-----")
    print(Border)

    if(len(sys.argv)== 2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This script is used to :")
            print("1 : Create automatic logs")
            print("2 : Execute Periodacally")
            print("3 : Send mail with the log")
            print("4 : store information about processes")
            print("5 : Store information about CPU")
            print("6 : Store information about RAM usage")
            print("7 : Store information about secondary storage")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Used the automation script as : ")
            print("Scriptname.py Time Interval Directoryname")
            print("TimeInterval :  the time in minutes for periodic scheduling")
            print("DirectoryName : Name of directory to create auto log")
        else:
            print("Unable to procced as there is no such option")
            print("please use --h or --u get more details")
    # Python3 Demo.py 5 Marvellous
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval : ",sys.argv[1])
        print("Directory Name : ",sys.argv[2])
    else:
        print("Invalid number of command line arguments")
        print("Unable to procced as there is no such option ")
        print("please use --h or --u get more details")



    print(Border)
    print("----------Thank you for using our script----------")
    print(Border)

if __name__ =="__main__":
    main()