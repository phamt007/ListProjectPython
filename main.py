#Tim Pham
#Check list Project with Python
from list import *

def main():
    print("Check list Project")
    obj = List()
    user = 0
    word = ""
    number = 0 
    i = 0

    obj.inserttxt()
    obj.display()



    print("Welcome, enter")
    while(i != 4):
        print("1 - Insert")
        print("2 - Remove")
        print("3 - Display")
        print("4 - Exit")
        
        user = int(input("Enter command:"))
        i = user
        if(user == 1):
            print("What do you want to add to the list?")
            word = input("")
            obj.insert(word)
            word = ""
            obj.display()
        if(user == 2):
            print("What do you want to remove from the list?")
            number = int(input("Enter the number the topic is in: "))
            obj.remove(number)
            obj.display()
        if(user == 3):
            obj.display()
        if(user == 4):
            obj.changetxt()

    

if __name__ == "__main__":
    main()
    