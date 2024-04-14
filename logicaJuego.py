import random
import pygame as pg
import time 
import sys

# Tamaño pantalla
ANCHO, ALTO = 1000, 600
# FPS
FPS = 10

# PALETA DE COLORES RGB()
NEGRO = (0,0,0)
BLANCO = (255,255,255)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)

# imagenes para el juego
fondo = pg.transform.scale(pg.image.load("imagenes/fondo_cuidad_final.png"), (ANCHO,ALTO))

imagenes_exterminador_quieto = [pg.image.load("imagenes/exterminador/Gunner_Blue_Idle_1.png")     
         ]

imagenes_exterminador_correrDerecha = [pg.image.load("imagenes/exterminador/Gunner_Blue_Run_1.png"),
                  pg.image.load("imagenes/exterminador/Gunner_Blue_Run_2.png"),
                  pg.image.load("imagenes/exterminador/Gunner_Blue_Run_3.png"),
                  pg.image.load("imagenes/exterminador/Gunner_Blue_Run_4.png"),
                  pg.image.load("imagenes/exterminador/Gunner_Blue_Run_5.png"),
                  pg.image.load("imagenes/exterminador/Gunner_Blue_Run_6.png")
                 ]

imagenes_exterminador_correrIzquierda = [pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_1.png"),
                    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_2.png"),
                    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_3.png"),
                    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_4.png"),
                    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_5.png"),
                    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_6.png")
                    ]

imagenes_exterminador_correrArriba = [pg.image.load("imagenes/exterminador/Gunner_Blue_arriba_1.png"),
        pg.image.load("imagenes/exterminador/Gunner_Blue_arriba_2.png"),
        pg.image.load("imagenes/exterminador/Gunner_Blue_arriba_3.png")
        ]

imagenes_exterminador_correrAbajo = [pg.image.load("imagenes/exterminador/Gunner_Blue_abajo_1.png"),
             pg.image.load("imagenes/exterminador/Gunner_Blue_abajo_2.png"),
             pg.image.load("imagenes/exterminador/Gunner_Blue_abajo_3.png")
            ]

imagenes_barraVida = [pg.image.load("imagenes/barra_vida/barraVida_1.png"),
             pg.image.load("imagenes/barra_vida/barraVida_2.png"),
             pg.image.load("imagenes/barra_vida/barraVida_3.png"),
             pg.image.load("imagenes/barra_vida/barraVida_4.png"),
             pg.image.load("imagenes/barra_vida/barraVida_5.png"),
             pg.image.load("imagenes/barra_vida/barraVida_6.png")
            ]

imagenes_cajasEspeciales = [pg.image.load("imagenes/caja_barril_explota.png"),
                    pg.image.load("imagenes/caja_disparo_grande.png"),
                    pg.image.load("imagenes/muro_blanco.png")
                    ]

imagenes_disparosGrandes =[ pg.image.load("imagenes/disparo_grande/disparo_grande_derecha.png"),
                    pg.image.load("imagenes/disparo_grande/disparo_grande_izquierda.png"),
                    pg.image.load("imagenes/disparo_grande/disparo_grande_arriba.png"),
                    pg.image.load("imagenes/disparo_grande/disparo_grande_abajo.png")
                ]

imagenes_efectosJuego = [pg.image.load("imagenes/explosion_barril.png")] 

imagenes_zombieVerde_correrDerecha = [ pg.image.load("imagenes/zombies/zombies_verde_der_1.png"),
               pg.image.load("imagenes/zombies/zombies_verde_der_2.png"),
               pg.image.load("imagenes/zombies/zombies_verde_der_3.png"),
               pg.image.load("imagenes/zombies/zombies_verde_der_4.png"),
               pg.image.load("imagenes/zombies/zombies_verde_der_5.png") 
            ]

imagenes_zombieVerde_morderDerecha = [ pg.image.load("imagenes/zombies/zombies_verde_morder_1.png"),
                  pg.image.load("imagenes/zombies/zombies_verde_morder_2.png"),
                ]

imagenes_zombieMorado_CorrerDerecha = [ pg.image.load("imagenes/zombies/zombies_morado_der_1.png"),
                  pg.image.load("imagenes/zombies/zombies_morado_der_2.png"),
                  pg.image.load("imagenes/zombies/zombies_morado_der_3.png"),
                  pg.image.load("imagenes/zombies/zombies_morado_der_4.png"),
                  pg.image.load("imagenes/zombies/zombies_morado_der_5.png")
                ]

imagenes_zombieMorado_MorderDerecha = [pg.image.load("imagenes/zombies/zombies_morado_der_morder_1.png"),
                            pg.image.load("imagenes/zombies/zombies_morado_der_morder_2.png")
                            ]

imagenes_zombieMorado_correrIzquierda = [pg.image.load("imagenes/zombies/zombies_morado_izq_1.png"),
                    pg.image.load("imagenes/zombies/zombies_morado_izq_2.png"),
                    pg.image.load("imagenes/zombies/zombies_morado_izq_3.png"),
                    pg.image.load("imagenes/zombies/zombies_morado_izq_4.png"),
                    pg.image.load("imagenes/zombies/zombies_morado_izq_5.png")
                    ]

imagenes_zombieMorado_morderIzquierda = [pg.image.load("imagenes/zombies/zombies_morado_izq_morder_1.png"),
                            pg.image.load("imagenes/zombies/zombies_morado_izq_morder_2.png")
                            ]


imagen_sonido_bajar = pg.image.load("imagenes/sonido/bajar_volumen.png")
imagen_sonido_subir= pg.image.load("imagenes/sonido/subir_volumen.png")
imagen_sonido_maximo = pg.image.load("imagenes/sonido/maximo_volumen.png")
imagen_sonido_nulo = pg.image.load("imagenes/sonido/silenciar_volumen.png")

#VARIABLES GLOBALES PARA EL FUNCIONAMIENTO DEL JUEGO 

# variables direccion
movimientoExterminador_izquierda = False
movimientoExterminador_derecha = False
movimientoExterminador_arriba = False
movimientoExterminador_abajo = False

#Variables para contar los frames
contadorFrames_exterminador_arriba = 0
contadorFrames_exterminador_DerIzq = 0
contadorFrames_exterminador_abajo = 0

# contadores para las coliciones
contador_bala_muro = 0
contador_enemigo_muro =0

#Variables boleanas para los cubos (premios)
bool_disparo_grande = False
bool_barril_explota = False

# contador para los objetos premios
contador_balas_disparoGrande = 3
contador_barril_explota = 3
contador_muros = 5

# contadores boleanos para saber si poner musica
bool_musica_mordida_zombie_verde = False
bool_musica_mordida_zombie_morado = False
    # No hay necesidad de una variable para la musica del barril ya que cuando lo actualizamos se elimina el sprite
bool_musica_dolor_jugador = False

# variable para saber si el jugador se mueve
moviendose = False

# mirar si el volumen es nulo
es_volumen_nulo = False

#Podemos que cuando presiona una tecla disparos grandes se posiciona
#Si se queda sin balas bool_disparos_grande = False

class Jugador(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() # heredar de la sub_clase Sprite
        self.image = pg.transform.scale(pg.image.load("imagenes/exterminador/Gunner_Blue_Idle_1.png"),(100,50))
        self.rect = self.image.get_rect() # obtener el rectangulo del sprite, es decir, de la imagen.  ojo get_rect crea un rectangulo con esa imagen
        # poner un radio para hacer las coliciones mas precisas
        self.radius = 27 # tiene que ser radius
        # centrar el jugador al centro de la pantalla
        self.rect.center = (ANCHO//2, ALTO//2)
        # velocidad del personaje(inicial) <var para dar la velocidad al personaje>
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.sonido_disparo = pg.mixer.Sound("musica/disparo.mp3")
        self.sonido_dolor = pg.mixer.Sound("musica/dolor_jugador.mp3")

    def update(self): # hereda de la clase sprite Update
        # llamar las variables a utilizar
        global movimientoExterminador_izquierda
        global movimientoExterminador_derecha
        global movimientoExterminador_arriba
        global movimientoExterminador_abajo

        global contadorFrames_exterminador_abajo
        global contadorFrames_exterminador_DerIzq
        global contadorFrames_exterminador_arriba

        global bool_disparo_grande
        global bool_barril_explota

        global contador_barril_explota
        global contador_muros

        global EstaDisparando
        global bool_musica_dolor_jugador
        global moviendose
        

        # Restablecer el indice del sprite cuando se termine de hacer la animaciòn
        # como hay seis frames para izq y derecha entonces los (contadorFrames_exterminador_DerIzq) sirve para la los frames de derecha y movimientoExterminador_izquierda
        if contadorFrames_exterminador_DerIzq >= 6:  # son 6 sprites 
            contadorFrames_exterminador_DerIzq = 0
        if contadorFrames_exterminador_arriba >= 3:  # son 3 sprites
            contadorFrames_exterminador_arriba = 0
        if contadorFrames_exterminador_abajo  >=3:  # son 3 sprites
            contadorFrames_exterminador_abajo = 0

        # Cambiar la imagen si el jugador  la tecla correspondiente. Va antes porque primero se toca la tecla
        if movimientoExterminador_derecha == True and moviendose == True:
            self.image = pg.transform.scale((imagenes_exterminador_correrDerecha[contadorFrames_exterminador_DerIzq]), (100,50))
            contadorFrames_exterminador_DerIzq += 1
        elif movimientoExterminador_izquierda == True and moviendose == True:
            self.image = pg.transform.scale((imagenes_exterminador_correrIzquierda[contadorFrames_exterminador_DerIzq]), (100,50))
            contadorFrames_exterminador_DerIzq += 1
        # para frames de movimiento vertical
        elif movimientoExterminador_arriba == True and moviendose == True:
            self.image = pg.transform.scale((imagenes_exterminador_correrArriba[contadorFrames_exterminador_arriba]), (100,50))
            contadorFrames_exterminador_arriba += 1
        elif movimientoExterminador_abajo == True and moviendose == True:
            self.image = pg.transform.scale((imagenes_exterminador_correrAbajo[contadorFrames_exterminador_abajo]),  (100,50))
            contadorFrames_exterminador_abajo += 1
 
        # PARA CUANDO NO ESTA MOVIENDOSE
        if movimientoExterminador_derecha == True and moviendose == False:
            self.image = pg.transform.scale(pg.image.load("imagenes/exterminador/Gunner_Blue_Idle_1.png"),(100,50))
        elif movimientoExterminador_izquierda == True and moviendose == False:
            self.image = pg.transform.scale(pg.image.load("imagenes/exterminador/Gunner_Blue_Idle_izq_1.png"), (100,50))
        # para frames de movimiento vertical
        elif movimientoExterminador_arriba == True and moviendose == False:
            self.image = pg.transform.scale((imagenes_exterminador_correrArriba[1]), (100,50))
        elif movimientoExterminador_abajo == True and moviendose == False:
            self.image = pg.transform.scale((imagenes_exterminador_correrAbajo[1]),  (100,50))
        # velocidad predeterminadad cada vuelta del bucle si no pulsas nada

        self.velocidad_x = 0
        self.velocidad_y = 0

        # comando para cuando el usuario mantiene la tecla pulsada
        teclas = pg.key.get_pressed()

        

        # mover el personaje izq - der
        if teclas[pg.K_a]:  # mover movimientoExterminador_movimientoExterminador_izquierda
            self.velocidad_x = -10
            movimientoExterminador_izquierda = True
            movimientoExterminador_derecha = False
            movimientoExterminador_arriba = False
            movimientoExterminador_abajo = False
            moviendose = True
        elif teclas[pg.K_d]:  # mover movimientoExterminador_derecha
            self.velocidad_x = 10
            movimientoExterminador_derecha = True
            movimientoExterminador_izquierda = False
            movimientoExterminador_arriba = False
            movimientoExterminador_abajo = False
            moviendose = True
        # mover el personaje arr -abj
        elif teclas[pg.K_w]:
            self.velocidad_y = -10 # quita relleno
            movimientoExterminador_arriba = True
            movimientoExterminador_abajo = False
            movimientoExterminador_izquierda = False
            movimientoExterminador_derecha = False
            moviendose = True
        elif teclas[pg.K_s]:
            self.velocidad_y = 10 # pone relleno
            movimientoExterminador_abajo = True
            movimientoExterminador_arriba = False
            movimientoExterminador_izquierda = False
            movimientoExterminador_derecha = False
            moviendose = True
        # si no se toca ninguna tecla
        else:
            moviendose = False 

        # SI EL JUGADOR QUIERE DISPARAR

        # Disparo grande va primero porque si es verdad pasa algo en las funciones disparo_der, izq...

        # si el jugador toca la tecla g y ya hizo colicion con una caja especial
        if teclas[pg.K_g] and contador_balas_disparoGrande > 0:
          bool_disparo_grande = True
        # si toca la tecla pero no tiene balas grandes
        elif teclas[pg.K_t]:
          bool_disparo_grande = False
          #print("toco la tecla tecla t ")
        # para desactivar el poder por si solo
        if contador_balas_disparoGrande <= 0:
          bool_disparo_grande = False

        # DISPAROS
        if teclas[pg.K_SPACE] and movimientoExterminador_derecha == True:
           # EN VEZ DE CAMBIAR LA VELOCIDAD LLAMAMOS A QUE SE CREE UNA BALA POR EL METODO (DISPARO) 
           jugador.disparo_der() 
           EstaDisparando = True # musica
        elif teclas[pg.K_SPACE] and movimientoExterminador_izquierda == True:
           jugador.disparo_izq()
           EstaDisparando = True # musica
        elif teclas[pg.K_SPACE] and movimientoExterminador_abajo == True:
           jugador.disparo_abj()
           EstaDisparando = True # musica
        elif teclas[pg.K_SPACE] and movimientoExterminador_arriba == True:
           jugador.disparo_Arrb()
           EstaDisparando = True # musica
        elif teclas[pg.K_SPACE]:
            jugador.disparo_der()
            EstaDisparando = True # musica
        
        #MUROS
        if teclas[pg.K_f] and contador_muros > 0:
            jugador.crear_muro()
            contador_muros -= 1
        if teclas[pg.K_r] and contador_barril_explota > 0:
            jugador.crear_muro_exposivo()
            contador_barril_explota -= 1
        else:
            pass

        
        # Especificar el cambio de posicion del personaje(VELOCIDAD)
        self.rect.x += self.velocidad_x 
        self.rect.y += self.velocidad_y


        # si el jugador colisiona con algun muro (NO LO DEJA AVANZAR)
        colision_muros= pg.sprite.spritecollide(jugador,sprites_muros,False,pg.sprite.collide_circle)
        if colision_muros:
            # Va a morverlo contrario a la direccion que tomo
            if teclas[pg.K_a]:  # mover movimientoExterminador_izquierda
                self.rect.x += 10
            elif teclas[pg.K_d]:  # mover derecha
                self.rect.x -= 10
            # mover el personaje arr -abj
            elif teclas[pg.K_w]:
                self.rect.y += 10 # pone relleno
            elif teclas[pg.K_s]:
                self.rect.y -= 10 # quita relleno
            else:
                pass
        
        #LIMITES DE PANTALLA
        # limites del margen izquierdo
        if self.rect.left < 0:
            self.rect.left = 0
        # limites del margen derecho
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        #limites arriba y abajo
        if self.rect.top < 0:
            self.rect.top = 0
        # limite margen de abajo
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO

        #PONER MUSICA DE DOLOR
        if es_volumen_nulo == False:
            if bool_musica_dolor_jugador == True:
                self.sonido_dolor.play()
                bool_musica_dolor_jugador = False
            else:
                pass


    def disparo_der(self):
        global contador_balas_disparoGrande

        # ver si el volumen es nulo
        if es_volumen_nulo == False:
            self.sonido_disparo.play()

        # para cuado se llama a una bala pero (DISPARO GRANDE) esta activado
        if bool_disparo_grande == True:
            contador_balas_disparoGrande -= 1
            bala_g = DisparosDerecha(self.rect.centerx, self.rect.centery)
            sprites_balas_grandes.add(bala_g)
        else:
            bala = DisparosDerecha(self.rect.centerx, self.rect.centery)
            sprites_balas.add(bala)


    def disparo_izq(self):
        global contador_balas_disparoGrande

        # ver si el volumen es nulo
        if es_volumen_nulo == False:
            self.sonido_disparo.play()

        if bool_disparo_grande == True:
            contador_balas_disparoGrande -= 1
            bala_g = DisparosIzquierda(self.rect.centerx, self.rect.centery)
            sprites_balas_grandes.add(bala_g)
        else:
            bala = DisparosIzquierda(self.rect.centerx, self.rect.centery)
            sprites_balas.add(bala)

    def disparo_abj(self):
        global contador_balas_disparoGrande

        # ver si el volumen es nulo
        if es_volumen_nulo == False:
            self.sonido_disparo.play()


        if bool_disparo_grande == True:
            contador_balas_disparoGrande -= 1
            bala_g = DisparosAbajo(self.rect.centerx, self.rect.centery)
            sprites_balas_grandes.add(bala_g)
        else:
            bala = DisparosAbajo(self.rect.centerx, self.rect.centery)
            sprites_balas.add(bala)


    def disparo_Arrb(self):
        global contador_balas_disparoGrande

        # ver si el volumen es nulo
        if es_volumen_nulo == False:
            self.sonido_disparo.play()

        if bool_disparo_grande == True:
            contador_balas_disparoGrande -= 1
            bala_g = DisparosArriba(self.rect.centerx, self.rect.centery)
            sprites_balas_grandes.add(bala_g)
        else:
            bala = DisparosArriba(self.rect.centerx, self.rect.centery)
            sprites_balas.add(bala)
          

    def crear_muro(self):
        # hace lo mismo que la funcion disparo crea el objeto cuando lo llaman con las posiciones
        # del jugador
        muro = Muro(self.rect.centerx + 5, self.rect.centery)
        sprites_muros.add(muro)

    def crear_muro_exposivo(self):
        # hace lo mismo que la funcion disparo crea el objeto cuando lo llaman con las posiciones
        # del jugador
        muro_explosivo = MuroExplosivo(self.rect.centerx + 5, self.rect.centery)
        sprites_muros_explosivos.add(muro_explosivo)


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
        self.velocidad_x = 5
        self.velocidad_y = 5
        #contar los pasos del zombie
        self.cuentaPasos_Zombie = 0
        # boleano si esta mordiendo
        self.sonido_mordida =  pg.mixer.Sound("musica/mordida.mp3")

    def update(self):
        global bool_musica_mordida_zombie_verde

        self.rect.y += self.velocidad_x
        self.rect.x += self.velocidad_y

        # control_sprites
        if self.cuentaPasos_Zombie >= 5:  # son 5 sprites 
            self.cuentaPasos_Zombie = 0

        # cambiar imagen

        self.image = pg.transform.scale((imagenes_zombieVerde_correrDerecha[self.cuentaPasos_Zombie]), (50,60))
        self.cuentaPasos_Zombie += 1
        #print(self.cuentaPasos_Zombie)

        # Limites o maregnes
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

        # sonido
        if es_volumen_nulo == False:
            if bool_musica_mordida_zombie_verde == True:
                self.sonido_mordida.play()
                bool_musica_mordida_zombie_verde = False
            else:
                pass
        


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
        #contar los pasos del zombie
        self.cuentaPasos_Zombie = 0
        # poner musica
        self.sonido_mordida =  pg.mixer.Sound("musica/mordida.mp3")


    def update(self):
        global bool_musica_mordida_zombie_morado
         
        self.rect.y -= self.velocidad_x
        self.rect.x -= self.velocidad_y

        # sonido
        if es_volumen_nulo == False:
            if bool_musica_mordida_zombie_morado:
                self.sonido_mordida.play()
                bool_musica_mordida_zombie_morado = False
            else:
                pass

        # control_sprites
        if self.cuentaPasos_Zombie >= 5:  # son 5 sprites 
            self.cuentaPasos_Zombie = 0

        # cambiar imagen solo de correr
        self.image = pg.transform.scale((imagenes_zombieMorado_correrIzquierda[self.cuentaPasos_Zombie]), (50,60))
        self.cuentaPasos_Zombie += 1
        #print(self.cuentaPasos_Zombie)

        # Limites o maregnes
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


class DisparosDerecha(pg.sprite.Sprite):
    def __init__(self, x, y): # al inicializar un objeto de clase se pide la posicion(x, y)
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("imagenes/disparo_der_izq.png"),(10,20))
        self.rect = self.image.get_rect()
        self.rect.y = y - 17 # se quiere que la posicion de Y se ponga instanciando la clase
        self.rect.right = x # se quiere que la posicion de X se ponga instanciando la clase

    def update(self):

         # Si  jugador presiono (g) disparo Grande esta prendido[cambia la imagen]
        if bool_disparo_grande == True:
          self.image = pg.transform.scale(imagenes_disparosGrandes[0],(110,50))
          self.rect.x += 25 
        else:
            self.image = pg.transform.scale(pg.image.load("imagenes/disparo_der_izq.png"),(10,20))
            # Velocidad de la bala
            self.rect.x += 25 

        #print(self.rect.left) # llega hasta 1020 entonces si borra la bala
        if self.rect.left >= ANCHO:
            self.kill()


class DisparosIzquierda(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("imagenes/disparo_der_izq.png"),(10,20)) 
        self.rect = self.image.get_rect()
        self.rect.y = y - 17 
        self.rect.left = x 

    def update(self):

        # Si disparo Grande esta prendido
        if bool_disparo_grande == True:
          self.image = pg.transform.scale(imagenes_disparosGrandes[1],(110,50))
          self.rect.x -= 25 
        else:
          self.image = pg.transform.scale(pg.image.load("imagenes/disparo_der_izq.png"),(10,20))
          # Velocidad de la bala
          self.rect.x -= 25 
        
        if self.rect.left <= 0:
            self.kill()



class DisparosAbajo(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("imagenes/disparo_der_izq.png"),(10,20)) 
        self.rect = self.image.get_rect()
        self.rect.y = y 
        self.rect.x = x -5

    def update(self):
        # Si disparo Grande esta prendido
        if bool_disparo_grande == True:
            self.image = pg.transform.scale(imagenes_disparosGrandes[3],(50,110))
            self.rect.y += 25
        else:
            self.image = pg.transform.scale(pg.image.load("imagenes/disparo_der_izq.png"),(10,20))
            # Velocidad de la bala
            self.rect.y += 25

        if self.rect.bottom >= ALTO:
            self.kill()

class DisparosArriba(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("imagenes/disparo_der_izq.png"),(10,20)) 
        self.rect = self.image.get_rect()
        self.rect.y = y 
        self.rect.x = x-3

    def update(self):
        # Si disparo Grande esta prendido
        if bool_disparo_grande == True:
          self.image = pg.transform.scale(imagenes_disparosGrandes[2],(50,110))
          self.rect.y -= 25
        else:
            self.image = pg.transform.scale(pg.image.load("imagenes/disparo_der_izq.png"),(10,20))
            # Velocidad de la bala
            self.rect.y -= 25

        if self.rect.top <= 0:
            self.kill()


class Muro(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("imagenes/muro_blanco.png"),(40,40))
        self.rect = self.image.get_rect()
        # queremos que el alto lo pongan instanciando la clase
        self.rect.bottom = y + 30
        # se quiere que la posiscion x la pongan instanciando la clase
        self.rect.centerx = x +40
        # radio
        self.radius = 8 
        # pg.draw.circle(self.image, ROJO,self.rect.center,self.radius,10)
        

    def update(self):

        # SE PUEDE MEJPRARA CON EL CONTADOR BALA MURO_ PARA LA ELIMINACION CON LAS BALAS Y LA ELIMIACION CON LOS ENEMIGOS
        # el muro solo se actualiza cuando las balas van a romper los mueros
        global contador_bala_muro
        pg.sprite.groupcollide(sprites_balas,sprites_muros,False,True, pg.sprite.collide_circle) # colision_balas_muro
        # if colision_bala_muro:
            # print("colsion bala muro")
            # contador_bala_muro += 1
            # print(contador_bala_muro)
            # if contador_bala_muro >= 3:
            #     contador_bala_muro = 0

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
    
    def update(self):
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
        if es_volumen_nulo == False:
            self.sonido_explosion.play()

        for sprite_muroExplosivo in sprites_muros_explosivos:
                colicion_muroExplosivo_enemigo = pg.sprite.spritecollide(sprite_muroExplosivo,sprites_enemigos,True,pg.sprite.collide_circle)
            # la colicion es sin radio para que coja todo el sprite
            

class BarraVida(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.transform.scale(imagenes_barraVida[0],(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO -100
        self.rect.y = 15

    def update(self):
        global contador_golpes_jugador_porEnemigo

        if contador_golpes_jugador_porEnemigo >= 1 and  contador_golpes_jugador_porEnemigo < 11 :
           self.image = pg.transform.scale(imagenes_barraVida[1],(100,100))
        elif contador_golpes_jugador_porEnemigo >= 11 and  contador_golpes_jugador_porEnemigo < 21:
           self.image = pg.transform.scale(imagenes_barraVida[2],(100,100))
        elif contador_golpes_jugador_porEnemigo >= 21 and contador_golpes_jugador_porEnemigo < 31:
           self.image = pg.transform.scale(imagenes_barraVida[3],(100,100))
        elif contador_golpes_jugador_porEnemigo >= 31 and contador_golpes_jugador_porEnemigo  < 41:
           self.image = pg.transform.scale(imagenes_barraVida[4],(100,100)) 
        elif contador_golpes_jugador_porEnemigo  >= 41 and contador_golpes_jugador_porEnemigo < 51 :
           self.image = pg.transform.scale(imagenes_barraVida[5],(100,100)) 
        else:
           self.image = pg.transform.scale(imagenes_barraVida[0],(100,100)) 
        


class CajasEspeciales(pg.sprite.Sprite):
    def __init__(self, numeroSprite):
        super().__init__()
        self.image= pg.transform.scale(imagenes_cajasEspeciales[numeroSprite], (30,30))
        self.rect = self.image.get_rect()
        self.rect.y = 300
        self.rect.x = 400
        self.radius = 8

    def update(self):
        global bool_disparo_grande
        global bool_barril_explota

        if bool_disparo_grande == True:
            self.image = pg.transform.scale(imagenes_cajasEspeciales[0], (30,30))
            #print("se imprimio disparo grande")
        elif bool_barril_explota == True:
            self.image = pg.transform.scale(imagenes_cajasEspeciales[1], (30,30))


# Pantalla y clock 
pantalla = None 
clock = None

# el metodo update se llama por  los grupos (Group.update())
# GRUPOS DE SPRITES
sprites_jugador = None
sprites_enemigos = None
sprites_enemigos_verdes = None
sprites_enemigos_morados = None
sprites_balas = None
sprites_balas_grandes = None
sprites_muros = None
sprites_barra_vida = None
sprites_cajas_especiales = None
sprites_muros_explosivos = None

# Crear objetos y añadirlos al grupo de sprite
jugador = None
barra_v = None

# muros contenedores horizontales
y = None
x = None

# MAS CONTADORES QUE HAY QUE OGRANIZAR PRINCIPALMENTE COLICIONES
numeroColisiones = None
huboColision = None
contador_balas_enemigo = None
contador_golpes_jugador_porEnemigo = None

# Contador de cronometro
tiempo_milisegundo = None
segundos = None
minutos = None

# Contador de puntuacion
contador_muerte_enemigos = None
puntuacion = None


# contador mordidas de los zombies
cuentaMordidas_zombie_verde = None
cuentaMordidas_zombie_morado = None

# contador para el numero de enemigos
contador_poner_enemigos = None

def inicializarJuego():
    # INICIALIZAR LAS VARIABLES PARA EL FUNCIONAMIENTO DEL JUEGO 
    # Pantalla y clock 
    global pantalla
    global clock

    # el metodo update se llama por  los grupos (Group.update())
    # GRUPOS DE SPRITES
    global sprites_jugador
    global sprites_enemigos
    global sprites_enemigos_verdes
    global sprites_enemigos_morados
    global sprites_balas
    global sprites_balas_grandes
    global sprites_muros
    global sprites_barra_vida
    global sprites_cajas_especiales
    global sprites_muros_explosivos

    # Crear objetos y añadirlos al grupo de sprite
    global jugador
    global barra_v

    # muros contenedores horizontales
    global y
    global x

    # MAS CONTADORES QUE HAY QUE OGRANIZAR PRINCIPALMENTE COLICIONES
    global numeroColisiones
    global huboColision
    global contador_balas_enemigo
    global contador_golpes_jugador_porEnemigo

    # Contador de cronometro
    global tiempo_milisegundo
    global segundos
    global minutos

    # Contador de puntuacion
    global contador_muerte_enemigos
    global puntuacion

    # contador mordidas de los zombies
    global cuentaMordidas_zombie_verde
    global cuentaMordidas_zombie_morado

    # contador para el numero de enemigos
    global contador_poner_enemigos
        
    # Incializar pygame
    pg.init()

    # pantalla
    pantalla = pg.display.set_mode((ANCHO, ALTO))
    pg.display.set_caption("JUEGO EXTERMINADOR")
    ######
    # Falta poner icono


    # musica
    pg.mixer.music.load("musica/musica_fondo.mp3")# cargar musica python
    # reproducir la musica infinitamente
    pg.mixer.music.play(-1) 

    # reloj
    clock = pg.time.Clock()

    # el metodo update se llama por  los grupos (Group.update())
    # GRUPOS DE SPRITES
    sprites_jugador = pg.sprite.Group()
    sprites_enemigos = pg.sprite.Group()
    sprites_enemigos_verdes = pg.sprite.Group()
    sprites_enemigos_morados = pg.sprite.Group()
    sprites_balas = pg.sprite.Group()
    sprites_balas_grandes = pg.sprite.Group()
    sprites_muros = pg.sprite.Group()
    sprites_barra_vida = pg.sprite.Group()
    sprites_cajas_especiales = pg.sprite.Group()
    sprites_muros_explosivos = pg.sprite.Group()


    # Crear objetos y añadirlos al grupo de sprite
    jugador = Jugador()
    barra_v = BarraVida()


    # Añadir los objeto a los grupos de sprites
    sprites_jugador.add(jugador) 
    sprites_barra_vida.add(barra_v)

    # muros contenederes verticales
    y = 40
    x = 730
    for i in range(7):
        y += 20
        if i == 3:
            y += 20
            muro = Muro(x, y)
            sprites_muros.add(muro)
        else:
            muro = Muro(x, y)
            sprites_muros.add(muro)

    # muros contenedores horizontales
    y = 280
    x = 760

    for i in range(5):
        x += 40
        muro = Muro(x, y)
        sprites_muros.add(muro)


    # MAS CONTADORES QUE HAY QUE OGRANIZAR PRINCIPALMENTE COLICIONES
    numeroColisiones = 0
    huboColision = False
    contador_balas_enemigo = 0
    contador_golpes_jugador_porEnemigo = 0

    # Contador de cronometro
    tiempo_milisegundo = 0
    segundos = 0
    minutos = 0

    # Contador de puntuacion
    contador_muerte_enemigos = 0
    puntuacion = 0


    # contador mordidas de los zombies
    cuentaMordidas_zombie_verde = 0
    cuentaMordidas_zombie_morado = 0

    # contador para el numero de enemigos
    contador_poner_enemigos = 4

    ######
    # LLAMAR A LAS OTRAS VARIABLES GLOABALES 
    # variables direccion
    global movimientoExterminador_izquierda
    global movimientoExterminador_derecha
    global movimientoExterminador_arriba
    global movimientoExterminador_abajo

    #Variables para contar los frames
    global contadorFrames_exterminador_arriba
    global contadorFrames_exterminador_DerIzq
    global contadorFrames_exterminador_abajo

    # contadores para las coliciones
    global contador_bala_muro
    global contador_enemigo_muro

    #Variables boleanas para los cubos (premios)
    global bool_disparo_grande
    global bool_barril_explota

    # contador para los objetos premios
    global contador_balas_disparoGrande
    global contador_barril_explota
    global contador_muros

    # contadores boleanos para saber si poner musica
    global bool_musica_mordida_zombie_verde
    global bool_musica_mordida_zombie_morado
        # No hay necesidad de una variable para la musica del barril ya que cuando lo actualizamos se elimina el sprite
    global bool_musica_dolor_jugador

    # variable para saber si el jugador se mueve
    global moviendose

    # mirar si el volumen es nulo
    global es_volumen_nulo

    #BUCLE DEL JUEGO         
    while True:
        clock.tick(FPS) # velociade de bucle

        #para saber si terminar el bucle
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        # CREAR ENEMIGOS CON EL TIEMPO
        if ((segundos == 2 and tiempo_milisegundo < 1) and minutos == 0) or (segundos == 30 and tiempo_milisegundo < 1) or (segundos == 59 and tiempo_milisegundo < 1):

            for i in range(contador_poner_enemigos):
                enemigo_verde = Enemigos_verdes()
                enemigo_morado = Enemigos_morado()

                sprites_enemigos_verdes.add(enemigo_verde)
                sprites_enemigos_morados.add(enemigo_morado)

                sprites_enemigos.add(enemigo_verde)
                sprites_enemigos.add(enemigo_morado)

            contador_poner_enemigos += 2
            time.sleep(1)
            ####  hacer UN TEXTO LLAMATIVO QUE SAQUE EMBOSCADA

        # Actualizacion de sprites
        sprites_jugador.update() # actualizar el grupo de sprites
        sprites_enemigos.update()
        sprites_balas.update()
        sprites_barra_vida.update()
        sprites_balas_grandes.update()
        #sprites_muros.update()


        # COLISIONES
        #Ojo para que sean mas precisas se necesita un radio no rectangulo. 
        #colision = pg.sprite.spritecollide(jugador,sprites_enemigos,False,pg.sprite.collide_circle) 
        # colision_balas_enemigos =  pg.sprite.groupcollide(sprites_balas,sprites_enemigos,True,False,) # de esos dos grupos de sprites elimina el segundo


        # Colicion de los enemigos con las balas pequeñas
        for sprite_enemigo in sprites_enemigos:
            colision_balas_enemigo = pg.sprite.spritecollide(sprite_enemigo,sprites_balas,False,pg.sprite.collide_circle)
            if colision_balas_enemigo:
                # ya que sabemos que hubo colicion de un enemigo con alguna bala entonces borramos esa bala
                colision_balas_enemigo = pg.sprite.spritecollide(sprite_enemigo,sprites_balas,True,pg.sprite.collide_circle)
                contador_balas_enemigo += 1
                if contador_balas_enemigo >= 4:
                    contador_balas_enemigo = 0
                    # poner puntos a la puntuacion
                    contador_muerte_enemigos += 1
                    puntuacion += 20
                    sprite_enemigo.kill()

        # colicion balas Grandes con los enemigos
        for sprite_balaGrande in sprites_balas_grandes:
            i = 0
            j = 0
            for sprite_enemigo in sprites_enemigos:
                j += 1
                i += 1 
                comparacion_x = sprite_balaGrande.rect.x  - sprite_enemigo.rect.x
                comparacion_y = sprite_balaGrande.rect.y  - sprite_enemigo.rect.y
                # print(f"la bala grande  {i}: { sprite_balaGrande.rect.x }, {sprite_balaGrande.rect.y}")
                # print(f"el enemigo   {j}: {  sprite_enemigo.rect.x }, {sprite_enemigo.rect.y}")
                # print(comparacion_x)
                # print(comparacion_y)
                if ((comparacion_y >= -30) and (comparacion_y <= 30)) and ((comparacion_x >= -30) and (comparacion_x <= 30)):
                    sprite_enemigo.kill()
                    #poner puntuacion
                    contador_muerte_enemigos += 1
                    puntuacion += 20
                else:
                    pass
            

        # eliminar bala grande
        for sprite_balaGrande in sprites_balas_grandes:
            # Limites o margenes
            if sprite_balaGrande.rect.right > ANCHO: # margen derecho
                sprite_balaGrande.kill()
            elif sprite_balaGrande.rect.left < 0: # margen izquierdo
                sprite_balaGrande.kill()
            elif sprite_balaGrande.rect.bottom > ALTO: # margen abajo
                sprite_balaGrande.kill()
            elif sprite_balaGrande.rect.top < 0: # margen arriba
                sprite_balaGrande.kill()

        # Coliciones de la bala pequeña con el muro
        for sprite_muro in sprites_muros:
            colision_balas_muros =  pg.sprite.spritecollide(sprite_muro, sprites_balas,False,pg.sprite.collide_circle)
            if colision_balas_muros:
                contador_bala_muro += 1
                if contador_bala_muro >= 100:
                    contador_bala_muro = 0
                    sprite_muro.update() 
                    # poner puntuacion
                    puntuacion += 3
        
        # Coliciones de la bala grande con el muro
        for sprite_muro in sprites_muros:
            colision_balasGrandes_muro =  pg.sprite.spritecollide(sprite_muro,sprites_balas_grandes,False,pg.sprite.collide_circle)
            if colision_balasGrandes_muro:
                contador_bala_muro += 45
                if contador_bala_muro >= 100:
                    contador_bala_muro = 0
                    sprite_muro.kill()
                    puntuacion += 3


        # Coliciones del enemigo (zombie verde) con el muro
        for sprite_muro in sprites_muros:
            for sprite_enemigo in sprites_enemigos_verdes:
                # vamos a ver si el enemigo tiene colicion con alguno de los muros
                colicion_muro_enemigo = pg.sprite.spritecollide(sprite_enemigo,sprites_muros,False,pg.sprite.collide_circle)
                if colicion_muro_enemigo:      
                    contador_enemigo_muro += 1
                    sprite_enemigo.rect.x += -5
                    sprite_enemigo.rect.y += -5
                    if contador_enemigo_muro >= 100:
                        sprite_muro.kill()
                        contador_enemigo_muro = 0
        
        # Coliciones del enemigo (zombie morado) con el muro
        for sprite_muro in sprites_muros:
            for sprite_enemigo in sprites_enemigos_morados:
                # vamos a ver si el enemigo tiene colicion con alguno de los muros
                colicion_muro_enemigo = pg.sprite.spritecollide(sprite_enemigo,sprites_muros,False,pg.sprite.collide_circle)
                if colicion_muro_enemigo:      
                    contador_enemigo_muro += 1
                    sprite_enemigo.rect.x += +5
                    sprite_enemigo.rect.y += +6 # va a ir escalando un poco
                    if contador_enemigo_muro >= 100: 
                        sprite_muro.kill()
                        contador_enemigo_muro = 0
                        
                    

        # Coliciones del jugador con los enemigos
        colision_jugador_enemigos = pg.sprite.spritecollide(jugador, sprites_enemigos, False,pg.sprite.collide_circle)
        if colision_jugador_enemigos:
            contador_golpes_jugador_porEnemigo += 1
            bool_musica_dolor_jugador = True # poner musica en la clase
            if contador_golpes_jugador_porEnemigo == 51:
                print("perdio")
                return(0)
                
                # pg.quit()

        # Cuando un zombie verde nos muerde
        #limite del sprite
        if cuentaMordidas_zombie_verde >= 2:
            cuentaMordidas_zombie_verde = 0

        #Cambiar sprite
        for sprite_enemigo_verde in sprites_enemigos_verdes:
            colicion_jugador_enemigos_verdes = pg.sprite.spritecollide(sprite_enemigo_verde, sprites_jugador, False,pg.sprite.collide_circle)
            if colicion_jugador_enemigos_verdes : # si hay colcion de los enemigos verdes con el jugador
                bool_musica_mordida_zombie_verde = True # poner musica en la clase
                if cuentaMordidas_zombie_verde >= 2: # te puede morder mas de un zombi a la vez
                    cuentaMordidas_zombie_verde = 0
                else:
                    sprite_enemigo_verde.image = pg.transform.scale((imagenes_zombieVerde_morderDerecha[cuentaMordidas_zombie_verde]), (50,60))
                    cuentaMordidas_zombie_verde += 1

        # Cuando un zombie morado nos muerde
        #limite del sprite
        if cuentaMordidas_zombie_morado >= 2:
            cuentaMordidas_zombie_morado = 0

        #Cambiar sprite
        for sprite_enemigo_morado in sprites_enemigos_morados:
            colicion_jugador_enemigoMorado = pg.sprite.spritecollide(sprite_enemigo_morado, sprites_jugador, False,pg.sprite.collide_circle)
            if colicion_jugador_enemigoMorado:
                bool_musica_mordida_zombie_morado = True # poner musica en la clase
                # llamamos de nuevo esta parte para que no se rompa el juego, si nos muerden varios zombies
                if cuentaMordidas_zombie_morado >= 2:
                    cuentaMordidas_zombie_morado= 0
                else:
                    sprite_enemigo_morado.image = pg.transform.scale((imagenes_zombieMorado_morderIzquierda[cuentaMordidas_zombie_morado]), (50,60))
                    cuentaMordidas_zombie_morado += 1

        # Coliciones de barriles explosivos con los ENEMIGOS VERDES
        for sprite_enemigo in sprites_enemigos_verdes:
            # vamos a ver si el enemigo tiene colicion con alguno de los muros
            colicion_muroExplosivo_enemigo = pg.sprite.spritecollide(sprite_enemigo,sprites_muros_explosivos,False,pg.sprite.collide_circle)
            if colicion_muroExplosivo_enemigo:      
                sprite_enemigo.rect.x += -5
                sprite_enemigo.rect.y += -8 # se va ir un poco hacia arriba lo va a escalar

        # Coliciones de barriles explosivos con los ENEMIGOS MORADOS
        for sprite_enemigo in sprites_enemigos_morados:
            # vamos a ver si el enemigo tiene colicion con alguno de los muros
            colicion_muroExplosivo_enemigo = pg.sprite.spritecollide(sprite_enemigo,sprites_muros_explosivos,False,pg.sprite.collide_circle)
            if colicion_muroExplosivo_enemigo:      
                sprite_enemigo.rect.x += 30
                sprite_enemigo.rect.y += 10

        # Colicion barril_explosivo con la bala
        for sprite_muroExplosivo in sprites_muros_explosivos:
            colicion_muroExplosivo_balas = pg.sprite.spritecollide(sprite_muroExplosivo,sprites_balas,False,pg.sprite.collide_circle)
            if colicion_muroExplosivo_balas:
                sprite_muroExplosivo.update()
                pg.display.flip() # actualizamos pantalla
                time.sleep(0.5) # paramos un momento el juego 1/2 segundo
                sprite_muroExplosivo.kill()
                puntuacion += 5

        # Colciion barril_explosivo con la bala grande
        for sprite_muroExplosivo in sprites_muros_explosivos:
            colicion_muroExplosivo_balasGrandes = pg.sprite.spritecollide(sprite_muroExplosivo,sprites_balas_grandes,False,pg.sprite.collide_circle)
            if colicion_muroExplosivo_balasGrandes:
                sprite_muroExplosivo.update()
                pg.display.flip() # actualizamos pantalla
                time.sleep(0.5) # paramos un momento el juego 1/2 segundo
                sprite_muroExplosivo.kill()
                puntuacion += 5

        # Dibujar el fondo de la pantalla. Tiene que ser en el bucle porque si no quedan las imagenes represadas
        pantalla.blit(fondo,(0,0)) # imagen, (0,0) no margenes

        # Dibujar los grupos de sprites
        sprites_jugador.draw(pantalla) 
        sprites_enemigos.draw(pantalla)
        sprites_balas.draw(pantalla) 
        sprites_muros.draw(pantalla)
        sprites_barra_vida.draw(pantalla)
        sprites_muros_explosivos.draw(pantalla)
        sprites_balas_grandes.draw(pantalla)

        
        # hacer un cronometro no tan exacto casero
        tiempo_milisegundo += 1.10
        if tiempo_milisegundo >=10:
            segundos += 1
            tiempo_milisegundo = 0
        if segundos >= 60:
            minutos += 1
            segundos = 0  


        
        # CAJAS ESPECIALES (disparos grandes)
        if segundos >= 10 and segundos < 17: # va durar la caja 5 segundos en pantalla(10-15 =5)
            if segundos == 10 and tiempo_milisegundo < 1:
                cajas_e = CajasEspeciales(1) # como es caja de disparo grande sprite(1)
                print("aparecio caja")
                sprites_cajas_especiales.add(cajas_e)
            else:
                sprites_cajas_especiales.draw(pantalla)
                colicion_jugador_cajasEspeciales = pg.sprite.spritecollide(jugador, sprites_cajas_especiales, False,pg.sprite.collide_circle)
                # si el tiempo se paso
                if segundos == 16 and tiempo_milisegundo < 1:
                    cajas_e.kill()
                if colicion_jugador_cajasEspeciales:
                    contador_balas_disparoGrande += (5 +(5*minutos))
                    cajas_e.kill() # como el objeto es solo uno entonces se puede eliminar directamente
                    # bool_disparo_grande = True <-- lo va a activar presionando una tecla
                    # revisar es linea
        
        # CAJAS ESPECIALES (barril explota)
        if segundos >= 5 and segundos < 11: # va durar la caja 5 segundos en pantalla(10-15 =5)
            if segundos == 5 and tiempo_milisegundo < 1:
                cajas_barril = CajasEspeciales(0) # como es caja de barriles sprite(0)
                print("aparecio caja")
                sprites_cajas_especiales.add(cajas_barril)
            else:
                sprites_cajas_especiales.draw(pantalla)
                colicion_jugador_cajasEspeciales = pg.sprite.spritecollide(jugador, sprites_cajas_especiales, False,pg.sprite.collide_circle)
                if segundos == 10 and tiempo_milisegundo < 1:
                    cajas_barril.kill()
                if colicion_jugador_cajasEspeciales:
                    contador_barril_explota += (3 + 3*minutos)
                    cajas_barril.kill() # como el objeto es solo uno entonces se puede eliminar directamente
                    # bool_disparo_grande = True <-- lo va a activar presionando una tecla
                    # revisar es linea
        
        # CAJAS ESPECIALES (muros)
        if segundos >= 20 and segundos < 27: # va durar la caja 5 segundos en pantalla(10-15 =5)
            if segundos == 20 and tiempo_milisegundo < 1:
                cajas_muro = CajasEspeciales(2) # como es caja de muros sprite(2)
                print("aparecio caja")
                sprites_cajas_especiales.add(cajas_muro)
            else:
                sprites_cajas_especiales.draw(pantalla)
                colicion_jugador_cajasEspeciales = pg.sprite.spritecollide(jugador, sprites_cajas_especiales, False,pg.sprite.collide_circle)
                if segundos == 26 and tiempo_milisegundo < 1:
                    cajas_muro.kill()
                if colicion_jugador_cajasEspeciales:
                    contador_muros += (3 + 3*minutos)
                    cajas_muro.kill() # como el objeto es solo uno entonces se puede eliminar directamente
                    # bool_disparo_grande = True <-- lo va a activar presionando una tecla
                    # revisar es linea

        # SONIDO Y CONTROLADOR DE SONIDO
        #Ojo: solo para la musica en bucle(FONDO DEL JUEGO)
        
        keys = pg.key.get_pressed() #Opción tecla pulsada

        #CONTROL DE SONIDO
        volumen_actual = pg.mixer.music.get_volume()

        #saber si el volumen es nulo 
        if volumen_actual == 0.0:
            es_volumen_nulo = True
        else:
            es_volumen_nulo = False

        #baja volumen
        if keys[pg.K_1] and volumen_actual > 0.0: # 0.0 volumen nulo
            pg.mixer.music.set_volume(volumen_actual - 0.1) # para colocar o cambiar el volumen
            imagen = pg.transform.scale(imagen_sonido_bajar,(100,50))
            pantalla.blit(imagen, (10,70))

        elif keys[pg.K_1] and volumen_actual == 0.0:
            imagen = pg.transform.scale(imagen_sonido_bajar,(100,50))
            pantalla.blit(imagen, (10,70))
        
        #sube volumen
        if keys[pg.K_2] and volumen_actual < 1.0: # 1.0 maximo volumen
            pg.mixer.music.set_volume(volumen_actual + 0.1)
            imagen = pg.transform.scale(imagen_sonido_subir,(100,50))
            pantalla.blit(imagen,(10,70))


        elif keys[pg.K_2] and volumen_actual == 0.0 or (keys[pg.K_2] and volumen_actual == 1.0):
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

        
        # imprimir en la pantalla el cronometro
        pg.font.init()
        font = pg.font.SysFont("Chiller", 35) # crear fuente
        fuente = pg.font.Font(None,30)  # otra forma de crear fuente
        texto = font.render(f'Tiempo <{minutos}:{segundos}>', 1, NEGRO) # imprimir el
        pantalla.blit(texto, (ANCHO -170, 0))

        #imprimir por pantalla a los atributos(balas, poderes, especiales, muros, etc)´
        font = pg.font.SysFont("Chiller", 20)
        pantalla.blit(pg.transform.scale(imagenes_disparosGrandes[1],(20,20)), (ANCHO-80, 90))
        texto=  font.render(f'X {contador_balas_disparoGrande}', 1, NEGRO)
        pantalla.blit(texto, (ANCHO -50, 90))

        pantalla.blit(pg.transform.scale(imagenes_cajasEspeciales[0],(20,20)), (ANCHO-80, 110))
        texto=  font.render(f'X {contador_barril_explota}', 1, NEGRO)
        pantalla.blit(texto, (ANCHO -50, 110))

        pantalla.blit(pg.transform.scale(imagenes_cajasEspeciales[2],(20,20)), (ANCHO-80, 130))
        texto=  font.render(f'X {contador_muros}', 1, NEGRO)
        pantalla.blit(texto, (ANCHO -50, 130))

        # imprimir la puntuacion
        texto = font.render(f" SCORE: 0{puntuacion}",1,BLANCO)
        pantalla.blit(texto, (0, 20))

        
        #actualizar conteniddo de pantalla
        pg.display.flip()



