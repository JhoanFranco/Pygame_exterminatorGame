import pygame as pg
from main import ANCHO, ALTO

imagenes_barraVida = [
    pg.image.load("imagenes/barra_vida/barraVida_1.png"),
    pg.image.load("imagenes/barra_vida/barraVida_2.png"),
    pg.image.load("imagenes/barra_vida/barraVida_3.png"),
    pg.image.load("imagenes/barra_vida/barraVida_4.png"),
    pg.image.load("imagenes/barra_vida/barraVida_5.png"),
    pg.image.load("imagenes/barra_vida/barraVida_6.png")
]

class BarraVida(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(imagenes_barraVida[0],(100,100))
        
        # posicion 
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO -100
        self.rect.y = 15

        # contadorVida
        self.contadorVida = 51


    def update(self):
        if self.contadorVida >= 1 and  self.contadorVida < 11 :
           self.image = pg.transform.scale(imagenes_barraVida[1],(100,100))
        elif self.contadorVida >= 11 and  self.contadorVida < 21:
           self.image = pg.transform.scale(imagenes_barraVida[2],(100,100))
        elif self.contadorVida >= 21 and self.contadorVida < 31:
           self.image = pg.transform.scale(imagenes_barraVida[3],(100,100))
        elif self.contadorVida >= 31 and self.contadorVida  < 41:
           self.image = pg.transform.scale(imagenes_barraVida[4],(100,100)) 
        elif self.contadorVida  >= 41 and self.contadorVida < 51 :
           self.image = pg.transform.scale(imagenes_barraVida[5],(100,100)) 
        else:
           self.image = pg.transform.scale(imagenes_barraVida[0],(100,100)) 
    
    def quitarVida(self, danoGolpe:int):
       self.contadorVida -= danoGolpe
        