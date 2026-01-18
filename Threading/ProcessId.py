import os

def main():
    print("PID of Running process : ",os.getpid())
    print("PID of Parent Procece is : ",os.getppid())

if __name__ == "__main__":
    main()