from game.word import Word
from game.display import Display
from game.player import Player

class Director:
    """A person who directs the game.
    
    The responsibility of the Director is to control the program event order.
    """
    
    def __init__(self):
        """Constructs a new Director instance.
        Far 
        Args:
            self(Director): an instance of the Director
        """
        self._playing = True
        self.grab_input = None
    def start_game(self):
        
        disp = Display()
        palp = Player()
        disp.parachute(self, palp.return_lives)
        disp.print_man()
        while self.playing:
            palp.get_input
            palp.create_display_list()
            disp.parachute(self, palp.return_lives)
            disp.print_man()
            if palp.lives == 0:
                self.grab_input = input("Would you like to play again?: [y/n]")
                if self.grab_input == "y":
                    self.playing = True
                else:
                    self.playing = False
