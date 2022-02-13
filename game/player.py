from word import Word

class Player:
    """One who plays the game.
    
    Responsibility: to handle and validate user input.
    
    Attributes:
        _lives -> The number of lives the player has   
        is_alive -> To make sure if the player still has lives left
        word -> the random word taken from the Word class
        display_list -> a list that shows how many letters the user has guessed right
        guess_correct -> a bool on whether or not the player has guessed correctly
        self.guess -> the guess of the player.
    """
    def __init__(self):
        self._lives = 5
        self.is_alive = True
        self.word = Word().get_puzzle_word
        self.display_list = []
        self.guess_correct = False
        self.guess = None
    
    def get_input(self):
        self.guess = input("Enter a letter: ")
        return self.guess
    
    def create_display_list(self):
        for i in len(self.word):
            self.display_list.append("_")
        return self.display_list

    def guess_is_correct(self):
        self.guess_correct = False
        for i in len(self.word):
            if self.guess == self.word[i]:
                self.guess_correct = True
                self.display_list[i] = self.guess
        return self.guess_correct

    def guess_is_wrong(self):
        self._lives -= 1

    def display(self):
        print(self.display_list)

    def manage_lives(self):
        if self.guess_is_correct() != True:
           self.guess_is_wrong()
           if self._lives == 0:
               self.is_alive = False
        self.display()