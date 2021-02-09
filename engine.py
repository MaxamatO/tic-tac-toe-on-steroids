import random
from random import choice
from math import inf as infinity
import time
class State():
    """
    Main engine class used to checking valid moves, checking board, minimax algorithm. This class is mainly to get the game working.
    """
    def __init__(self):
        
        # This is a represantation of a 3x3 tic tac toe board, dot '0' means blank space
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]
        ]
        self.x_to_move = True
        self.move_logs = []
        self.sign = 1
        self.message = {1: "It is x's turn.", -1: "It is o's turn."}
        self.errors = {'place_error': "Place is already taken.", 'undo_error':"No moves to undo."}
        self.wins = {1: 'Cross wins', -1: 'Circle wins', 0: "It's a draw."}
        self.winner = ''
        self.index = None
        self.isVsAi = True
        self.HUMAN = -1
        self.COMP = 1
        self.howWon = ''


        
    def makeMove(self, pos, x_to_move, SQ_SIZE=200):
        ''' Making a move is made by changing blank space in board to either 'x' or 'o' '''
        try:
            y = pos[1]//SQ_SIZE
            x = pos[0]//SQ_SIZE
            if self.board[y][x] == 0:
                self.board[y][x] = self.HUMAN
                self.move_logs.append((y, x))
                self.changeSign()
        except:
            self.errors['place_error']

    def changeSign(self):
        ''' This fucntion is called when you have to change the player that is supposed to move. For example: after move, when undo. '''
        if self.x_to_move:
            self.sign = -1
            self.message[self.sign]
            
        else:
            self.sign = 1
            self.message[self.sign]
        self.x_to_move = not self.x_to_move

    def checkWinner(self, state):
        ''' This function is checking if someone won in any way that is below. '''
        if self.game_over(state):
            moves = self.move_logs[-1]
            x = moves[0]
            y = moves[1]
            self.winner = self.board[x][y]
            if self.checkHorizontaly(state):
                return True
            elif self.checkVerticaly(state):
                return True
            elif self.checkDiagonally(state):
                return True
            
        if len(self.move_logs) == 9:
            self.winner = 0

       
    def checkHorizontaly(self, state):
        ''' Function used for checking if someone won by checking every row. '''
        self.index = 0
        for r in state:
            if len(set(r)) == 1 and 0 not in r: # Taking a list of signs in next rows and making it a set. !! This method is used in every win-checking function. !! 
                return True
            self.index += 1

    def checkVerticaly(self, state):
        ''' Function used for checking if someone won by checking every column. ''' 
        first_col = [item[0] for item in state]
        second_col = [item[1] for item in state]
        third_col = [item[2] for item in state]

        if len(set(first_col)) == 1 and 0 not in first_col:
            
            self.index = 0
            return True
        if len(set(second_col)) == 1 and 0 not in second_col:
            
            self.index = 1
            return True
        if len(set(third_col)) == 1 and 0 not in third_col:
            
            self.index = 2
            return True

    def checkDiagonally(self, state):
        ''' Function used to check winner of diagonalls '''
        n = len(state)
        # Left to right
        l_to_r = [state[i][i] for i in range(len(state))]
        r_to_l = [state[n-1-i][i] for i in range(n)]
        
        if len(set(l_to_r)) == 1 and 0 not in l_to_r:
            self.winner = state[0][0]
            self.index = 0
            return True
        elif len(set(r_to_l)) == 1 and 0 not in r_to_l:
            self.winner = state[0][2]
            self.index = 2
            return True

    def isDraw(self, state):
        """ Function used for checking if it is a draw """
        if len(self.move_logs) == 9:
            self.winner = 'draw'
            return True
        else:
            return False
            
    def undo(self):
        """ Function used for undoing moves - bugged"""
        if len(self.move_logs) == 1:
            self.errors['undo_error']
        else:
            
            n = self.move_logs.pop()
            self.board[n[0]][n[1]] = 0
            nd = self.move_logs.pop()
            self.board[nd[0]][nd[1]] = 0
            self.winner = ''

    def canMove(self, state):
        """ Function checking if next move is possible  """
        if self.game_over(state):
            return False
        else:
            return True

    def restart(self):
        self.move_logs.clear()
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]
        ]
        self.sign = 1
        self.winner = ''
        self.x_to_move = True

    '''MiniMax part'''

    def evaluate(self, state):
        '''
        Evaluate best move based on score
        '''
        # whoWon = self.move_logs[-1] if len(self.move_logs) != 0 else (0,0)
        # player = self.board[whoWon[0]][whoWon[1]]
        if self.wins_cases(state, self.COMP):
            score = +1
        elif self.wins_cases(state, self.HUMAN):
            score = -1
        else:
            score = 0
        return score

    def ai_move(self):
        '''
        Ai makes move, if depth is 0 (blank board) it's random
        else it minimax's it
        '''
        depth = len(self.getEmptyIndexes(self.board))
        if depth == 0 or self.game_over(self.board):
            return 
        
        if depth == 9:
            x = choice([0,1,2])
            y = choice([0,1,2])
        else:
            move = self.minimax(self.board, depth, self.COMP)
            x, y = move[0], move[1]
        
        self.set_move(x, y, self.COMP) 
        
        

    def getEmptyIndexes(self, state):
        '''
        Takes a list of possible moves to make
        '''
        emptyIndexes = []
        for x, row in enumerate(state):
            for y, cell in enumerate(row):
                if cell == 0:
                    emptyIndexes.append([x, y])
        return emptyIndexes
    
    def set_move(self, x, y, player):
        '''
        Places a sign at board
        '''
        if self.valid_move(x, y):
            self.board[x][y] = player
            self.changeSign()
            self.move_logs.append((x, y))
            return True
        else:
            return False

    def valid_move(self, x, y):
        '''
        Checks if wanted move is possible
        '''
        if [x, y] in self.getEmptyIndexes(self.board):
            return True
        else:
            return False

    def wins_cases(self, state, player):
        '''
        Takes all possible wins and checks if any position wins
        '''
        win_state = [
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
        ]
        if [player, player, player] in win_state:
            
            return True
        else:
            return False

    def game_over(self, state):
        return self.wins_cases(state, self.HUMAN) or self.wins_cases(state, self.COMP)


    def minimax(self, state, depth, player):
        if player == self.COMP:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]

        if depth == 0 or self.game_over(state):
            score = self.evaluate(state)
            return [-1, -1, score]

        for cell in self.getEmptyIndexes(state):
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = self.minimax(state, depth - 1, -player)
            state[x][y] = 0
            score[0], score[1] = x, y

            if player == self.COMP:
                if score[2] > best[2]:
                    best = score
            else:
                if score[2] < best[2]:
                    best = score
        return best

