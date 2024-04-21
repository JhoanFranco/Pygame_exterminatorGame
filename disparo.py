import pygame as pg
from variablesMain import ANCHO,ALTO

imagenes_disparosGrandes =[ 
    pg.image.load("imagenes/disparo_grande/disparo_grande_derecha.png"),
    pg.image.load("imagenes/disparo_grande/disparo_grande_izquierda.png"),
    pg.image.load("imagenes/disparo_grande/disparo_grande_arriba.png"),
    pg.image.load("imagenes/disparo_grande/disparo_grande_abajo.png")
]

imagenes_disparosNormal = [
    pg.image.load("imagenes/disparo_der_izq.png"),

]

class DisparosDerecha(pg.sprite.Sprite):
    def __init__(self, x, y): # al inicializar un objeto de clase se pide la posicion(x, y)
        super().__init__()
        self.image = pg.transform.scale(imagenes_disparosNormal[0],(10,20))
        self.rect = self.image.get_rect()
        self.rect.y = y - 17 # se quiere que la posicion de Y se ponga instanciando la clase
        self.rect.right = x # se quiere que la posicion de X se ponga instanciando la clase

    def update(self):
        # Velocidad de la bala
        self.rect.x += 25 
        #print(self.rect.left) # llega hasta 1020 entonces si borra la bala
        if self.rect.left >= ANCHO:
            self.kill()

    def cambiarDisparoGrande(self):
        self.image = pg.transform.scale(imagenes_disparosGrandes[0],(110,50))


class DisparosIzquierda(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(imagenes_disparosNormal[0],(10,20)) 
        self.rect = self.image.get_rect()
        self.rect.y = y - 17 
        self.rect.left = x 

    def update(self):
        # Velocidad de la bala
        self.rect.x -= 25 
        if self.rect.left <= 0:
            self.kill()
    
    def cambiarDisparoGrande(self):
        self.image = pg.transform.scale(imagenes_disparosGrandes[1],(110,50))



class DisparosAbajo(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(imagenes_disparosNormal[0],(10,20)) 
        self.rect = self.image.get_rect()
        self.rect.y = y 
        self.rect.x = x -5

    def update(self):
        # velocidad de la bala
        self.rect.y += 25
        if self.rect.bottom >= ALTO:
            self.kill()

    def cambiarDisparoGrande(self):
        self.image = pg.transform.scale(imagenes_disparosGrandes[3],(50,110))
            


class DisparosArriba(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(imagenes_disparosNormal[0],(10,20)) 
        self.rect = self.image.get_rect()
        self.rect.y = y 
        self.rect.x = x-3
    
    def update(self):
        self.rect.y -= 25

        if self.rect.top <= 0:
            self.kill()
    
    def cambiarDisparoGrande(self):
        self.image = pg.transform.scale(imagenes_disparosGrandes[2],(50,110))
            

