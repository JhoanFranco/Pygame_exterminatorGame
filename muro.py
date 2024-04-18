import pygame as pg
from  main import VERDE, ANCHO, ALTO
from controladorSonido import ControladorSonido 


imagenes_Muro = [
    pg.image.load("imagenes/muro_blanco.png")
]

imagenes_cajasEspeciales = [
    pg.image.load("imagenes/caja_barril_explota.png"),
    pg.image.load("imagenes/caja_disparo_grande.png"),
    pg.image.load("imagenes/muro_blanco.png")
]

imagenes_efectosJuego = [pg.image.load("imagenes/explosion_barril.png")] 

class Muro(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(imagenes_Muro[0],(40,40))
        self.rect = self.image.get_rect()

        ## las posiciones X y Y
        self.rect.bottom = y + 30 # queremos que el alto lo pongan instanciando la clase
        self.rect.centerx = x +40 # se quiere que la posiscion x la pongan instanciando la clase
        self.radius = 8  # radio

        # contador colicion Bala con el muro  
        self.contadorDeVidaMuro = 120
        # pg.draw.circle(self.image, ROJO,self.rect.center,self.radius,10)
        
    def update(self):
        # SE PUEDE MEJPRARA CON EL CONTADOR BALA MURO_ PARA LA ELIMINACION CON LAS BALAS Y LA ELIMIACION CON LOS ENEMIGOS
        if self.contadorDeVidaMuro <= 0:
            self.kill()
               
    def ElminiarVariosMuros(self, spritesBalas, spritesMuros):
        # la funcion solo se llama cuando las balas van a romper los mueros
        pg.sprite.groupcollide(spritesBalas,spritesMuros,False,True, pg.sprite.collide_circle) # colision_balas_muro 

    def golpeMuro(self, golpeVida):
        self.contadorDeVidaMuro -= golpeVida 


class MuroExplosivo(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image =  pg.transform.scale(imagenes_cajasEspeciales[0],(40,40))
        self.rect = self.image.get_rect()
        # queremos que el alto lo pongan instanciando la clase
        self.rect.bottom = y 
        # se quiere que la posiscion x la pongan instanciando la clase
        self.rect.centerx = x 
        # radio
        self.radius = 8 
        # pg.draw.circle(self.image, ROJO,self.rect.center,self.radius,10)
        self.sonido_explosion = pg.mixer.Sound("musica/sonido-de-explosion-con-escombros.mp3")
    
    def update(self, pantalla, sprites_muros_explosivos, sprites_enemigos,  es_volumen_nulo=False):
        ## controlador de sonido importacion
        from main import controladorSonido 

        self.image =  pg.transform.scale(imagenes_efectosJuego[0],(300,300))
        self.rect.x -= 100
        self.rect.y -= 70
        self.radius = 70
        # tenemos que dibujarlos aqui porque si no la funcion de colicionar no funciona al no actualizar el dibujo
        sprites_muros_explosivos.draw(pantalla)
        # como tuve que mover la imagen para que se viera bien
        # ahora hay que arreglar la colision  el lugar para que coja bien
        self.rect.x += 110
        self.rect.y += 110
        pg.draw.circle(self.image, VERDE,self.rect.center,self.radius,5)
        #buscamos los sprites que le esten pegando al muro

        #sonido
        if controladorSonido.es_volumen_nulo == False:
            self.sonidoExplosion_barrilExplota(controladorSonido)

        for sprite_muroExplosivo in sprites_muros_explosivos:
                colicion_muroExplosivo_enemigo = pg.sprite.spritecollide(sprite_muroExplosivo,sprites_enemigos,True,pg.sprite.collide_circle)
            # la colicion es sin radio para que coja todo el sprite
            

    def sonidoExplosion_barrilExplota(self, controladorS:ControladorSonido):
        self.sonido_explosion.set_volume(controladorS.volumen_actual)
        self.sonido_explosion.play()
