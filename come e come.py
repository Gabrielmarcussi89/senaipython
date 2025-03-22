import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Come-Come (Snake Game)")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Tamanho do bloco
block_size = 20

# Velocidade inicial da cobra
snake_speed = 10

# Relógio para controlar a velocidade do jogo
clock = pygame.time.Clock()

# Fonte para exibir a pontuação
font = pygame.font.Font(None, 36)

# Função para exibir a pontuação na tela
def mostrar_pontuacao(pontuacao):
    texto = font.render(f"Pontuação: {pontuacao}", True, WHITE)
    screen.blit(texto, (10, 10))

# Função principal do jogo
def main():
    # Posição inicial da cobra
    snake = [[100, 50], [90, 50], [80, 50]]
    snake_direction = "RIGHT"  # Direção inicial

    # Posição inicial da comida
    comida_pos = [random.randrange(1, screen_width // block_size) * block_size,
                  random.randrange(1, screen_height // block_size) * block_size]
    comida_spawn = True

    pontuacao = 0
    velocidade = snake_speed  # Velocidade inicial

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != "DOWN":
                    snake_direction = "UP"
                elif event.key == pygame.K_DOWN and snake_direction != "UP":
                    snake_direction = "DOWN"
                elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                    snake_direction = "LEFT"
                elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                    snake_direction = "RIGHT"

        # Movimentação da cobra
        if snake_direction == "UP":
            nova_cabeca = [snake[0][0], snake[0][1] - block_size]
        elif snake_direction == "DOWN":
            nova_cabeca = [snake[0][0], snake[0][1] + block_size]
        elif snake_direction == "LEFT":
            nova_cabeca = [snake[0][0] - block_size, snake[0][1]]
        elif snake_direction == "RIGHT":
            nova_cabeca = [snake[0][0] + block_size, snake[0][1]]

        # Insere a nova cabeça na cobra
        snake.insert(0, nova_cabeca)

        # Verifica se a cobra comeu a comida
        if snake[0] == comida_pos:
            pontuacao += 1
            comida_spawn = False
            # Aumenta a velocidade a cada 5 pontos
            if pontuacao % 5 == 0:
                velocidade += 2
        else:
            # Remove a cauda da cobra se não comeu a comida
            snake.pop()

        # Gera nova comida se necessário
        if not comida_spawn:
            comida_pos = [random.randrange(1, screen_width // block_size) * block_size,
                          random.randrange(1, screen_height // block_size) * block_size]
            comida_spawn = True

        # Verifica colisões
        # Colisão com as paredes
        if (snake[0][0] >= screen_width or snake[0][0] < 0 or
                snake[0][1] >= screen_height or snake[0][1] < 0):
            running = False
        # Colisão com o próprio corpo
        for bloco in snake[1:]:
            if snake[0] == bloco:
                running = False

        # Renderiza a tela
        screen.fill(BLACK)

        # Desenha a cobra
        for bloco in snake:
            pygame.draw.rect(screen, GREEN, pygame.Rect(bloco[0], bloco[1], block_size, block_size))

        # Desenha a comida
        pygame.draw.rect(screen, RED, pygame.Rect(comida_pos[0], comida_pos[1], block_size, block_size))

        # Exibe a pontuação
        mostrar_pontuacao(pontuacao)

        # Atualiza a tela
        pygame.display.flip()

        # Controla a velocidade da cobra
        clock.tick(velocidade)

    pygame.quit()

if __name__ == "__main__":
    main()
