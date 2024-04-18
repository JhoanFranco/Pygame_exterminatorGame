import pygame as pg 

imagen_sonido_bajar = pg.image.load("imagenes/sonido/bajar_volumen.png")
imagen_sonido_subir= pg.image.load("imagenes/sonido/subir_volumen.png")
imagen_sonido_maximo = pg.image.load("imagenes/sonido/maximo_volumen.png")
imagen_sonido_nulo = pg.image.load("imagenes/sonido/silenciar_volumen.png")


class ControladorSonido(pg.sprite.Sprite):
    def __init__(self):
        self.volumen_actual = 0
        self.es_volumen_nulo = False

    def update(self, pantalla:pg.display):


        keys = pg.key.get_pressed() #Opción tecla pulsada

        #CONTROL DE SONIDO
        self.volumen_actual = pg.mixer.music.get_volume()

        #saber si el volumen es nulo 
        if self.volumen_actual == 0.0:
            self.es_volumen_nulo = True
        else:
            self.es_volumen_nulo = False
        
        #baja volumen
        if keys[pg.K_1] and self.volumen_actual > 0.0: # 0.0 volumen nulo
            pg.mixer.music.set_volume(self.volumen_actual - 0.1) # para colocar o cambiar el volumen
            imagen = pg.transform.scale(imagen_sonido_bajar,(100,50))
            pantalla.blit(imagen, (10,70))
        elif keys[pg.K_1] and self.volumen_actual == 0.0:
            imagen = pg.transform.scale(imagen_sonido_bajar,(100,50))
            pantalla.blit(imagen, (10,70))
        
        #sube volumen
        if keys[pg.K_2] and self.volumen_actual < 1.0: # 1.0 maximo volumen
            pg.mixer.music.set_volume(self.volumen_actual + 0.1)
            imagen = pg.transform.scale(imagen_sonido_subir,(100,50))
            pantalla.blit(imagen,(10,70))
        elif keys[pg.K_2] and self.volumen_actual == 0.0 or (keys[pg.K_2] and self.volumen_actual == 1.0):
            imagen = pg.transform.scale(imagen_sonido_subir,(100,50))
            pantalla.blit(imagen,(10,70))
        # volumen nulo
        elif keys[pg.K_3]:
            pg.mixer.music.set_volume(0.0)
            imagen = pg.transform.scale(imagen_sonido_nulo,(100,50))
            pantalla.blit(imagen,(10,70))

        # volumen maximo
        elif keys[pg.K_4]:
            pg.mixer.music.set_volume(1.0)
            imagen = pg.transform.scale(imagen_sonido_maximo,(100,50))
            pantalla.blit(imagen,(10,70))
    
    def configurarVolumenSonidosDeacuerdoAControlador(self):
        pg.mixer.music.set_volume(self.volumen_actual)
            