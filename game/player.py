from word import Word

class Player:
    """One who plays the game.
    
    Responsibility: to handle and validate user input.
    
    Attributes:
        
        
    """
    def __init__(self):
        self.word_list = []
        self.lives = 5

    def _split_word(self):
        word = Word()
        game_word = word.get_word()
        print(game_word)
        self.word_list = list(game_word)


    def display_game_word(self):
        self.game_array = []
        for I in range(0, len(self.word_list)):
            self.game_array.append('_')
        
        return self.game_array

    def user_guess(self):
        guess = input('What letter would you like to guess? ')
        if guess in self.word_list:
            for I in self.word_list:
                index = self.word_list.index(guess)
                self.game_array[index] = guess
        else:
            self.lives - 1
            print('Sorry, that letter is not in the word.')

        return self.game_array


def main():
    player = Player()
    player._split_word()
    game_word = player.display_game_word()
    print(game_word)
    after_guess = player.user_guess()
    print(after_guess)

main()