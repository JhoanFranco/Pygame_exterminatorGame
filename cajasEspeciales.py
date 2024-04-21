import pygame as pg
from variablesMain import ANCHO, ALTO
import random

imagenes_cajasEspeciales = [
    pg.image.load("imagenes/cajasEspeciales/caja_barril_explota.png"),
    pg.image.load("imagenes/cajasEspeciales/caja_disparo_grande.png"),
    pg.image.load("imagenes/cajasEspeciales/muro_blanco.png"),
    pg.image.load("imagenes/cajasEspeciales/caja_vida.png")
]


class CajasEspeciales(pg.sprite.Sprite):
    def __init__(self, numeroSprite):
        super().__init__()
        self.image= pg.transform.scale(imagenes_cajasEspeciales[numeroSprite], (30,30))
        self.rect = self.image.get_rect()
        # posicion 
        self.rect.y = 300
        self.rect.x = 400
        self.radius = 8

        # frames cajaEspecial
        self.numeroCaja = numeroSprite
        self.frameCajaEspecial = 0
        

    def update(self):
        # global bool_activacionDisparo_Grande
        # global bool_barril_explota
            # control_sprites
        if self.frameCajaEspecial >= 2:  # son 5 sprites 
            self.frameCajaEspecial = 0
            self.image= pg.transform.scale(imagenes_cajasEspeciales[self.numeroCaja], (30,30))
            # cambiar imagen solo de correr
        self.image = pg.transform.scale(imagenes_cajasEspeciales[self.numeroCaja], (40,40))
        self.frameCajaEspecial += 1
    
    def eliminarCaja(self):
        self.kill()

    def cambiarPosicionRandom(self):
        # Elegir un valor aleatorio para la coordenida y dentro del rango [0, ALTO)
        y = random.randint(100, ALTO - 100)
        x = random.randint(100, ANCHO - 100)
        self.rect.y = y
        self.rect.x = x 
        


