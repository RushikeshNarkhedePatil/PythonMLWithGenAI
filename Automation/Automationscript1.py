import schedule
import time
import datetime
import sys

def main():
    Border = "-"*40
    print(Border)
    print("----------Marvellous Automation---------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == '__h') or (sys.argv[1] == '__H')):
            print("This application is used to perform ----")
            print("This is a automation script")

        elif((sys.argv[1] == '__u') or (sys.argv[1] == '__U')):
            print("Used the given script as ")
            print("ScriptName.py Argument1 Argument2")
            print("Argument1 : _______________")
            print("Argument2 : _______________")

        else:
            print("Used the given flag as : ")
            print("__u :Used to display the usage")
            print("__h :Used to display the help")

    else:
        print("Invalid Number of command line arguments")
        print("Used the given flag as : ")
        print("__u :Used to display the usage")
        print("__h :Used to display the help")

    print(Border)
    print("-----Thank you for using our script-----")
    print("----------Marvellous Infosystems--------")
    print(Border)

    
if __name__ == "__main__":
    main()