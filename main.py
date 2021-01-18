'''
This file is responsible to take user input, draw things, display board etc.
'''
'''
 TODO In this app: add MiniMax algorithm, check for winner,
    display messages, create choice about type of game (PvP, PvPC),
    ask for another game at the end, Best Of 3, undo move.
'''


import pygame
import engine 
from pygame import freetype

# Initialize pygame dir
pygame.init()

# Define const parameters of our game 
WIDTH, HEIGHT = 600,700
DIMENSIONS = 3 # Number of cells used in bot x and y axis
SQ_SIZE = (WIDTH) // DIMENSIONS # Size of a single square (here 200x200)
FPS = 20
white, black = (255, 255, 255), (0, 0, 0)
IMGS = {}
GAME_FONT = pygame.freetype.SysFont("arial", 20) 
eng = engine.State()
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))


def loadImgs():
    '''
    Load images
    '''
    IMGS['x'] = pygame.transform.scale(pygame.image.load('imgs/X.jpg'), (SQ_SIZE, SQ_SIZE))
    IMGS['o'] = pygame.transform.scale(pygame.image.load('imgs/o.svg'), (SQ_SIZE, SQ_SIZE))

def displayBoard():
    '''
    Displaying 3x3 grid for tic tac toe + additional space for messages \n
    Display signs at board
    '''
    # Loop through 2D array with board to check for any sign placements
    for r in range(len(eng.board)):
        for c in range(len(eng.board[r])):
            if eng.board[c][r] != '.': 
                gameDisplay.blit(IMGS[eng.board[c][r]], (r*SQ_SIZE, c*SQ_SIZE))

    # Vertical lines
    pygame.draw.line(gameDisplay, black, (SQ_SIZE, 0), (SQ_SIZE, HEIGHT-100), 5)
    pygame.draw.line(gameDisplay, black, (2*SQ_SIZE, 0), (2*SQ_SIZE, HEIGHT-100), 5)

    # Horizontal lines
    pygame.draw.line(gameDisplay, black, (0, SQ_SIZE), (WIDTH, SQ_SIZE), 5)
    pygame.draw.line(gameDisplay, black, (0, 2*SQ_SIZE), (WIDTH, 2*SQ_SIZE), 5)

    # Draw message box
    pygame.draw.rect(gameDisplay, black, (0, 600, WIDTH, 100))

    # Display message taken from engine --
    text_surface, rect = GAME_FONT.render("Hello world!", (0,0,0))

def main():
    '''
    Main function used to run the whole program
    '''

    running = True
    clock = pygame.time.Clock()
    gameDisplay.fill(white)
    loadImgs()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                eng.makeMove(pos, SQ_SIZE)
        displayBoard()
        clock.tick(FPS)
        pygame.display.flip()


# Starting program
if __name__ == "__main__":
    main()
