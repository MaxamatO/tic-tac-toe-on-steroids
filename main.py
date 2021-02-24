'''
This file is responsible to take user input, draw things, display board etc.
'''
'''
 TODO In this app: Best Of 3.
'''

import sys
import pygame
import engine 
from pygame import freetype

# Initialize pygame dir
pygame.init()

# Define constant parameters of our game 
WIDTH, HEIGHT = 600,700
DIMENSIONS = 3 # Number of cells used in both x and y axis
SQ_SIZE = (WIDTH) // DIMENSIONS # Size of a single square (here 200x200)
FPS = 20
white, black, red = (255, 255, 255), (0, 0, 0), (255,0,0)
IMGS = {} 
GAME_FONT = pygame.freetype.SysFont("arial", 32) 
LARGE_FONT = pygame.freetype.SysFont("arial", 60)
eng = engine.State()
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))

class Btn():
    def __init__(self):
        self.width = WIDTH
        self.height = 200
        self.color = (145,145,145,150)
        self.yes_surface, self.y_rect= GAME_FONT.render("Yes",  (white))
        self.no_surface, self.n_rect = GAME_FONT.render("No",  (white))
        self.ai_surface, self.a_rect= GAME_FONT.render("Player vs Ai",  (white))
        self.hum_surface, self.h_rect = GAME_FONT.render("Player vs Player",  (white))
        


    def askForType(self):
        '''
        Asking player wheter he wants to play PvsP or PvsAi
        '''
        text_surface, rect = GAME_FONT.render("Choose a type of a game: ", (white))

        see_through = pygame.Surface((self.width, self.height)).convert_alpha()
        see_through.fill(self.color)
        see_through_rect = see_through.get_rect(midleft=(0, 300))

        gameDisplay.blit(see_through, see_through_rect)
        gameDisplay.blit(text_surface, (110, 250))
        gameDisplay.blit(self.ai_surface, (95, 310))
        gameDisplay.blit(self.hum_surface, (330, 310))

    def askForRestart(self):
        """
        Create pop up ending rectangle 
        """
        text_surface, rect = GAME_FONT.render("Do you want to restart?: ", (white))

        see_through = pygame.Surface((self.width, self.height)).convert_alpha()
        see_through.fill(self.color)
        see_through_rect = see_through.get_rect(midleft=(0, 300))

        gameDisplay.blit(see_through, see_through_rect)
        gameDisplay.blit(text_surface, (150, 250))
        gameDisplay.blit(self.yes_surface, (250, 310))
        gameDisplay.blit(self.no_surface, (350, 310))

    def yesNo_restart(self, pos):
        """
        Taking user input and determining if he wants to restart
        """
        if pos[0] in range(250, 305) and pos[1] in range(310, 335):
            eng.restart()
            main()
        elif pos[0] in range(350, 390) and pos[1] in range(310, 335):
            sys.exit()

    def choose_type(self,pos):
        if pos[0] in range(95, 260) and pos[1] in range(310, 335):
            eng.type = 1
            pygame.display.set_caption('Tic Tac Toe - Ai version')
            return True
        elif pos[0] in range(330, 560) and pos[1] in range(310, 335):
            eng.type = -1
            pygame.display.set_caption('Tic Tac Toe - Human version')
            return True
    

def loadImgs():
    '''
    Loads images
    '''
    IMGS[1] = pygame.transform.scale(pygame.image.load('imgs/X.jpg'), (SQ_SIZE, SQ_SIZE))
    IMGS[-1] = pygame.transform.scale(pygame.image.load('imgs/o.svg'), (SQ_SIZE, SQ_SIZE))

def displayMessages():
    """
    Displays errors, messages, winners at the bottom of the screen
    """
 
    # Display message taken from engine --
    if eng.winner != '':
        text_surface, rect  = GAME_FONT.render(eng.wins[eng.winner], (white))
        # drawWinnerLine()
        button.askForRestart()
    else:
        text_surface, rect = GAME_FONT.render(eng.message[eng.sign], (white))
    gameDisplay.blit(text_surface, (220, 640))

def drawWinnerLine():
    """
    Have no idea how to do it yet 
    """
    if eng.checkWinner(eng.board):
        if eng.checkHorizontaly(eng.board):
            pygame.draw.line(gameDisplay, red, (0, (SQ_SIZE*eng.index)+100), (WIDTH, (SQ_SIZE*eng.index)+100), 6)
            
        elif eng.checkVerticaly(eng.board):
            pygame.draw.line(gameDisplay, red, ((SQ_SIZE*eng.index)+100, 0), ((SQ_SIZE*eng.index)+100, HEIGHT-100), 6)
            
        elif eng.checkDiagonally(eng.board):
            if eng.index == 0:
                pygame.draw.line(gameDisplay, red, (SQ_SIZE*eng.index, 0), (WIDTH, HEIGHT-100), 6)
                
            elif eng.index == 2:
                pygame.draw.line(gameDisplay, red, (WIDTH, 0), (0, HEIGHT-100), 6)
                
        
def displayBoard():
    '''
    Displaying 3x3 grid for tic tac toe + additional space for messages \n
    Display signs at board
    '''
    # Loop through 2D array with board to check for any sign placements
    for r in range(len(eng.board)):
        for c in range(len(eng.board[r])):
            if eng.board[c][r] != 0: 
                gameDisplay.blit(IMGS[eng.board[c][r]], (r*SQ_SIZE, c*SQ_SIZE))
            else:
                pygame.draw.rect(gameDisplay, white,[SQ_SIZE*r, SQ_SIZE*c, SQ_SIZE, SQ_SIZE])

    # Draw Vertical lines
    pygame.draw.line(gameDisplay, black, (SQ_SIZE, 0), (SQ_SIZE, HEIGHT-100), 5)
    pygame.draw.line(gameDisplay, black, (2*SQ_SIZE, 0), (2*SQ_SIZE, HEIGHT-100), 5)

    # Draw Horizontal lines
    pygame.draw.line(gameDisplay, black, (0, SQ_SIZE), (WIDTH, SQ_SIZE), 5)
    pygame.draw.line(gameDisplay, black, (0, 2*SQ_SIZE), (WIDTH, 2*SQ_SIZE), 5)

    # Draw message box
    pygame.draw.rect(gameDisplay, black, (0, 600, WIDTH, 100))

    # Draw score box
    pygame.draw.line(gameDisplay, black, (3*SQ_SIZE, 0), (3*SQ_SIZE, HEIGHT), 2)
    


def state():
    """
    Display current game state
    """
    
    displayBoard()
    displayMessages()

def intro():
    running = True
    gameDisplay.fill(white)
    clock = pygame.time.Clock()
    state()
    button.askForType()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if button.choose_type(pos):
                    running = False
        pygame.display.update()
        clock.tick(FPS)

def main():
    '''
    Main function used to run the whole program
    '''
    
    if eng.type == '':
        intro()
    running = True
    clock = pygame.time.Clock()
    gameDisplay.fill(white)
    loadImgs()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                pos = pygame.mouse.get_pos()
                if event.button == 1:
                    if eng.canMove(eng.board): 
                        eng.makeMove(pos, eng.x_to_move)
                    if eng.winner != '':
                        button.yesNo_restart(pos)
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_z:
                    eng.undo()
                    gameDisplay.fill(white)
        if eng.type == 1 and eng.x_to_move:
                eng.ai_move()
        if eng.checkWinner(eng.board):
                drawWinnerLine()
        state()
        pygame.display.update()
        clock.tick(FPS)


# Starting program
if __name__ == "__main__":
    button = Btn()
    main()
    