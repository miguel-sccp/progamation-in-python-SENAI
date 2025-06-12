import pygame

pygame.init()
tamanho = 500, 500
janela = pygame.display.set_mode(tamanho)
pygame.display.set_caption('jogo pin-poing')

# cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# variáveis
raquete_x, raquete_y = 50, 225
raquete2_x, raquete2_y = 430, 225  # Corrigido para não sair da tela

ball_x, ball_y = 250, 250

velocidade_bola_x = 2
velocidade_bola_y = 2
velocidade_raquete = 5

largura_raquete = 20
altura_raquete = 100

bola_largura = 20
bola_altura = 20

placar1 = 0
placar2 = 0
font = pygame.font.Font(None, 55)

def desenhar():
    janela.fill(branco)
    pygame.draw.rect(janela, preto, (raquete_x, raquete_y, largura_raquete, altura_raquete))
    pygame.draw.rect(janela, preto, (raquete2_x, raquete2_y, largura_raquete, altura_raquete))
    pygame.draw.ellipse(janela, preto, (ball_x, ball_y, bola_largura, bola_altura))
    placar_texto = font.render(f"{placar1} - {placar2}", True, preto)
    janela.blit(placar_texto, (200, 10))
    pygame.display.flip()

Loop = True
clock = pygame.time.Clock()

while Loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Loop = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and raquete_y > 0:
        raquete_y -= velocidade_raquete
    if keys[pygame.K_s] and raquete_y < 500 - altura_raquete:
        raquete_y += velocidade_raquete
    if keys[pygame.K_UP] and raquete2_y > 0:
        raquete2_y -= velocidade_raquete
    if keys[pygame.K_DOWN] and raquete2_y < 500 - altura_raquete:
        raquete2_y += velocidade_raquete

    ball_x += velocidade_bola_x
    ball_y += velocidade_bola_y

    # Colisão com as paredes superior/inferior
    if ball_y <= 0 or ball_y >= 500 - bola_altura:
        velocidade_bola_y = -velocidade_bola_y

    # Colisão com as raquetes
    if (raquete_x < ball_x < raquete_x + largura_raquete) and (raquete_y < ball_y < raquete_y + altura_raquete):
        velocidade_bola_x = -velocidade_bola_x
    if (raquete2_x < ball_x + bola_largura < raquete2_x + largura_raquete) and (raquete2_y < ball_y < raquete2_y + altura_raquete):
        velocidade_bola_x = -velocidade_bola_x

    # Pontuação
    if ball_x <= 0:
        placar2 += 1
        ball_x, ball_y = 250, 250
    if ball_x >= 500 - bola_largura:
        placar1 += 1
        ball_x, ball_y = 250, 250

    desenhar()
    clock.tick(60)

pygame.quit()

        