#Imports
from random import randint as rn
#CONSTANTS

all_words = ["the","of","and","a","to","in","is","you","that","it","he","was","for","on","are","as","with","his","they","I","at","be","this","have","from","or","one","had","by","word","but","not","what","all","were","we","when","your","can","said","there","use","an","each","which","she","do","how","their","if","will","up","other","about","out","many","then","them","these","so","some","her","would","make","like","him","into","time","has","look","two","more","write","go","see","number","no","way","could","people","my","than","first","water","been","call","who","oil","its","now","find","long","down","day","did","get","come","made","may","part"]
digits = "0123456789"


class Game:
    
    def __init__(self) -> None:
        self.__chosen_word = None
        self.__tries = 10
        self.__has_ended = False
        self.__guessed_letters = []
        self.__found_letters = []
        self.__word_letters = []
        self.__current_pick = None
    
    def __pick_word(self):
        self.__chosen_word = all_words[rn(0,len(all_words) - 1)]
    def __ask_for_letter(self):
        self.__current_pick = None
        while self.__current_pick == None or self.__current_pick in digits or len(self.__current_pick) > 1 or self.__current_pick in self.__found_letters:
            self.__current_pick = input("Give a letter\n")
        if self.__current_pick not in self.__guessed_letters: self.__guessed_letters.append(self.__current_pick)

    def __Print(self):
        word = ""
        for i in self.__chosen_word:
            word += i if i in self.__found_letters else "_"
        print(self.__guessed_letters)
        print(word)
    
    def __check_if_found(self):
        for i in self.__chosen_word:
            if i == self.__current_pick: 
                if i not in self.__found_letters: self.__found_letters.append(i) 
                print("found a letter")
                return
        print("didn't find letter")

    def __check_if_won(self):
        self.__has_ended = len(self.__found_letters) == len(self.__word_letters) or self.__has_ended
        return len(self.__found_letters) == len(self.__word_letters)
    
    def __end_if_no_tries(self):
        self.__has_ended = self.__tries <= 0
    
    def Play(self):
        self.__pick_word()
        self.__word_letters = [i for i in self.__chosen_word if i not in self.__word_letters]
        while not self.__has_ended:
            self.__Print()
            self.__ask_for_letter()
            self.__check_if_found()
            self.__tries -= 1
            self.__end_if_no_tries()
            self.__check_if_won()
            
        if self.__check_if_won():
            print("You won")
        else:
            print("You lost")
            print(self.__chosen_word)
            

        

t = Game()
t.Play()
