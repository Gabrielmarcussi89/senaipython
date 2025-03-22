import random
import pygame
import os

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cacheta - Jogo de Cartas")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonte
font = pygame.font.Font(None, 36)

# Baralho
valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
naipes = ["ouros", "espadas", "copas", "paus"]
baralho = [f"{valor}_{naipe}" for valor in valores for naipe in naipes] * 2  # Dois baralhos

# Pasta das imagens das cartas
pasta_cartas = "cartas"

# Função para carregar as imagens das cartas
def carregar_imagens_cartas():
    imagens = {}
    for carta in baralho:
        caminho = os.path.join(pasta_cartas, f"{carta}.png")
        if os.path.exists(caminho):
            imagens[carta] = pygame.image.load(caminho)
    # Carrega a imagem da carta virada para baixo
    caminho_fundo = os.path.join(pasta_cartas, "fundo.png")
    if os.path.exists(caminho_fundo):
        imagens["fundo"] = pygame.image.load(caminho_fundo)
    return imagens

# Função para carregar a imagem de fundo do cassino
def carregar_fundo_cassino():
    caminho_fundo = os.path.join("imagens", "fundo_cassino.jpg")
    if os.path.exists(caminho_fundo):
        return pygame.image.load(caminho_fundo)
    return None

# Função para embaralhar o baralho
def embaralhar_baralho():
    random.shuffle(baralho)
    return baralho

# Função para verificar se o jogador venceu
def verificar_vitoria(mao):
    contador = {}
    for carta in mao:
        valor = carta.split("_")[0]  # Pega o valor da carta (ex: "2_ouros" -> "2")
        if valor in contador:
            contador[valor] += 1
        else:
            contador[valor] = 1
    # Verifica se há 9 ou 10 cartas do mesmo valor
    for valor, qtd in contador.items():
        if qtd >= 9:
            return True
    return False

# Função principal do jogo
def main():
    baralho_embaralhado = embaralhar_baralho()
    imagens_cartas = carregar_imagens_cartas()
    fundo_cassino = carregar_fundo_cassino()

    # Verifica se as imagens foram carregadas corretamente
    if not fundo_cassino:
        print("Erro: Imagem de fundo do cassino não encontrada!")
        return
    if "fundo" not in imagens_cartas:
        print("Erro: Imagem de fundo da carta não encontrada!")
        return

    # Distribui 9 cartas para cada jogador
    mao_jogador = [baralho_embaralhado.pop() for _ in range(9)]
    mao_adversario = [baralho_embaralhado.pop() for _ in range(9)]

    monte = baralho_embaralhado  # Cartas restantes no monte
    descarte = []  # Cartas descartadas na mesa
    vez_jogador = True  # True = jogador, False = adversário

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if vez_jogador:
                    if event.key == pygame.K_m:  # Pega do monte
                        if monte:
                            carta_comprada = monte.pop()
                            mao_jogador.append(carta_comprada)
                            print(f"Você comprou: {carta_comprada}")
                            # Descarta uma carta
                            if len(mao_jogador) > 9:
                                carta_descartada = mao_jogador.pop()
                                descarte.append(carta_descartada)
                                print(f"Você descartou: {carta_descartada}")
                            vez_jogador = False
                    elif event.key == pygame.K_d:  # Pega do descarte
                        if descarte:
                            carta_comprada = descarte.pop()
                            mao_jogador.append(carta_comprada)
                            print(f"Você pegou do descarte: {carta_comprada}")
                            # Descarta uma carta
                            if len(mao_jogador) > 9:
                                carta_descartada = mao_jogador.pop()
                                descarte.append(carta_descartada)
                                print(f"Você descartou: {carta_descartada}")
                            vez_jogador = False

        # Verifica se o jogador venceu
        if verificar_vitoria(mao_jogador):
            print("Você venceu! Batida mole ou dura!")
            running = False

        # Turno do adversário (simples)
        if not vez_jogador and monte:
            carta_comprada = monte.pop()
            mao_adversario.append(carta_comprada)
            print(f"Adversário comprou: {carta_comprada}")
            # Descarta uma carta
            if len(mao_adversario) > 9:
                carta_descartada = mao_adversario.pop()
                descarte.append(carta_descartada)
                print(f"Adversário descartou: {carta_descartada}")
            vez_jogador = True

        # Verifica se o adversário venceu
        if verificar_vitoria(mao_adversario):
            print("Adversário venceu! Batida mole ou dura!")
            running = False

        # Renderiza a tela
        screen.blit(fundo_cassino, (0, 0))  # Fundo do cassino

        # Desenha a mão do jogador
        for i, carta in enumerate(mao_jogador):
            if carta in imagens_cartas:
                screen.blit(imagens_cartas[carta], (50 + i * 100, 600))

        # Desenha o monte (carta virada para baixo)
        if monte:
            screen.blit(imagens_cartas["fundo"], (50, 400))

        # Desenha o descarte (última carta descartada virada para cima)
        if descarte:
            screen.blit(imagens_cartas[descarte[-1]], (200, 400))

        # Exibe instruções
        texto_instrucao = font.render("Pressione M para comprar do monte ou D para pegar do descarte", True, WHITE)
        screen.blit(texto_instrucao, (50, 50))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

