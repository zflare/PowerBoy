import pygame, sys
from pygame import mixer
# Setup Window
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Power Boy Bar')
screen = pygame.display.set_mode((800, 600),0,32)
 
font = pygame.font.SysFont(None, 20)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False

# Background Sound
mixer.music.load('PowerBoy\8BIT_Crossing Field_LiSA_SAO_shrtvs.ogg')
mixer.music.play(-1)

def main_menu():
    while True:
        # Background
        menuBg = pygame.image.load('PowerBoy\PowerBoyMainMenu.png')

        # Text on Main Menu
        titleFont = pygame.font.Font('freesansbold.ttf', 64)
        titleText = titleFont.render('Power Boy', True, (225, 225, 255))
        startFont = pygame.font.Font('freesansbold.ttf', 40)
        startText = startFont.render('Start', True, (225, 225, 255))
        quitFont = pygame.font.Font('freesansbold.ttf', 40)
        quitText = startFont.render('Quit', True, (225, 225, 255))

        screen.blit(menuBg, (0,0))
        screen.blit(titleText, (225, 175))
        startButton = screen.blit(startText, (350, 300))
        quitButton = screen.blit(quitText, (350, 375)) 
        
        mouseX, mouseY = pygame.mouse.get_pos()

        if startButton.collidepoint((mouseX, mouseY)):
            if click:
                pygame.mixer.music.stop()
                game()
        if quitButton.collidepoint((mouseX, mouseY)):
            if click:
                pygame.mixer.music.stop()
                quitMenu()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        mainClock.tick(60)


def game():
    running = True
    while running:
        screen.fill((0,0,0))

        draw_text("Game", font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
       
        pygame.display.update()
        mainClock.tick(60)


def quitMenu():
    pygame.quit()
    sys.exit()


main_menu()