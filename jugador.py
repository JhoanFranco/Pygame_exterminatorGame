import pygame as pg
from main import ANCHO, ALTO,ROJO
from disparo import DisparosArriba,DisparosIzquierda,DisparosDerecha,DisparosAbajo
from muro import Muro, MuroExplosivo
from controladorSonido import ControladorSonido 
from teclado import TecladoExterminador1


imagenes_exterminador_quieto = [
    pg.image.load("imagenes/exterminador/Gunner_Blue_Idle_1.png")     
]

imagenes_exterminador_correrDerecha = [
    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_1.png"),
    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_2.png"),
    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_3.png"),
    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_4.png"),
    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_5.png"),
    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_6.png")
]

imagenes_exterminador_correrIzquierda = [
    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_1.png"),
    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_2.png"),
    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_3.png"),
    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_4.png"),
    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_5.png"),
    pg.image.load("imagenes/exterminador/Gunner_Blue_Run_izquierda_6.png")
]

imagenes_exterminador_correrArriba = [
    pg.image.load("imagenes/exterminador/Gunner_Blue_arriba_1.png"),
    pg.image.load("imagenes/exterminador/Gunner_Blue_arriba_2.png"),
    pg.image.load("imagenes/exterminador/Gunner_Blue_arriba_3.png")
]

imagenes_exterminador_correrAbajo = [
    pg.image.load("imagenes/exterminador/Gunner_Blue_abajo_1.png"),
    pg.image.load("imagenes/exterminador/Gunner_Blue_abajo_2.png"),
    pg.image.load("imagenes/exterminador/Gunner_Blue_abajo_3.png")
]


class Jugador(pg.sprite.Sprite):                                                                                            ### cambiar 
    def __init__(self, contadorMunicion_BarrilExplota:int, contadorMunicion_Muros:int, contadorMunicion_DisparoGrande:int, teclado:TecladoExterminador1, esJugadorDos=False ):
        super().__init__() # heredar de la sub_clase Sprite
        self.image = pg.transform.scale(pg.image.load("imagenes/exterminador/Gunner_Blue_Idle_1.png"),(100,50))
        self.rect = self.image.get_rect() # obtener el rectangulo del sprite, es decir, de la imagen.  ojo get_rect crea un rectangulo con esa imagen
        
        # poner un radio para hacer las coliciones mas precisas
        self.radius = 27 # tiene que ser radius
        self.rect.center = (ANCHO//2, ALTO//2) # centrar el jugador al centro de la pantalla

        # velocidad del personaje(inicial) <var para dar la velocidad al personaje>
        self.velocidad_x = 0
        self.velocidad_y = 0

        # sonido
        self.sonido_disparo = pg.mixer.Sound("musica/disparo.mp3")
        self.sonido_dolor = pg.mixer.Sound("musica/dolor_jugador.mp3")

        # Banderas de movimiento
        self.movimientoExterminador_izquierda = False
        self.movimientoExterminador_derecha = False
        self.movimientoExterminador_arriba = False
        self.movimientoExterminador_abajo  = False
        self.exterminador_moviendose = False

        # contador de frames
        self.contadorFrames_exterminador_abajo = 0
        self.contadorFrames_exterminador_DerIzq = 0
        self.contadorFrames_exterminador_arriba = 0

        # bandera activacion de municion especial 
        self.bool_activacionDisparo_Grande = False
        self.bool_barril_explota = False

        # contador  de la municion especial
        self.contadorMunicionExterminador_barril_explota = contadorMunicion_BarrilExplota
        self.contadorMunicionExterminador_muros =  contadorMunicion_Muros
        self.contadorMunicionExterminador_balas_disparoGrande = contadorMunicion_DisparoGrande

        # bandera Disparar
        self.EstaDisparando = False

        # bandera sonido
        self.bool_musica_dolor_jugador = False

        # vida del jugador 
        self.vidaJuagador = 51

        # teclado 
        self.teclado = teclado

        # ver si es jugador 2
        self.bool_esJugadorDos = esJugadorDos
        self.colorRGBJuagor2 = (19,12,74)
        # cambiar color imagen jugador 2
        if self.bool_esJugadorDos:
            self.image = self.changColor(self.image, self.colorRGBJuagor2)


    def update(self, jugador, sprites_balas_grandes:pg.sprite.Group, sprites_balas:pg.sprite.Group, sprites_muros:pg.sprite.Group, sprites_muros_explosivos:pg.sprite.Group): # hereda de la clase sprite Update
        ## importar controlador de sonido
        from main import controladorSonido
        es_volumen_nulo = controladorSonido.es_volumen_nulo

        ## control_sprites
        # como hay seis frames para izq y derecha entonces los (contadorFrames_exterminador_DerIzq) sirve para la los frames de derecha y movimientoExterminador_izquierda
        if self.contadorFrames_exterminador_DerIzq >= 6:  # son 6 sprites 
            self.contadorFrames_exterminador_DerIzq = 0
        if self.contadorFrames_exterminador_arriba >= 3:  # son 3 sprites
            self.contadorFrames_exterminador_arriba = 0
        if self.contadorFrames_exterminador_abajo  >=3:  # son 3 sprites
            self.contadorFrames_exterminador_abajo = 0

        # Cambiar la imagen si el jugador  la tecla correspondiente. Va antes porque primero se toca la tecla
        if self.movimientoExterminador_derecha and self.exterminador_moviendose:
            self.image = pg.transform.scale((imagenes_exterminador_correrDerecha[self.contadorFrames_exterminador_DerIzq]), (100,50))
            self.contadorFrames_exterminador_DerIzq += 1
        elif self.movimientoExterminador_izquierda and self.exterminador_moviendose:
            self.image = pg.transform.scale((imagenes_exterminador_correrIzquierda[self.contadorFrames_exterminador_DerIzq]), (100,50))
            self.contadorFrames_exterminador_DerIzq += 1
        # para frames de movimiento vertical
        elif self.movimientoExterminador_arriba and self.exterminador_moviendose:
            self.image = pg.transform.scale((imagenes_exterminador_correrArriba[self.contadorFrames_exterminador_arriba]), (100,50))
            self.contadorFrames_exterminador_arriba += 1
        elif self.movimientoExterminador_abajo and self.exterminador_moviendose:
            self.image = pg.transform.scale((imagenes_exterminador_correrAbajo[self.contadorFrames_exterminador_abajo]),  (100,50))
            self.contadorFrames_exterminador_abajo += 1
 
        # PARA CUANDO NO ESTA MOVIENDOSE
        if self.movimientoExterminador_derecha and self.exterminador_moviendose == False:
            self.image = pg.transform.scale(pg.image.load("imagenes/exterminador/Gunner_Blue_Idle_1.png"),(100,50))
        elif self.movimientoExterminador_izquierda  and self.exterminador_moviendose == False:
            self.image = pg.transform.scale(pg.image.load("imagenes/exterminador/Gunner_Blue_Idle_izq_1.png"), (100,50))
        # para frames de movimiento vertical
        elif self.movimientoExterminador_arriba  and self.exterminador_moviendose == False:
            self.image = pg.transform.scale((imagenes_exterminador_correrArriba[1]), (100,50))
        elif self.movimientoExterminador_abajo and self.exterminador_moviendose == False:
            self.image = pg.transform.scale((imagenes_exterminador_correrAbajo[1]),  (100,50))
        
        # velocidad predeterminadad cada vuelta del bucle si no pulsas nada
        self.velocidad_x = 0
        self.velocidad_y = 0

        # comando para cuando el usuario mantiene la tecla pulsada
        teclas = pg.key.get_pressed()

        # mover el personaje izq - der
        if teclas[self.teclado.escogerTecla(self.teclado.tecla_movIzquierda[0])]:  # mover movimientoExterminador_movimientoExterminador_izquierda
            self.velocidad_x = -10
            self.movimientoExterminador_izquierda = True
            self.movimientoExterminador_derecha = False
            self.movimientoExterminador_arriba = False
            self.movimientoExterminador_abajo = False
            self.exterminador_moviendose = True
        elif teclas[self.teclado.escogerTecla(self.teclado.tecla_movDerecha[0])]:  # mover movimientoExterminador_derecha
            self.velocidad_x = 10
            self.movimientoExterminador_derecha = True
            self.movimientoExterminador_izquierda = False
            self.movimientoExterminador_arriba = False
            self.movimientoExterminador_abajo = False
            self.exterminador_moviendose = True
        # mover el personaje arr -abj
        elif teclas[self.teclado.escogerTecla(self.teclado.tecla_movArriba[0])]:   # Tecla arriba
            self.velocidad_y = -10 # quita relleno
            self.movimientoExterminador_arriba = True
            self.movimientoExterminador_abajo = False
            self.movimientoExterminador_izquierda = False
            self.movimientoExterminador_derecha = False
            self.exterminador_moviendose = True
        elif teclas[self.teclado.escogerTecla(self.teclado.tecla_movAbajo[0])]:     # Tecla mov abajo                                                    # Tecla abajo
            self.velocidad_y = 10 # pone relleno
            self.movimientoExterminador_abajo = True
            self.movimientoExterminador_arriba = False
            self.movimientoExterminador_izquierda = False
            self.movimientoExterminador_derecha = False
            self.exterminador_moviendose = True
        # si no se toca ninguna tecla
        else:
            self.exterminador_moviendose = False 

        ## SI EL JUGADOR QUIERE DISPARAR

        # Disparo grande va primero porque si es verdad pasa algo en las funciones disparo_der, izq...

        # si el jugador toca la tecla g y tiene balas grandes  ACTIVA PODER o DESACTIVA
        if teclas[self.teclado.escogerTecla(self.teclado.tecla_activarPoderDisparoGrande[0])] and self.contadorMunicionExterminador_balas_disparoGrande > 0: #Tecla activacion BalaGrande
            if self.bool_activacionDisparo_Grande == True:
                self.bool_activacionDisparo_Grande = False
            else:
                self.bool_activacionDisparo_Grande = True

        # para desactivar el poder por si solo
        if self.contadorMunicionExterminador_balas_disparoGrande <= 0:
            self.bool_activacionDisparo_Grande = False

        # DISPAROS
        if teclas[self.teclado.escogerTecla(self.teclado.tecla_colocarBala[0])] and self.movimientoExterminador_derecha == True:
           # EN VEZ DE CAMBIAR LA VELOCIDAD LLAMAMOS A QUE SE CREE UNA BALA POR EL METODO (DISPARO) 
           self.disparo_der(controladorSonido, sprites_balas_grandes, sprites_balas) 
           self.EstaDisparando = True # musica
        elif teclas[self.teclado.escogerTecla(self.teclado.tecla_colocarBala[0])] and self.movimientoExterminador_izquierda == True:
           self.disparo_izq(controladorSonido, sprites_balas_grandes, sprites_balas)
           self.EstaDisparando = True # musica
        elif teclas[self.teclado.escogerTecla(self.teclado.tecla_colocarBala[0])] and self.movimientoExterminador_abajo == True:
           self.disparo_abj(controladorSonido, sprites_balas_grandes, sprites_balas)
           self.EstaDisparando = True # musica
        elif teclas[self.teclado.escogerTecla(self.teclado.tecla_colocarBala[0])] and self.movimientoExterminador_arriba == True:
           self.disparo_Arrb(controladorSonido, sprites_balas_grandes, sprites_balas)
           self.EstaDisparando = True # musica
        elif teclas[self.teclado.escogerTecla(self.teclado.tecla_colocarBala[0])]:
            self.disparo_der(controladorSonido, sprites_balas_grandes, sprites_balas)
            self.EstaDisparando = True # musica
        
        #MUROS
        if teclas[self.teclado.escogerTecla(self.teclado.tecla_colocarPoderMuro[0])] and self.contadorMunicionExterminador_muros > 0:
            self.crear_muro(sprites_muros)
            self.contadorMunicionExterminador_muros -= 1
        if teclas[self.teclado.escogerTecla(self.teclado.tecla_colocarPoderMurosExplosivos[0])] and self.contadorMunicionExterminador_barril_explota > 0:
            self.crear_muro_exposivo(sprites_muros_explosivos)
            self.contadorMunicionExterminador_barril_explota -= 1
        else:
            pass

        # Especificar el cambio de posicion del personaje(VELOCIDAD)
        self.rect.x += self.velocidad_x 
        self.rect.y += self.velocidad_y


        # si el jugador colisiona con algun muro (NO LO DEJA AVANZAR)
        colision_muros= pg.sprite.spritecollide(jugador,sprites_muros,False,pg.sprite.collide_circle)
        if colision_muros:
            # Va a morverlo contrario a la direccion que tomo
            if teclas[self.teclado.escogerTecla(self.teclado.tecla_movIzquierda[0])]:  # mover movimientoExterminador_izquierda
                self.rect.x += 10
            elif teclas[self.teclado.escogerTecla(self.teclado.tecla_movDerecha[0])]:  # mover derecha
                self.rect.x -= 10
            # mover el personaje arr -abj
            elif teclas[self.teclado.escogerTecla(self.teclado.tecla_movArriba[0])]:  # mover arriba
                self.rect.y += 10 # pone relleno
            elif teclas[self.teclado.escogerTecla(self.teclado.tecla_movAbajo[0])]:   # mover abajo
                self.rect.y -= 10 # quita relleno
            else:
                pass
        
        ## LIMITES DE PANTALLA
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
        if self.bool_musica_dolor_jugador == True:
            if es_volumen_nulo == False:
                self.sonidoDolorjugador(controladorSonido)
                self.bool_musica_dolor_jugador = False
            else:
                pass
        
        # CAMBIAR COLOR DE SPRITE SI EL JUGADOR ES 2
        if self.bool_esJugadorDos:
            self.image = self.changColor(self.image, self.colorRGBJuagor2)

        

    def sonidoDolorjugador(self, controlador:ControladorSonido):
        self.sonido_dolor.set_volume(controlador.volumen_actual)
        self.sonido_dolor.play()

    def sonidoDisparo(self, controlador:ControladorSonido):
        self.sonido_disparo.set_volume(controlador.volumen_actual)
        self.sonido_disparo.play()

    def disparo_der(self, controladorS:ControladorSonido,sprites_balas_grandes:pg.sprite.Group, sprites_balas:pg.sprite.Group):
        # ver si el volumen es nulo
        if controladorS.es_volumen_nulo == False:
            self.sonidoDisparo(controladorS)

        # para cuado se llama a una bala pero (DISPARO GRANDE) esta activado
        if self.bool_activacionDisparo_Grande == True:
            self.contadorMunicionExterminador_balas_disparoGrande -= 1
            bala_g = DisparosDerecha(self.rect.centerx, self.rect.centery)
            bala_g.cambiarDisparoGrande()
            sprites_balas_grandes.add(bala_g)
        else:
            bala = DisparosDerecha(self.rect.centerx, self.rect.centery)
            sprites_balas.add(bala)


    def disparo_izq(self, controladorS:ControladorSonido,sprites_balas_grandes:pg.sprite.Group, sprites_balas:pg.sprite.Group):
        # ver si el volumen es nulo
        if controladorS.es_volumen_nulo == False:
            self.sonidoDisparo(controladorS)

        if self.bool_activacionDisparo_Grande:
            self.contadorMunicionExterminador_balas_disparoGrande -= 1
            bala_g = DisparosIzquierda(self.rect.centerx, self.rect.centery)
            bala_g.cambiarDisparoGrande()
            sprites_balas_grandes.add(bala_g)
        else:
            bala = DisparosIzquierda(self.rect.centerx, self.rect.centery)
            sprites_balas.add(bala)

    def disparo_abj(self, controladorS:ControladorSonido, sprites_balas_grandes:pg.sprite.Group, sprites_balas:pg.sprite.Group):
        # ver si el volumen es nulo
        if controladorS.es_volumen_nulo == False:
            self.sonidoDisparo(controladorS)

        if self.bool_activacionDisparo_Grande == True:
            self.contadorMunicionExterminador_balas_disparoGrande -= 1
            bala_g = DisparosAbajo(self.rect.centerx, self.rect.centery)
            bala_g.cambiarDisparoGrande()
            sprites_balas_grandes.add(bala_g)
        else:
            bala = DisparosAbajo(self.rect.centerx, self.rect.centery)
            sprites_balas.add(bala)

    def disparo_Arrb(self, controladorS:ControladorSonido, sprites_balas_grandes:pg.sprite.Group, sprites_balas:pg.sprite.Group):
        # ver si el volumen es nulo
        if controladorS.es_volumen_nulo == False:
            self.sonidoDisparo(controladorS)

        if self.bool_activacionDisparo_Grande == True:
            self.contadorMunicionExterminador_balas_disparoGrande -= 1
            bala_g = DisparosArriba(self.rect.centerx, self.rect.centery)
            bala_g.cambiarDisparoGrande()
            sprites_balas_grandes.add(bala_g)
        else:
            bala = DisparosArriba(self.rect.centerx, self.rect.centery)
            sprites_balas.add(bala)
          
    def crear_muro(self, sprites_muros:pg.sprite.Group):
        # hace lo mismo que la funcion disparo crea el objeto cuando lo llaman con las posiciones
        # del jugador
        muro = Muro(self.rect.centerx + 5, self.rect.centery)
        sprites_muros.add(muro)

    def crear_muro_exposivo(self, sprites_muros_explosivos:pg.sprite.Group):
        # hace lo mismo que la funcion disparo crea el objeto cuando lo llaman con las posiciones
        # del jugador
        muro_explosivo = MuroExplosivo(self.rect.centerx + 5, self.rect.centery)
        sprites_muros_explosivos.add(muro_explosivo)

    def quitarVida(self, dano:int):
        self.vidaJuagador -= dano
    
    def activarMusica_dolorjugador(self):
        self.bool_musica_dolor_jugador = True
    
    def AumentarMunicionEspecial(self, numeroSpriteCajaEspecial:int, cantidadAumentar:int):
        if(numeroSpriteCajaEspecial == 0): # barriles explosivos
            self.contadorMunicionExterminador_barril_explota += cantidadAumentar 
        elif(numeroSpriteCajaEspecial == 1): # disparo Grande
            self.contadorMunicionExterminador_balas_disparoGrande += cantidadAumentar       
        elif(numeroSpriteCajaEspecial == 2): # muros
            self.contadorMunicionExterminador_muros += cantidadAumentar     
        else:
            pass  
        
    def BorrarSprite(self):
        self.kill()

    def changColor(self, image, color):
        # Convierte la imagen en una superficie con transparencia
        image = image.convert_alpha()
        # Crea una copia de la imagen original
        final_image = image.copy()
        # Crea una superficie temporal para aplicar el color
        colored_surface = pg.Surface(image.get_size(), pg.SRCALPHA)
        # Rellena la superficie con el color dado
        colored_surface.fill((color[0], color[1], color[2], 0))
        # Mezcla la superficie coloreada con la imagen original
        final_image.blit(colored_surface, (0, 0), special_flags=pg.BLEND_RGBA_ADD)
        
        return final_image

