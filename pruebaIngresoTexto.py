import pygame
import sys

pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ingreso de texto")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuente
font = pygame.font.Font(None, 32)

# Texto ingresado por el usuario
input_text = ''
MAX_LETTERS = 10  # Límite de letras

while True:
    screen.fill(WHITE)
    
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print("Texto ingresado:", input_text)
                input_text = ''
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif len(input_text) < MAX_LETTERS:
                input_text += event.unicode
    
    # Renderizar texto ingresado en la pantalla
    text_surface = font.render(input_text, True, BLACK)
    screen.blit(text_surface, (10, 10))
    
    # Renderizar guión debajo del texto
    remaining_letters = MAX_LETTERS - len(input_text)
    if remaining_letters > 0:
        underscore_text = '-' * remaining_letters
        underscore_surface = font.render(underscore_text, True, BLACK)
        screen.blit(underscore_surface, (10, 40))
    
    pygame.display.flip()
