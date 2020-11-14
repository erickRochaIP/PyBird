import pygame


class Bird:
    def __init__(self, x, y, velocidade_x, velocidade_y, velocidade, g, raio, larg, alt, tecla, cor, score):
        self.x = x
        self.y = y
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y
        self.velocidade = velocidade
        self.g = g
        self.raio = raio
        self.larg = larg
        self.alt = alt
        self.tecla = tecla
        self.cor = cor
        self.score = score

    def atualiza_dados(self):
        """Atualiza os dados em posicao e velocidade"""
        self.velocidade_y += self.g
        keys = pygame.key.get_pressed()
        if keys[self.tecla] and self.velocidade_y > 0:
            self.velocidade_y = -self.velocidade

        self.x += self.velocidade_x
        self.y += self.velocidade_y

    def bate_parede(self):
        """Caso ele encoste em uma parede muda a direcao e retorna True"""
        flag = False
        if self.x + self.raio > self.larg:
            self.velocidade_x = -self.velocidade
            self.score += 1
            flag = True
        if self.x - self.raio < 0:
            self.velocidade_x = self.velocidade
            self.score += 1
            flag = True
        return flag

    def bate_teto_chao(self):
        """Caso ele encoste no teto ou no chao reinicia a posicao e retorna True"""
        flag = False
        if self.y + self.raio > self.alt:
            self.reinicia()
            flag = True
        if self.y - self.raio < 0:
            self.reinicia()
            flag = True
        return flag

    def reinicia(self):
        """Reinicia os dados em posicao e velocidade"""
        self.velocidade_x, self.velocidade_y = self.velocidade, 0
        self.x, self.y = 50, 50
        self.score = 0


def printa_bird(win, bird):
    """Usa os dados de bird para printar na tela"""
    cor = bird.cor
    x = bird.x
    y = bird.y
    raio = bird.raio
    pygame.draw.circle(win, cor, (int(x), int(y)), raio, 0)


def render_score(font, bird):
    """Retorna texto com a cor de bird"""
    return font.render(str(bird.score), False, bird.cor)


def print_scores(textsurfaces, win):
    """Recebe uma lista de scores e printa na tela"""
    i = 0
    for text in textsurfaces:
        win.blit(text, (i, 0))
        i += 50

# Constantes
VELOCIDADE = 0.5
GRAVIDADE = 0.001
RAIO = 5
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
LARGURA = 580
ALTURA = 620


def main_menu():
    pygame.init()

    velocidade_x, velocidade_y, x, y = 0.5, 0, 50, 50
    bird_r = Bird(50, 50, VELOCIDADE, 0, VELOCIDADE, GRAVIDADE, RAIO, LARGURA, ALTURA, pygame.K_w, VERMELHO, 0)
    bird_b = Bird(50, 50, VELOCIDADE, 0, VELOCIDADE, 0.002, 10, LARGURA, ALTURA, pygame.K_UP, AZUL, 0)
    birds = [bird_r, bird_b]
    game(birds)


def game(birds):

    win = pygame.display.set_mode((LARGURA, ALTURA), 0)
    font = pygame.font.SysFont("Comic Sans MS", 30)
    while True:
        textsurfaces = []
        for bird in birds:
            bird.atualiza_dados()
            bird.bate_parede()
            bird.bate_teto_chao()
            textsurfaces.append(render_score(font, bird))
        # trata bird_r
        win.fill((0, 0, 0))
        for bird in birds:
            printa_bird(win, bird)
        print_scores(textsurfaces, win)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()


main_menu()