import pygame
pygame.init()

WIDTH = 850
HEIGHT = 1000

pygame.display.set_caption("shapes")
screen=pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("orange")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.draw.rect(screen,"green",(150,250,550,550))
    pygame.draw.rect(screen,"blue",(200,350,150,150))
    pygame.draw.rect(screen,"blue",(500,350,150,150))
    pygame.draw.rect(screen,"yellow",(350,550,150,250))
    pygame.draw.circle(screen,"red",(380,655),10)
    pygame.draw.polygon(screen,"red",[(150,250),(425,0),(700,250)])

    pygame.display.update()