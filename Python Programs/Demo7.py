class Demo:
    def __init__(self):
        try:
            a=int(input("Enter A value :"))
            b=int(input("Enter B value :"))
            c=a/b
            print("Result is: ",c)
        except:
            print("Can't divide with zero")#instead of throwing error,prints this line -Zero Division Exception
        finally:
            print("Thank you...")
#raise keyword-manually raise
d=Demo()#Object creation
