import pygame
import sys
import os
import ctypes


pygame.init()
font = pygame.font.SysFont('Arial', 40)
black = 0, 0, 0

user32 = ctypes.windll.user32
size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
# size = width, height = 1080, 720
fps = 60
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
objects = []


class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])

            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


def myFunction():
    print('Button Pressed')


customButton = Button(30, 30, 400, 100, 'Button One (onePress)', myFunction)
customButton = Button(
    30, 140, 400, 100, 'Button Two (multiPress)', myFunction, True)


if __name__ == "__main__":

    while 1:
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for object in objects:
            object.process()

        pygame.display.flip()
        fpsClock.tick(fps)
