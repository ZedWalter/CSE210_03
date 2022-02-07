from word import Word

class Player:
    """One who plays the game.
    
    Responsibility: to handle and validate user input.
    
    Attributes:
        
        
    """
    def __init__(self):
        self.word_list = []

    def _split_word(self):
        word = Word()
        game_word = word.get_word()
        self.word_list = list(game_word)


    def display_empty_word(self):
        empty_array = []
        for I in range(1, len(self.word_list)):
            empty_array.append('_')
        
        return empty_array
