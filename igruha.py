import pygame 
import time 
clock = pygame.time.Clock()


window = pygame.display.set_mode((735, 517))
pygame.display.set_caption("igruha")
icon = pygame.image.load("images\icon.png")

pygame.display.set_icon(icon)

background = pygame.image.load("images\background.png")

Dino_w = [
    pygame.image.load("images\dino_1.png"),
    pygame.image.load("images\dino_2.png"),
    pygame.image.load("images\dino_3png"),
    pygame.image.load("images\dino_4.png"),
    pygame.image.load("images\dino_5.png"),
    pygame.image.load("images\dino_6.png"),
    pygame.image.load("images\dino_7.png"),
]


Dino_w_count = 0

background_2 = 0

background_sound = pygame.mixer.Sound("sound\background_sound.mp3")
background_sound.play()



game = True 
while game:

    window.blit(background, (0,0))
    window.blit(background_2 + 735,  0)
    window.blit(Dino_w[Dino_w_count], (300, 300))

    if Dino_w_count == 3:
        Dino_w_count = 0
    else:
        Dino_w_count += 1

    background_2 -= 2
    if background_2 == -735:
        background_2 = 0

    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    pygame.draw.rect(window, (255,0,0), (100,100,100,100))
    
    pygame.display.update()

clock.tick(10)