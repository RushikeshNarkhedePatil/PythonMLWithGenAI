import time
import datetime
import schedule

def fun():
    print("Inside funt at :",datetime.datetime.now())

def main():
    print("Inside Marvellous automation script at : ",datetime.datetime.now())
    schedule.every(20).seconds.do(fun)
    #Problem on this code is it will run only one time after 20 seconds

if __name__ == "__main__":
    main()