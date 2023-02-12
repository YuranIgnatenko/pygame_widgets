import pygame_widgets as pw
import pygame

pygame.init()

screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption('Tutorial 1')
screen.fill((255,255,255))
pygame.display.flip()

running = True

def draw():
    wgt1 = pw.Histogram(screen, 300,100,200,50,(200,40,10),(50,100,0),35)

    b = pw.ButtonPick(screen,"btn",0,0,0)

    wgt = pw.Button(screen,"abcd",0,0,0,0,100,40,(200,40,10),(0,0,0),(29,160,140), lambda:print(123))
    wgt.wait()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    draw()
    pygame.display.flip()
    pygame.display.update()
    
