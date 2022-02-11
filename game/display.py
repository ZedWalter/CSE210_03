class Display:
    """
    
    The responsibility of Display is to create and display the picture to the game.
    
    """

    def __init__(self):
        self._body = """   /|\\
   / \\
                """
    
        self._line = 0
        self.head = "    o    "
        self._newparachute = []
        self._parachute = [
        "   ___  ", #0
        " / ___ \ ", #1
        " \     / ", #2
        "  \   /  ", #3
        self.head #4
        ]


    def parachute(self, lives):
        if lives == 0:
            self.head = "    x"
            self._parachute[4] = self.head
            self._newparachute = self._parachute[4:]
            # print (self._parachute)
            return self._newparachute

        self._newparachute = self._parachute[-1*(lives-4):]
        
        return self._newparachute

    
    def print_man(self):
        for x in self._newparachute:
            print(x)
        print(self._body)

# dsp = Display()
# dsp.parachute()
# dsp.print_man()

#   ___
# / ___ \
# \     /
#  \   /
#    o
#   /|\
#   / \