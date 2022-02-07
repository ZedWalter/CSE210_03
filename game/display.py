class Display:
    """
    
    The responsibility of Display is to create and display the picture to the game.
    
    """

    def __init__(self):
        self._body = """  /|\
                          / \
                """
        self._line = 0
        self.head = "o"
        self._parachute = [
        "  ___  \n",
        " / ___ \ \n",
        " \     / \n",
        "  \   /  \n", 
        self.head
        ]


    def parachute(self, lives):
        self._line = lives
        for _ in range(self._line, 5):
            self._line += 1

    def print_man(self):
        print(self._parachute + self._body)





#   ___
# / ___ \
# \     /
#  \   /
#    o
#   /|\
#   / \