import random

class Word:
    """
    The responsibility of word is to initialize an array with a list of words and pick a random word

    Attributes:
        
    """
    word_list = None

    # This function initializes our word class with an empty array.
    def __init__(self):
        self._puzzle_word = self.get_word()
        self.word_list = []

    # This function appends the list of words you want to use to your list.
    def add_word(self):
        #adding some words to intially help test our display program
        test_list = ['pasta', 'ramen', 'steak', 'apple', 'lemon', 'onion', 'snail']
        self.word_list.extend(test_list)

    # This function grabs a random word from the list and returns it.
    def get_word(self):
        length = len(self.word_list)
        word = self.word_list[random.randint(0,length - 1)]

        return word

    def get_puzzle_word(self): return self._puzzle_word