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
BRANCO = (255, 255, 255)
LARGURA = 580
ALTURA = 620


def print_win(win, selected, options):
    """Recebe opcoes de menu e printa uma tela com destaque na opcao selecionada"""
    font = pygame.font.SysFont("Comic Sans MS", 30)
    title = font.render("PyBird", False, BRANCO)
    desc = font.render("Pressione espaço para iniciar", False, BRANCO)
    rects = []
    for i in range(len(options)):
        rect = pygame.Rect(10, (i+1)*100, 125, 25)
        if i == selected:
            rect.width = 150
        rects.append(rect)
    texts = []
    for option in options:
        font_t = pygame.font.SysFont("Comic Sans MS", 15)
        text_t = font_t.render(option, False, BRANCO)
        texts.append(text_t)
    win.fill((0, 0, 0))
    win.blit(title, (0, 0))
    win.blit(desc, (0, 50))
    for rect in rects:
        if rect.width == 150:
            pygame.draw.rect(win, VERMELHO, rect)
        else:
            pygame.draw.rect(win, AZUL, rect)
    for i in range(len(texts)):
        win.blit(texts[i], (20, ((i+1)*100+3)))

def main_menu():
    pygame.init()
    win = pygame.display.set_mode((LARGURA, ALTURA), 0)
    velocidade_x, velocidade_y, x, y = 0.5, 0, 50, 50
    options = ["Um jogador", "Dois jogadores"]
    selected = 0
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    selected -= 1
                    if selected < 0:
                        selected = len(options) - 1
                if e.key == pygame.K_DOWN:
                    selected += 1
                    if selected > len(options) - 1:
                        selected = 0
                if e.key == pygame.K_SPACE:
                    running = False

        print_win(win, selected, options)
        pygame.display.update()

    birds = []
    if selected == 0:
        birds.append(Bird(x, y, VELOCIDADE, 0, VELOCIDADE, GRAVIDADE, RAIO, LARGURA, ALTURA, pygame.K_w, VERMELHO, 0))
    elif selected == 1:
        birds.append(Bird(x, y, VELOCIDADE, 0, VELOCIDADE, GRAVIDADE, RAIO, LARGURA, ALTURA, pygame.K_UP, AZUL, 0))
        birds.append(Bird(x, y, VELOCIDADE, 0, VELOCIDADE, GRAVIDADE, RAIO, LARGURA, ALTURA, pygame.K_w, VERMELHO, 0))
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