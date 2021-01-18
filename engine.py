'''
This part of code might be used for checking valid moves, checking board, minimax algorithm
'''

class State():
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
        self.errors = {'place_error': "Place is already taken."}

    def makeMove(self, pos, SQ_SIZE):
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
        if self.sign == 'x':
            self.sign = 'o'
        else:
            self.sign = 'x'
        self.message[self.sign]
        self.x_to_move = not self.x_to_move

    


        


    
