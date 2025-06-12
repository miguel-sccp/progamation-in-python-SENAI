# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()


# Definição do tamanho da tela
largura, altura = 400, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Labirinto")

# Definição das cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# listas para o labirinto
tamanho_celula = 40
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1]
]

# Posição inicial do jogador
x, y = 1 * tamanho_celula, 1 * tamanho_celula
# Velocidade do jogador
velocidade = 40

# criar uma função para desenhar o labirinto
def desenhar_labirinto():
     #ler labirinto
    for linha in range(len(labirinto)):
        # desenhar cada linha do labirinto
        for coluna in range(len(labirinto[linha])):
            # Verifica se o usario pode passar ou não
            cor = preto if labirinto[linha][coluna] == 1 else branco
            #desenhar o retangulo do labirinto
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))

# Loop principal do jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
# Manipulação das teclas
    teclas = pygame.key.get_pressed()
    #o pressinar da direcional esquerdo
    if teclas[pygame.K_LEFT]:
        novo_x = x - velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    #o pressinar da direcional direito
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    #o pressinar da direcional cima
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    #o pressinar da direcional baixo
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y


    # Preenche a tela com a cor branca
    tela.fill(branco)

    # Desenha o labirinto e o jogador
    desenhar_labirinto()
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))

    # Atualiza a tela
    pygame.display.flip()

# Controla a taxa de atualização do jogo
    pygame.time.Clock().tick(30)

# Encerra o Pygame
pygame.quit()
