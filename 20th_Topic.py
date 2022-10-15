#Write python program that user to enter only odd numbers, else will raise an exception.

def Oddnumber():
    try:
        n=(int(input("Enter the Value:")))
        if n%2>=1:
            print("This number is ODD.")
        else:
            raise Exception
    except Exception as e:
        print("Exception Caught:-Not an even number!")
Oddnumber()





