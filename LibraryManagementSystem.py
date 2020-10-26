#this library management system helps to operate all the libraries of a state
import time
class Library:
    def __init__(self,alist,aname):
        self.list = alist
        self.name = aname
        self.lendDict = {}
    def printbooks(self):
        print(f"We have following books in our  {self.name} ")
        for i in self.list:
            print(i)
    def lendbooks(self,user,lnd1):
        if lnd1 not in self.lendDict.keys():
            self.lendDict.update({lnd1: user})
            print("Loading..................................Please wait")
            time.sleep(2)
            print(f"""The book {lnd1} is ready and you can take it now!!""")
        else:
            print("Loading..................................")
            time.sleep(2)
            print(f"""Sorry the book is already taken by {self.lendDict[lnd1]} 
                    Please wait until {self.lendDict[lnd1]} returrns the book""")
            print("You can exit or continue searching for other books")
    def addabook(self,addbook):
        self.list.append(addbook)
        print(f"Congratulations Your book {addbook} has been added")
        print("Loading..................................Please wait")
        time.sleep(2)
        print("You can exit or continue browsing for other books")
    def returnbook(self,rebook):
        self.lendDict.pop(rebook)
        print(f"Your book {rebook} has been returned successfully")
        print("Loading..................................")
        time.sleep(1)
        print("You can exit or continue browsing for other books")

if __name__ == '__main__':
    smart_library = Library(["Maths","Biology","History","Political Science","Chemistry","English"],"Smart Library")
    m=10      #i have simply created a variable m to make while as infinite loop
    while(m!=0):
        print(" ---------------Welcome to Smart Library----------------------")
        time.sleep(2)
        print("Loading..................................Please wait")
        print(f"""" Please select the option that you want to do
                    1.Display the collections of books we have 
                    2.Lend a book from our library
                    3.Add a book to our library
                    4.Return a book to our library
                    5.Exit the library""")

        try:
                n = int(input("Enter your option  here"))
                print("Loading..................................Please wait")
                time.sleep(2)
                if n == 1:
                    print("Loading..................................Please wait")
                    time.sleep(2)
                    print("Ok so you want to Display the collections of books we have")
                    print("Loading..................................Please wait")
                    time.sleep(2)
                    smart_library.printbooks()
                elif n == 2:
                    print("Ok so you want to Lend a book")
                    time.sleep(2)
                    lnd = input("Please enter name of book which you want to lend ?")
                    print("Loading..................................Please wait")
                    time.sleep(2)
                    user_name = input("Please enter your name")
                    print("Loading..................................Please wait")
                    time.sleep(2)
                    smart_library.lendbooks(user_name, lnd)
                elif n == 3:
                    print("Ok so you want to Add a book")
                    print("Loading..................................Please wait")
                    time.sleep(1)
                    print("You are welcome to add books into our library")
                    print("Loading..................................Please Wait")
                    time.sleep(2)
                    add_name = input("Please enter the name of the book which you wanna add")
                    print("Loading..................................Please wait")
                    time.sleep(2)
                    smart_library.addabook(add_name)

                elif n == 4:
                    print("Ok so you want to return a book")
                    print("Loading..................................Please wait")
                    time.sleep(1)
                    print("We are glad to see that you are returning the books")
                    print("Loading..................................Please wait")
                    time.sleep(2)
                    rebook = input("Please Enter name of book that you wanna return")
                    smart_library.returnbook(rebook)
                elif n==5:
                    print("Thanks for visiting the library..........Hope to see you soon")
                    m=0
                else:
                    print("Please select a valid option")

        except Exception as e:
                print("Please enter a valid option as 1,2,3 or 4")

