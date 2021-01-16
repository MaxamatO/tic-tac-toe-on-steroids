'''
This part of code might be used for checking valid moves, checking board, minimax algorithm
'''

class State():
    def __init__(self):
        self.board = [['.', '|', '.', '|', '.'],
                      ['-', '+', '-', '+', '-'],
                      ['.', '|', '.', '|', '.'],
                      ['-', '+', '-', '+', '-'],
                      ['.', '|', '.', '|', '.']
        ]
        self.x_to_move = True
        self.move_logs = []

    
