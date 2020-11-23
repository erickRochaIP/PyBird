from utils import *


def main_menu():
    pygame.init()
    win = pygame.display.set_mode((LARGURA, ALTURA), 0)
    velocidade_x, velocidade_y, x, y = 0.5, 0, 50, 50
    tela_menu = Menu(["Um jogador", "Dois jogadores", "Tres Jogadores", "Quatro Jogadores"], win)
    running = True
    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            tela_menu.atualiza_selected(e)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    running = False

        tela_menu.print_win()
        pygame.display.update()

    birds = [Bird(x, y, cor=VERMELHO, tecla=pygame.K_q)]
    if tela_menu.selected >= 1:
        birds.append(Bird(x+10, y, cor=AZUL, tecla=pygame.K_w))
    if tela_menu.selected >= 2:
        birds.append(Bird(x+20, y, cor=BRANCO, tecla=pygame.K_e))
    if tela_menu.selected >= 3:
        birds.append(Bird(x+30, y, cor=AMARELO, tecla=pygame.K_r))

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
