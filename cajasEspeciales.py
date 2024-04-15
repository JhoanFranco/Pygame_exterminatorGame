import pygame as pg

imagenes_cajasEspeciales = [
    pg.image.load("imagenes/caja_barril_explota.png"),
    pg.image.load("imagenes/caja_disparo_grande.png"),
    pg.image.load("imagenes/muro_blanco.png")
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

