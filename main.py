#Tim Pham
#Check list Project with Python
from list import *

def main():
    print("Check list Project")
    obj = List()
    obj.hello()
    word = "Hello World!"
    obj.insert(word)
    obj.display()
    obj.remove(1)
    obj.display()

if __name__ == "__main__":
    main()
    