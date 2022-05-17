from gamePlay import *
from player import *
from board import *
from AIPlayer import *
import random


# mode 1: Two Player
# uncomment to play as two-player
# connect_four(Player('X'), Player('O'))


# mode 2: Single Player vs Random Player
# uncomment to play with random player
# connect_four(Player('X'), RandomPlayer('O'))

# mode 3: Single Player vs AI Player
# uncomment to play with AI player
# connect_four(Player('X'), AIPlayer('O', 'RANDOM', 5))