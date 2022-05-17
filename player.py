#
# A Connect-Four Player class 
#  

from board import Board

# write your class below.

class Player:
    """ a data type for a Connect Four player
    """  
    
    def __init__(self, checker):
        """ constructor for Player
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        """ returns a string representing a Player object.
        The string returned should indicate which checker
        the Player object is using.
        """
        s = 'Player ' + self.checker
        return s
    
    def opponent_checker(self):
        """ returns a one-character string representing the
        checker of the Player object’s opponent.
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, b):
        """ returns the column where the player wants to make
        the next move. Also increments the number of moves that
        the Player object has made.
        input b: a Board object 
        """
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col):
                return col
            else:
                print('Try again!')
