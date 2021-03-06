import pygame


# Constantes
VELOCIDADE = 0.5
GRAVIDADE = 0.001
RAIO = 5
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)
LARGURA = 580
ALTURA = 620

# funcoes


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

# classes


class Option:
    def __init__(self, text, x, y):
        font_t = pygame.font.SysFont("Comic Sans MS", 15)
        self.text = text
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 150, 25)
        self.text_t = font_t.render(text, False, BRANCO)
        self.cor = AZUL

    def set_selected(self):
        """Muda a opcao para ser selecionada"""
        self.rect.width = 180
        self.cor = VERMELHO

    def print_option(self, win):
        """Printa a opcao"""
        pygame.draw.rect(win, self.cor, self.rect)
        win.blit(self.text_t, (self.x+10, self.y+3))


class Menu:
    def __init__(self, options, win):
        self.options = options
        self.win = win
        self.selected = 0

    def atualiza_selected(self, e):
        """Recebe os eventos e atualiza a opcao selecionada"""
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                self.selected -= 1
                if self.selected < 0:
                    self.selected = len(self.options) - 1
            if e.key == pygame.K_DOWN:
                self.selected += 1
                if self.selected > len(self.options) - 1:
                    self.selected = 0

    def print_win(self):
        """Printa uma tela com destaque na opcao selecionada"""
        font = pygame.font.SysFont("Comic Sans MS", 30)
        title = font.render("PyBird", False, BRANCO)
        desc = font.render("Pressione espaço para iniciar", False, BRANCO)
        options = []
        for i in range(len(self.options)):
            option = Option(self.options[i], 10, (i + 1) * 100)
            if i == self.selected:
                option.set_selected()
            options.append(option)
        self.win.fill((0, 0, 0))
        self.win.blit(title, (0, 0))
        self.win.blit(desc, (0, 50))
        for option in options:
            option.print_option(self.win)


class Bird:
    def __init__(self, x, y, velocidade_x=VELOCIDADE, velocidade_y=0, velocidade=VELOCIDADE,
                 g=GRAVIDADE, raio=RAIO, larg=LARGURA, alt=ALTURA, tecla=pygame.K_UP,
                 cor=BRANCO, score=0):
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
