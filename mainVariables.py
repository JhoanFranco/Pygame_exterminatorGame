import pygame as pg
# from menu import menuPrincipal
from claseControladorSonido import ControladorSonido

# Tamaño pantalla
ANCHO, ALTO = 1000, 600
FPS = 10

# PALETA DE COLORES RGB()
NEGRO = (0,0,0)
BLANCO = (255,255,255)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)

pg.init()
es_volumen_nulo = False
pantalla = pg.display.set_mode((ANCHO, ALTO))
# pg.display.set_caption("JUEGO EXTERMINADOR")

# Falta poner icono
clock = pg.time.Clock()

es_volumen_nulo = False

# creacion de controlador de sonido 
controladorSonido =  ControladorSonido()


