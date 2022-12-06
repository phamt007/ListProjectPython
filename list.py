#List setups

class List:

    character = []


    def hello(self):
        print("Hello!")
    def inserttxt(self):
        print("Inserting text file")
        i = 0
        f = open("text.txt", "r")
        word = f.readlines()
        size = len(word)
        while(i < size):
            self.character.append(word[i].rstrip('\n'))
            i = i+1
        f.close()
    def changetxt(self):
        print("Saving List")
        i = 0
        f = open("text.txt", "w")
        self.character.append("Final")
        f.write('\n'.join(self.character))
    def insert(self, word):
        print("Insert")
        self.character.append(word)
    def remove(self, number):
        print("Remove")
        word = self.character[number-1]
        self.character.remove(word)
    def display(self):
        print("Display")
        i = 0
        while(i < len(self.character)):
            if(self.character[i]):
                print(i+1,". ",self.character[i])
                
            i += 1
        print("")

