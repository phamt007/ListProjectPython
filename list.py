#List setups

class List:

    character = []


    def hello(self):
        print("Hello!")
    def insert(self, word):
        print("Insert")
        self.character.append(word)
        self.character.append("word")
        self.character.append("word")
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

