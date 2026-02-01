#seek(kuthe,kuthun)
#kuthun : 0 / 1 / 2
# 0 : Starting
# 1 : Current
# 2 : End

def main():

    try:
        fobj = open("Hello.txt","r")
        print("File gets sucessfully opened")

        print("Current offset is :",fobj.tell()) # 0

        fobj.seek(6,1)
        print("Current offset is :",fobj.tell())    # 11

        data = fobj.read(6)

        print("Current offset is :",fobj.tell())    # 17

        print("Data From file is : " , data)
        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")
    finally:
        print("End Of Application")
      

if __name__ == "__main__":
    main()