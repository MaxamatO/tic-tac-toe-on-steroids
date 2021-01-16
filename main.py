'''
This file is responsible to take user input, draw things, display board etc.
'''

import pygame
# Might use it later
# import engine 

WIDTH, HEIGHT = 600,700
DIMENSIONS = 3
SQ_SIZE = (WIDTH) // DIMENSIONS
FPS = 20
white, black = (255, 255, 255), (0, 0, 0)

IMGS = {}

# x_img = pygame.transform.scale(pygame.image.load('imgs/X.jpg'), (SQ_SIZE, SQ_SIZE))  
# o_img = pygame.image.load('imgs/o.svg')

gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))



'''
Dsiplaying 3x3 grid for tic tac toe + additional space for messages
'''
def loadImgs():
    IMGS['x'] = pygame.transform.scale(pygame.image.load('imgs/X.jpg'), (SQ_SIZE, SQ_SIZE))


def displayBoard():
    # Vertical lines
    pygame.draw.line(gameDisplay, black, (SQ_SIZE, 0), (SQ_SIZE, HEIGHT-100), 5)
    pygame.draw.line(gameDisplay, black, (2*SQ_SIZE, 0), (2*SQ_SIZE, HEIGHT-100), 5)

    # Horizontal lines
    pygame.draw.line(gameDisplay, black, (0, SQ_SIZE), (WIDTH, SQ_SIZE), 5)
    pygame.draw.line(gameDisplay, black, (0, 2*SQ_SIZE), (WIDTH, 2*SQ_SIZE), 5)

    # drawin message box
    pygame.draw.rect(gameDisplay, black, (0, 600, WIDTH, 100))

def changeSign():
    pass

def makeMove(pos):
    gameDisplay.blit(IMGS['x'], (pos[0], pos[1]))

def main():
    running = True
    clock = pygame.time.Clock()
    gameDisplay.fill(white)
    loadImgs()
    while running:
        pygame.init()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                makeMove(pos)
                # col = (pos[0])//SQ_SIZE
                # row = (pos[1])//SQ_SIZE
                
        displayBoard()
        
        clock.tick(FPS)
        pygame.display.flip()




if __name__ == "__main__":
    main()
