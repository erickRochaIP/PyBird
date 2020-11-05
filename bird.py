import pygame


def restart():
    return 0.5, 0, 50, 50


# Constantes
VELOCIDADE = 0.5
GRAVIDADE = 0.001
RAIO = 5
COR = (255, 0, 0)
AZUL = (0, 0, 255)
LARGURA = 580
ALTURA = 620

pygame.init()
win = pygame.display.set_mode((LARGURA, ALTURA), 0)
font = pygame.font.SysFont("Comic Sans MS", 30)

velocidade_x, velocidade_y, x, y = 0.5, 0, 50, 50
score = 0

pygame.draw.circle(win, COR, (x, y), RAIO, 0)
#pygame.draw.circle(win, AZUL, (50, 50), RAIO, 0)
pygame.display.update()


def restart():
    pass


while True:

    velocidade_y += GRAVIDADE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and velocidade_y > 0:
        velocidade_y = -VELOCIDADE

    x += velocidade_x
    y += velocidade_y

    if x + RAIO > LARGURA:
        velocidade_x = -VELOCIDADE
        score += 1
    if x - RAIO < 0:
        velocidade_x = VELOCIDADE
        score += 1
    if y + RAIO > ALTURA:
        velocidade_x, velocidade_y, x, y = 0.5, 0, 50, 50
        score = 0
    if y - RAIO < 0:
        velocidade_x, velocidade_y, x, y = 0.5, 0, 50, 50
        score = 0

    textsurface = font.render(str(score), False, AZUL)
    win.fill((0, 0, 0))
    pygame.draw.circle(win, COR, (int(x), int(y)), RAIO, 0)
    win.blit(textsurface, (0,0))
    #pygame.draw.circle(win, AZUL, (50, 50), RAIO, 0)
    pygame.display.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
