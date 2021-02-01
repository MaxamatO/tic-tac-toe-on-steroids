import random
from random import choice
from math import inf as infinity
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
        self.wins = {1: 'Cross wins', -1: 'Circle wins', 'draw': "It's a draw."}
        self.winner = ''
        self.index = None
        self.isVsAi = True
        
    def makeMove(self, pos, x_to_move, SQ_SIZE=200):
        ''' Making a move is made by changing blank space in board to either 'x' or 'o' '''
        
        try:
            if x_to_move and self.isVsAi:
                row = pos[1]
                col = pos[0]
                if self.board[row][col] == 0:
                    self.board[row][col] = self.sign
                    self.move_logs.append((row, col))
                    self.changeSign()
                else:
                    self.makeMove(pos, SQ_SIZE, x_to_move)
            else:
                row = pos[1]//SQ_SIZE
                col = pos[0]//SQ_SIZE
                if self.board[row][col] == 0:
                    self.board[row][col] = self.sign
                    self.move_logs.append((row, col))
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

    def checkWinner(self):
        ''' This function is checking if someone won in any way that is below. '''
        whoWon = self.move_logs[-1] if len(self.move_logs) != 0 else None
        if self.checkHorizontaly():
            self.winner = self.board[whoWon[0]][whoWon[1]]
            return True
        elif self.checkVerticaly():
            self.winner = self.board[whoWon[0]][whoWon[1]]
            return True
        elif self.checkDiagonally():
            self.winner = self.board[whoWon[0]][whoWon[1]]
            return True
        elif self.isDraw():
            return True
            
    def checkHorizontaly(self):
        ''' Function used for checking if someone won by checking every row. '''
        self.index = 0
        for r in self.board:
            if len(set(r)) == 1 and 0 not in r: # Taking a list of signs in next rows and making it a set. !! This method is used in every win-checking function. !! 
                return True
            self.index += 1

    def checkVerticaly(self):
        ''' Function used for checking if someone won by checking every column. ''' 
        first_col = [item[0] for item in self.board]
        second_col = [item[1] for item in self.board]
        third_col = [item[2] for item in self.board]

        if len(set(first_col)) == 1 and 0 not in first_col:
            self.winner = self.board[0][0]
            self.index = 0
            return True
        if len(set(second_col)) == 1 and 0 not in second_col:
            self.winner = self.board[0][1]
            self.index = 1
            return True
        if len(set(third_col)) == 1 and 0 not in third_col:
            self.winner = self.board[0][2]
            self.index = 2
            return True

    def checkDiagonally(self):
        ''' Function used to check winner of diagonalls '''
        n = len(self.board)
        # Left to right
        l_to_r = [self.board[i][i] for i in range(len(self.board))]
        r_to_l = [self.board[n-1-i][i] for i in range(n)]
        
        if len(set(l_to_r)) == 1 and 0 not in l_to_r:
            self.winner = self.board[0][0]
            self.index = 0
            return True
        elif len(set(r_to_l)) == 1 and 0 not in r_to_l:
            self.winner = self.board[0][2]
            self.index = 2
            return True

    def isDraw(self):
        """ Function used for checking if it is a draw """
        if len(self.move_logs) == 9:
            self.winner = 'draw'
            return True
        else:
            return False
            
    def undo(self):
        """ Function used for undoing moves """
        if len(self.move_logs) == 0:
            self.errors['undo_error']
        else:
            # n = len(self.move_logs)-1
            n = self.move_logs.pop()
            self.board[n[0]][n[1]] = 0
            print(self.move_logs)
            
            self.changeSign()

    def canMove(self):
        """ Function checking if next move is possible  """
        if self.checkWinner():
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
        self.x_to_move = True


class MiniMax(State):
    HUMAN = -1
    COMP = 1
    def __init__(self):
        super().__init__()
        self.current_board = self.board
        self.depth = 3
        self.emptyIndexes = self.getEmptyIndexes(self.current_board)


        

    def evaluate(self, state):
        whoWon = self.move_logs[-1] if len(self.move_logs) != 0 else None
        player = self.board[whoWon[0]][whoWon[1]]
        if self.checkWinner() and player == self.COMP:
            score = +1
        elif self.checkWinner() and player == self.HUMAN:
            score = -1
        else:
            score = 0
        return score

    def ai_move(self):
        depth = len(self.getEmptyIndexes(self.current_board))
        if depth == 0 or self.checkWinner():
            return 
        
        if depth == 9:
            x = choice([0,1,2])
            y = choice([0,1,2])
        else:
            move = self.minimax(self.current_board, depth, self.COMP)
            x, y = move[0], move[1]
        
        self.makeMove((x, y), True)

    def getEmptyIndexes(self, board):
        emptyIndexes = []
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[c][r] == 0:
                    emptyIndexes.append([r, c])
        return emptyIndexes
    

    def minimax(self, state, depth, player):
        if player == self.COMP:
            best = [-1, -1, -infinity]
        else:
            best = [-1, -1, +infinity]

        if depth == 0 or self.checkWinner():
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


