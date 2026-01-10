def Display(A,B,C,D):
    print(A,B,C,D)

def main():
    #Display(10,20) # Not allowed - Less agrguments
    #Display(10,20,30,40,50) # Not Allowed - extra arguments
    Display(10,20,30,40) # Allowed

if __name__ == "__main__":
    main()