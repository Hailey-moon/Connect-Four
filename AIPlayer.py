
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """ looks ahead some number of moves into the future to assess
    the impact of each possible move that it could make for its next
    move, and it will assign a score to each possible move
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ inherits from Player but adds tiebreak and lookahead
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def  __repr__(self):
        """ returns a string representing an AIPlayer object, including
        the checker, tiebreaking straategy, and lookahead.
        """
        s = 'Player ' + str(self.checker) + ' (' + str(self.tiebreak) + ', ' + str(self.lookahead) + ')'
        return s
    
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of
        the board, and that returns the index of the column with the
        maximum score. If one or more columns are tied, the method
        should apply the called AIPlayer‘s tiebreaking strategy to
        break the tie.
        """
        max_score = max(scores)
        index_list = []
        for i in range(len(scores)):
            if scores[i] == max_score:
                index_list += [i]
        if self.tiebreak == 'LEFT':
            return index_list[0]
        elif self.tiebreak == 'RIGHT':
            return index_list[-1]
        elif self.tiebreak == 'RANDOM':
            return random.choice(index_list)
        
    def scores_for(self, b):
        """ takes a Board object b and determines the called AIPlayer‘s
        scores for the columns in b.takes a Board object b and determines
        the called AIPlayer‘s scores for the columns in b.
        """
        scores = [0] * b.width
        for i in range(len(scores)):
            if b.can_add_to(i) == False:
                scores[i] = -1
            elif b.is_win_for(self.checker):
                scores[i] = 100
            elif b.is_win_for(self.opponent_checker()):
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50
            else:
                b.add_checker(self.checker, i)
                opp = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opp.scores_for(b)
                if max(opp_scores) == 100:
                    scores[i] = 0
                elif max(opp_scores) == 50:
                    scores[i] = 50
                elif max(opp_scores) == 0:
                    scores[i] = 100
                b.remove_checker(i)
        return scores
    
    def next_move(self, b):
        """ returns the called AIPlayer‘s judgment of its best possible move.
        """
        self.num_moves += 1
        scores = self.scores_for(b)
        move = self.max_score_column(scores)
        return move
