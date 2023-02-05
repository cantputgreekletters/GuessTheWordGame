class Game:
    def __init__(self):
        self.__dictionary = ["the","of","and","a","to","in","is","you","that","it","he","was","for","on","are","as","with","his","they","I","at","be","this","have","from","or","one","had","by","word","but","not","what","all","were","we","when","your","can","said","there","use","an","each","which","she","do","how","their","if","will","up","other","about","out","many","then","them","these","so","some","her","would","make","like","him","into","time","has","look","two","more","write","go","see","number","no","way","could","people","my","than","first","water","been","call","who","oil","its","now","find","long","down","day","did","get","come","made","may","part"]
        self.__chosen_word = None
        self.__tries = 10
        self.__has_ended = False
        self.__guessed_letters = []
        self.__found_letters = []
        self.__word_letters = None
        self.__get_word()
        self.__get_word_letters()
        self.__start()
    
    def __get_word(self):
        from random import randint as rn
        x = len(self.__dictionary) - 1
        self.__chosen_word = self.__dictionary[rn(0,x)]
        print("Picked a word")
        del rn
    
    def __get_word_letters(self):
        array = [i for i in self.__chosen_word]
        new_array = []
        new_array = [i for i in array if i not in new_array ]
        self.__word_letters = new_array
        
    
    def __print_found_letters(self):
        for i in self.__chosen_word:
            if i not in self.__found_letters:
                print("_",end="")
            else:
                print(i,end="")
        print("\n")
    def __ask(self):
        while True:
            letter = input("give a letter\n")
            if len(letter) > 1 or letter == " ":
                print("Invalid Option")
            elif letter in self.__guessed_letters:
                print("You have already picked this letter")
            else:
                break
        return letter
    
    def __check(self,letter):
        self.__guessed_letters.append(letter)
        if letter in self.__chosen_word:
            self.__found_letters.append(letter)
            print("You found a letter")
        else:
            print("This letter is not in the word")
            self.__tries -= 1

    def __check_if_ended(self):
        if self.__tries == 0:
            self.__has_ended = True
            return
        if len(self.__found_letters) == len(self.__word_letters):
            self.__has_ended = True
            print("You found all the letters!!!")
            return


    def __start(self):
        
        while not self.__has_ended:
            self.__print_found_letters()
            letter = self.__ask()
            self.__check(letter)
            self.__check_if_ended()
        if len(self.__found_letters) != len(self.__word_letters):
            print("You lost")
        print("The word is: {word}".format(word=self.__chosen_word))
            
Game = Game()