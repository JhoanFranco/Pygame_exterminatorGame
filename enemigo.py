import pygame as pg
import random
from main import ANCHO,ALTO, VERDE
from controladorSonido import ControladorSonido 

imagenes_zombieVerde_correrDerecha = [ 
    pg.image.load("imagenes/zombies/zombies_verde_der_1.png"),
    pg.image.load("imagenes/zombies/zombies_verde_der_2.png"),
    pg.image.load("imagenes/zombies/zombies_verde_der_3.png"),
    pg.image.load("imagenes/zombies/zombies_verde_der_4.png"),
    pg.image.load("imagenes/zombies/zombies_verde_der_5.png") 
]

imagenes_zombieVerde_morderDerecha = [ 
    pg.image.load("imagenes/zombies/zombies_verde_morder_1.png"),
    pg.image.load("imagenes/zombies/zombies_verde_morder_2.png"),
]

imagenes_zombieMorado_correrIzquierda = [
    pg.image.load("imagenes/zombies/zombies_morado_izq_1.png"),
    pg.image.load("imagenes/zombies/zombies_morado_izq_2.png"),
    pg.image.load("imagenes/zombies/zombies_morado_izq_3.png"),
    pg.image.load("imagenes/zombies/zombies_morado_izq_4.png"),
    pg.image.load("imagenes/zombies/zombies_morado_izq_5.png")
]

imagenes_zombieMorado_morderIzquierda = [
    pg.image.load("imagenes/zombies/zombies_morado_izq_morder_1.png"),
    pg.image.load("imagenes/zombies/zombies_morado_izq_morder_2.png")
]


class Enemigos_verdes(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() # heredar de la clase Sprite
        self.image = pg.transform.scale(pg.image.load("imagenes/exterminador/Gunner_Blue_Idle_1.png"),(100,50))
        self.rect = self.image.get_rect() 

        # poner una radio para coliciones mas precisas
        self.radius = 27 # tiene que ser radius
        pg.draw.circle(self.image, VERDE,self.rect.center,self.radius,5) # dibujamos ese radio

        # posicion aleatoria respecto a la pantalla
        self.rect.x = random.randint(0,ANCHO/2)  #para que solo puedan aparecer desde el margen izquierdo hasta la mitad
        self.rect.y = random.randrange(0,ALTO)

        # velocidad del personaje(inicial)
        self.velocidad_x = 4
        self.velocidad_y = 4

        # contar Frames
        self.framesEnemigo_corriendo = 0 #contar los frames del enemigo corriendo
        self.framesEnemigo_mordiendo = 0 #contar los frames del enemigo mordiendo 

        #booleno Saber si esta mordiendo 
        self.estarMordiendo = False

        # sonido Mordida
        self.sonido_mordida =  pg.mixer.Sound("musica/mordida.mp3")

        # vida del enemigo
        self.vidaEnemigo = 4

    def update(self):
        # importar el controlador de sonido para saber que poner 
        from main import controladorSonido
        es_volumen_nulo = controladorSonido.es_volumen_nulo


        self.rect.y += self.velocidad_x
        self.rect.x += self.velocidad_y

        if self.estarMordiendo:
            self.cambioImagenMordida()
            print("zombie verde volumen nulo: " + f"{es_volumen_nulo}")
            # si el volumen_nulo es igual a false 
            if es_volumen_nulo ==  False: 
                self.sonidoMordida(controladorSonido) # aqui ya cambia el volumen y hace el play 
            else:
                pass 
            self.cambiarEstadoEstarMordiendo(False)
        else:   
            # control_sprites
            if self.framesEnemigo_corriendo >= 5:  # son 5 sprites 
                self.framesEnemigo_corriendo = 0
            # cambiar imagen
            self.image = pg.transform.scale((imagenes_zombieVerde_correrDerecha[self.framesEnemigo_corriendo]), (50,60))
            self.framesEnemigo_corriendo += 1

        ## Limites o margenes
        # margen derecho
        if self.rect.right > ANCHO:
            self.rect.left = 0
        # margen abajo
        if self.rect.bottom > ALTO:
            self.rect.top = 0
        # margen arriba
        if self.rect.top < 0:
            self.rect.bottom = ALTO
        # no hay izquierdo porque estos enemigos solo se mueven en posicion(positiva)

    # si no tiene vida, borrar sprite
        if self.vidaEnemigo <=0:
            self.kill()    

         
    def sonidoMordida(self, controlador:ControladorSonido): 
        self.sonido_mordida.set_volume(controlador.volumen_actual)
        self.sonido_mordida.play()

    def cambioImagenMordida(self):
        # control_sprites
        if self.framesEnemigo_mordiendo >= 2:  # son 2 sprites 
            self.framesEnemigo_mordiendo = 0

        self.image = pg.transform.scale((imagenes_zombieVerde_morderDerecha[self.framesEnemigo_mordiendo]), (50,60))
        self.framesEnemigo_mordiendo += 1
    
    def cambiarEstadoEstarMordiendo(self, value:bool):
        self.estarMordiendo = value

    def quitarVida(self, dano:int):
        self.vidaEnemigo -= dano


    


class Enemigos_morado(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() # heredar de la clase Sprite
        self.image = pg.transform.scale(pg.image.load("imagenes/exterminador/Gunner_Blue_Idle_1.png"),(100,50))
        self.rect = self.image.get_rect() 

        # poner una radio para coliciones mas precisas
        self.radius = 27 # tiene que ser radius
        pg.draw.circle(self.image, VERDE,self.rect.center,self.radius,5) # dibujamos ese radio

        # posicion aleatoria respecto a la pantalla
        self.rect.x = random.randint(0,ANCHO/2)
        self.rect.y = random.randrange(0,ALTO)

        # velocidad del personaje(inicial)
        self.velocidad_x = 5
        self.velocidad_y = 5

        # contar Frames
        self.framesEnemigo_corriendo = 0 #contar los frames del enemigo corriendo
        self.framesEnemigo_mordiendo = 0 #contar los frames del enemigo mordiendo 

        #booleno Saber si esta mordiendo 
        self.estarMordiendo = False
        # poner musica
        self.sonido_mordida =  pg.mixer.Sound("musica/mordida.mp3")

        # vida del enemigo
        self.vidaEnemigo = 4

    def update(self):
        # importar el controlador de sonido para saber que poner 
        from main import controladorSonido
        es_volumen_nulo = controladorSonido.es_volumen_nulo

        self.rect.y -= self.velocidad_x
        self.rect.x -= self.velocidad_y

        if self.estarMordiendo:
            self.cambioImagenMordida()
            # si el volumen_nulo es igual a false 
            if es_volumen_nulo ==  False: 
                self.sonidoMordida(controladorSonido)
            else:
                pass 
            self.cambiarEstadoEstarMordiendo(False)
        else:   
            # control_sprites
            if self.framesEnemigo_corriendo >= 5:  # son 5 sprites 
                self.framesEnemigo_corriendo = 0
            # cambiar imagen solo de correr
            self.image = pg.transform.scale((imagenes_zombieMorado_correrIzquierda[self.framesEnemigo_corriendo]), (50,60))
            self.framesEnemigo_corriendo += 1

        ## Limites o maregnes
        # margen derecho
        if self.rect.right > ANCHO:
            self.rect.left = 0
        # margen izquierdo
        if self.rect.left < 0:
            self.rect.right = ANCHO
        # margen abajo
        if self.rect.bottom > ALTO:
            self.rect.top = 0
        # margen arriba
        if self.rect.top < 0:
            self.rect.bottom = ALTO

        # si no tiene vida, borrar sprite
        if self.vidaEnemigo <=0:
            self.kill()    


    def sonidoMordida(self, controlador:ControladorSonido): 
        self.sonido_mordida.set_volume(controlador.volumen_actual)
        self.sonido_mordida.play()

    def cambioImagenMordida(self):
        # control_sprites
        if self.framesEnemigo_mordiendo >= 2:  # son 2 sprites 
            self.framesEnemigo_mordiendo = 0

        self.image = pg.transform.scale((imagenes_zombieMorado_morderIzquierda[self.framesEnemigo_mordiendo]), (50,60))
        self.framesEnemigo_mordiendo += 1
    
    def cambiarEstadoEstarMordiendo(self, value:bool):
        self.estarMordiendo = value

    def quitarVida(self, dano:int):
        self.vidaEnemigo -= dano
    
