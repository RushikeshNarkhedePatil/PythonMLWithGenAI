

def main():

    try:
        fobj = open("Hello.txt","r")
        print("File gets sucessfully opened")

        print("Current offset is :",fobj.tell()) # 0

        fobj.seek(7)
        print("Current offset is :",fobj.tell())    # 7

        data = fobj.read(10)

        print("Current offset is :",fobj.tell())    # 17

        print("Data From file is : " , data)
        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")
    finally:
        print("End Of Application")
      

if __name__ == "__main__":
    main()