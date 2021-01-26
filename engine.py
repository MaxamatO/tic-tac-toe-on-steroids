
class State():
    """
    Main engine class used to checking valid moves, checking board, minimax algorithm. This class is mainly to get the game working.
    """
    def __init__(self):
        
        # This is a represantation of a 3x3 tic tac toe board, dot '.' means blank space
        self.board = [['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.']
        ]
        self.x_to_move = True
        self.move_logs = []
        self.sign = 'x'
        self.message = {'x': "It is x's turn.", 'o': "It is o's turn."}
        self.errors = {'place_error': "Place is already taken.", 'undo_error':"No moves to undo."}
        self.wins = {'x': 'Cross wins', 'o': 'Circle wins', 'draw': "It's a draw."}
        self.winner = ''
        self.index = None

        
    def makeMove(self, pos, SQ_SIZE):
        ''' Making a move is made by changing blank space in board to either 'x' or 'o' '''
        row = pos[1]//SQ_SIZE
        col = pos[0]//SQ_SIZE
        try:
            if self.board[row][col] == '.':
                self.board[row][col] = self.sign
                self.move_logs.append((row, col))
                self.changeSign()
        except:
            self.errors['place_error']

    def changeSign(self):
        ''' This fucntion is called when you have to change the player that is supposed to move. For example: after move, when undo. '''
        if self.sign == 'x':
            self.sign = 'o'
            self.message[self.sign]
        else:
            self.sign = 'x'
            self.message[self.sign]
        self.message[self.sign]
        self.x_to_move = not self.x_to_move

    def checkWinner(self):
        ''' This function is checking if someone won in any way that is below. '''
        if self.checkHorizontaly():
            return True
        elif self.checkVerticaly():
            return True
        elif self.checkDiagonally():
            return True
        elif self.isDraw():
            return True
            
    def checkHorizontaly(self):
        ''' Function used for checking if someone won by checking every row. '''
        self.index = 0
        for r in self.board:
            if len(set(r)) == 1 and '.' not in r: # Taking a list of signs in next rows and making it a set. !! This method is used in every win-checking function. !! 
                self.winner = r[0]
                return True
            self.index += 1

    def checkVerticaly(self):
        ''' Function used for checking if someone won by checking every column. ''' 
        first_col = [item[0] for item in self.board]
        second_col = [item[1] for item in self.board]
        third_col = [item[2] for item in self.board]

        if len(set(first_col)) == 1 and '.' not in first_col:
            self.winner = self.board[0][0]
            self.index = 0
            return True
        if len(set(second_col)) == 1 and '.' not in second_col:
            self.winner = self.board[0][1]
            self.index = 1
            return True
        if len(set(third_col)) == 1 and '.' not in third_col:
            self.winner = self.board[0][2]
            self.index = 2
            return True

    def checkDiagonally(self):
        ''' Function used to check winner of diagonalls '''
        n = len(self.board)
        # Left to right
        l_to_r = [self.board[i][i] for i in range(len(self.board))]
        r_to_l = [self.board[n-1-i][i] for i in range(n)]
        
        if len(set(l_to_r)) == 1 and '.' not in l_to_r:
            self.winner = self.board[0][0]
            self.index = 0
            return True
        elif len(set(r_to_l)) == 1 and '.' not in r_to_l:
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
            self.board[n[0]][n[1]] = '.'
            self.x_to_move = not self.x_to_move
            

    def canMove(self):
        """ Function checking if next move is possible  """
        if self.checkWinner():
            return False
        else:
            return True

    def restart(self):
        self.move_logs.clear()
        self.board = [['.', '.', '.'],
                      ['.', '.', '.'],
                      ['.', '.', '.']
        ]

        