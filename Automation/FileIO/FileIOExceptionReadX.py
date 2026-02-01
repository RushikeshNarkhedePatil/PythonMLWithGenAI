

def main():

    try:
        fobj = open("Hello.txt","r")
        print("File gets sucessfully opened")

        data = fobj.read(6)

        print("Data From file is : " , data)
        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")
    finally:
        print("End Of Application")
      

if __name__ == "__main__":
    main()