import random
import pygame as pg
import time 
import sys
# # importacion de clases creadas para el juego 
from muro import Muro, MuroExplosivo
from barraVida import BarraVida
from jugador import Jugador
from  enemigo import Enemigos_morado, Enemigos_verdes
from cajasEspeciales import CajasEspeciales
from teclado import TecladoExterminador1

from cronometro import Cronometro
from controladorSonido import ControladorSonido

# Tamaño pantalla
from main import ANCHO, ALTO
# FPS
from main import FPS
# PALETA DE COLORES RGB()
from main import NEGRO, BLANCO, ROJO, AZUL,VERDE

# imagenes para el juego
fondo = pg.transform.scale(pg.image.load("imagenes/fondo_cuidad_final.png"), (ANCHO,ALTO))



# Pantalla y clock 
from main import pantalla
from main import clock
# es volumen nulo 
from main import es_volumen_nulo
# controlador de sonifo
from main import controladorSonido



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

# Contador de puntuacion
contador_muerte_enemigos = None
puntuacion = None

# contador para el numero de enemigos
contador_poner_enemigos = None

def inicializarJuego():
    # INICIALIZAR LAS VARIABLES PARA EL FUNCIONAMIENTO DEL JUEGO 
    # Pantalla y clock , es volumen nulo  
    global pantalla
    global clock
    global es_volumen_nulo 

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

    # Contador de puntuacion
    global contador_muerte_enemigos
    global puntuacion

    # contador para el numero de enemigos
    global contador_poner_enemigos

    # controlador de sonido
    global controladorSonido
        
    # Incializar pygame
    pg.init()

    # MUSICA poner en bucle el fondo del juego 
    pg.mixer.music.load("musica/musica_fondo.mp3")# cargar musica python
    # reproducir la musica infinitamente
    pg.mixer.music.play(-1) 

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

    # Crear objetos y añadirlos al grupo de sprite jugador, teclado, barravida 
    tecladoJuador1 = TecladoExterminador1()
    jugador = Jugador(contadorMunicion_DisparoGrande= 5, contadorMunicion_BarrilExplota= 5 , contadorMunicion_Muros=5, teclado=tecladoJuador1)
    barra_vidaObjeto = BarraVida()

    # Añadir los objeto a los grupos de sprites
    sprites_jugador.add(jugador) 
    sprites_barra_vida.add(barra_vidaObjeto)

    ## Poner muros en el mapa
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




    # Contador de puntuacion y numero de muertos por enemigo 
    contador_muerte_enemigos = 0
    puntuacion = 0

    # contador para el numero de enemigos
    contador_poner_enemigos = 4

    # creacion de cronometro
    cronometro = Cronometro()
    cronometro.iniciar()

    
    #BUCLE DEL JUEGO         
    while True:
        clock.tick(FPS) # velociade de bucle

        # PARA SABER CUANDO TERMINAR EL BUCLE
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        # OBTENER EL TIEMPO DEL CRONOMETRO
        minutos, segundos, tiempo_milisegundo = cronometro.obtener_tiempo_formateado()
        tiempo_milisegundo = int(tiempo_milisegundo/100)
        # print(minutos)

        
        # CREAR ENEMIGOS CON EL TIEMPO
        if ((segundos == 2 and tiempo_milisegundo < 1) and minutos == 0) or (segundos == 30 and tiempo_milisegundo < 1) or (segundos == 59 and tiempo_milisegundo < 1):
            for i in range(contador_poner_enemigos):
                # Crear objetos de enemigos y añadirlos 
                enemigo_verde = Enemigos_verdes()
                enemigo_morado = Enemigos_morado()
                sprites_enemigos_verdes.add(enemigo_verde)
                sprites_enemigos_morados.add(enemigo_morado)
                sprites_enemigos.add(enemigo_verde)
                sprites_enemigos.add(enemigo_morado)

            contador_poner_enemigos += 2
            time.sleep(1)
    

        # ACTUALIZACION DE SPRITES
        sprites_jugador.update(jugador, sprites_balas_grandes, sprites_balas, sprites_muros, sprites_muros_explosivos) # actualizar el grupo de sprites
        sprites_enemigos.update()   # sin argumentos adicionales
        sprites_balas.update()      # sin argumentos adicionales
        sprites_barra_vida.update() # sin argumentos adicionales
        sprites_balas_grandes.update() # sin argumentos adicionales
        sprites_muros.update()      # sin argumentos adicionales
 
        # COLISIONES
        # Ojo para que sean mas precisas se necesita un radio no rectangulo. 
        # colisionSoloUno = pg.sprite.spritecollide(jugador,sprites_enemigos,False,pg.sprite.collide_circle) 
        # colisionesVarios =  pg.sprite.groupcollide(sprites_balas,sprites_enemigos,True,False,) # de esos dos grupos de sprites elimina el segundo


        # COLICION de los enemigos con las balas pequeñas
        for sprite_enemigo in sprites_enemigos:
            colision_balas_enemigo = pg.sprite.spritecollide(sprite_enemigo,sprites_balas,False,pg.sprite.collide_circle)
            if colision_balas_enemigo:
                # ya que sabemos que hubo colicion de un enemigo con alguna bala entonces borramos esa bala
                colision_balas_enemigo = pg.sprite.spritecollide(sprite_enemigo,sprites_balas,True,pg.sprite.collide_circle)
                sprite_enemigo.quitarVida(1) # se le quita vida 

                if sprite_enemigo.vidaEnemigo <= 0:
                    # poner puntos a la puntuacion
                    contador_muerte_enemigos += 1
                    puntuacion += 20

        # COLICION balas Grandes con los enemigos
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
            
        # COLICION de la bala pequeña con el muro
        for sprite_muro in sprites_muros:
            colision_balas_muros =  pg.sprite.spritecollide(sprite_muro, sprites_balas,False,pg.sprite.collide_circle)
            if colision_balas_muros:
                sprite_muro.golpeMuro(1)
                if sprite_muro.contadorDeVidaMuro <= 0:
                    sprite_muro.update()    # si es <= 0 lo elimina
                    puntuacion += 3         # poner puntuacion
        
        # COLICION de la bala grande con el muro
        for sprite_muro in sprites_muros:
            colision_balasGrandes_muro =  pg.sprite.spritecollide(sprite_muro,sprites_balas_grandes,False,pg.sprite.collide_circle)
            if colision_balasGrandes_muro:
                sprite_muro.golpeMuro(45)
                if sprite_muro.contadorDeVidaMuro <= 0:
                    sprite_muro.update()    # si es <= 0 lo elimina
                    puntuacion += 3         # poner puntuacion    



        # # COLICION de los enemigo (zombie verde) con el muro 
        # # COLICION de los  enemigo (zombie verde) con el muro - retroceder al enemigo (zombie verde
        for sprite_muro in sprites_muros:
            for sprite_enemigoVerde in sprites_enemigos_verdes:
                # vamos a ver si el muro tiene colicion con algun enemigo 
                if pg.sprite.collide_circle(sprite_muro,sprite_enemigoVerde):   
                    sprite_muro.golpeMuro(1)
                    # mover el zombie
                    sprite_enemigoVerde.rect.x += -4
                    sprite_enemigoVerde.rect.y += -4
                    # si el muro se quedo sin vida
                    if sprite_muro.contadorDeVidaMuro <= 0:
                        sprite_muro.update()    # si es <= 0 lo elimina
                        puntuacion += 3         # poner la puntuacion   


        # COLICION del enemigo (zombie morado) con el muro
        # COLICION del enemigo (zombie morado) con el muro - retroceder al enemigo (zombie morado)   
        for sprite_muro in sprites_muros:
            for sprite_enemigoMorado in sprites_enemigos_morados:
                # vamos a ver si el muro tiene colicion con algun enemigo 
                if pg.sprite.collide_circle(sprite_muro,sprite_enemigoMorado):   
                    sprite_muro.golpeMuro(2)
                    # mover el zombie morado
                    sprite_enemigoMorado.rect.x += +5
                    sprite_enemigoMorado.rect.y += +6 # va a ir escalando un poco
                    # si el muro se quedo sin vida
                    if sprite_muro.contadorDeVidaMuro <= 0:
                        sprite_muro.update()    # si es <= 0 lo elimina
                        puntuacion += 3         # poner la puntuacion   



        # COLICION del jugador con los enemigos
        colision_jugador_enemigos = pg.sprite.spritecollide(jugador, sprites_enemigos, False,pg.sprite.collide_circle)
        if colision_jugador_enemigos:
            jugador.quitarVida(1)
            jugador.activarMusica_dolorjugador() # poner musica en la clase
            # BARRA VIDA
            barra_vidaObjeto.quitarVida(1)
            if jugador.vidaJuagador <= 0:
                # print("perdio")
                return(0)
                # pg.quit()

        # CAMBIAR SPRITE
        # Cuando un zombie verde nos muerde
        for sprite_enemigo_verde in sprites_enemigos_verdes:
            colicion_enemigoVerde_jugadores = pg.sprite.spritecollide(sprite_enemigo_verde, sprites_jugador, False,pg.sprite.collide_circle)
            if colicion_enemigoVerde_jugadores: # si hay colicion de los enemigos verdes con el jugador
                # cambiando ese estado se cambia de sprite y tambien se coloca sonido de mordida
                sprite_enemigo_verde.cambiarEstadoEstarMordiendo(True) 

        # CAMBIAR SPRITE
        # Cuando un zombie morado nos muerde
        for sprite_enemigo_morado in sprites_enemigos_morados:
            colicion_enemigoMorado_jugadores = pg.sprite.spritecollide(sprite_enemigo_morado, sprites_jugador, False,pg.sprite.collide_circle)
            if colicion_enemigoMorado_jugadores:
                # cambiando ese estado se cambia de sprite y tambien se coloca sonido de mordida
                sprite_enemigo_morado.cambiarEstadoEstarMordiendo(True) 


        # COLICION de barriles explosivos con los ENEMIGOS VERDES (lo escala un poco)
        for sprite_enemigoVerde in sprites_enemigos_verdes:
            # si el enemigo tiene colicion con alguno de los muros
            colicion_enemigoVerde_murosExplosivos = pg.sprite.spritecollide(sprite_enemigoVerde,sprites_muros_explosivos,False,pg.sprite.collide_circle)
            if colicion_enemigoVerde_murosExplosivos:      
                sprite_enemigoVerde.rect.x += -5
                sprite_enemigoVerde.rect.y += -8 # se va ir un poco hacia arriba lo va a escalar

        # COLICION de barriles explosivos con los ENEMIGOS MORADOS (lo escala mucho)
        for sprite_enemigoMorado in sprites_enemigos_morados:
            # vamos a ver si el enemigo tiene colicion con alguno de los muros
            colicion_enemigoMorado_murosExplosivos = pg.sprite.spritecollide(sprite_enemigoMorado,sprites_muros_explosivos,False,pg.sprite.collide_circle)
            if colicion_enemigoMorado_murosExplosivos:      
                sprite_enemigoMorado.rect.x += 30
                sprite_enemigoMorado.rect.y += 10

        # COLICION barril_explosivo con la bala
        for sprite_muroExplosivo in sprites_muros_explosivos:
            colicion_muroExplosivo_balas = pg.sprite.spritecollide(sprite_muroExplosivo,sprites_balas,False,pg.sprite.collide_circle)
            if colicion_muroExplosivo_balas:
                # al actualizar se borran los sprites enemigos que tocan la explosion 
                sprite_muroExplosivo.update(pantalla, sprites_muros_explosivos, sprites_enemigos, es_volumen_nulo=False)
                pg.display.flip() # actualizamos pantalla
                time.sleep(0.5) # paramos un momento el juego 1/2 segundo
                sprite_muroExplosivo.kill()
                puntuacion += 15

        # COLICION barril_explosivo con la bala grande
        for sprite_muroExplosivo in sprites_muros_explosivos:
            colicion_muroExplosivo_balasGrandes = pg.sprite.spritecollide(sprite_muroExplosivo,sprites_balas_grandes,False,pg.sprite.collide_circle)
            if colicion_muroExplosivo_balasGrandes:
                # al actualizar se borran los sprites enemigos que tocan la explosion 
                sprite_muroExplosivo.update(pantalla, sprites_muros_explosivos, sprites_enemigos, es_volumen_nulo=False)
                pg.display.flip() # actualizamos pantalla
                time.sleep(0.5) # paramos un momento el juego 1/2 segundo
                sprite_muroExplosivo.kill()
                puntuacion += 15

        # DIBUJAR el fondo de la pantalla
        # Tiene que ser en el bucle porque si no quedan las imagenes represadas
        pantalla.blit(fondo,(0,0)) # imagen, (0,0) no margenes

        # DIBUJAR los grupos de sprites
        sprites_jugador.draw(pantalla)
        sprites_enemigos.draw(pantalla)
        sprites_balas.draw(pantalla) 
        sprites_muros.draw(pantalla)
        sprites_barra_vida.draw(pantalla)
        sprites_muros_explosivos.draw(pantalla)
        sprites_balas_grandes.draw(pantalla)
        
        
        # CAJAS ESPECIALES (disparos grandes)
        if segundos >= 10 and segundos < 17: # va durar la caja 5 segundos en pantalla(10-15 =5)
            if segundos == 10 and tiempo_milisegundo < 1:
                cajas_e = CajasEspeciales(1) # como es caja de disparo grande sprite(1)
                sprites_cajas_especiales.add(cajas_e)
            else:
                sprites_cajas_especiales.draw(pantalla)
                colicion_jugador_cajasEspeciales = pg.sprite.spritecollide(jugador, sprites_cajas_especiales, False,pg.sprite.collide_circle)
                # si el tiempo se paso
                if segundos == 16 and tiempo_milisegundo < 1:
                    cajas_e.kill()
                if colicion_jugador_cajasEspeciales:
                    jugador.contadorMunicionExterminador_balas_disparoGrande += (5 +(5*minutos))
                    cajas_e.kill() # como el objeto es solo uno entonces se puede eliminar directamente
                    # bool_activacionDisparo_Grande = True <-- lo va a activar presionando una tecla
                    # revisar es linea
        
        # CAJAS ESPECIALES (barril explota)
        if segundos >= 5 and segundos < 11: # va durar la caja 5 segundos en pantalla(10-15 =5)
            if segundos == 5 and tiempo_milisegundo < 1:
                cajas_barril = CajasEspeciales(0) # como es caja de barriles sprite(0)
                sprites_cajas_especiales.add(cajas_barril)
            else:
                sprites_cajas_especiales.draw(pantalla)
                colicion_jugador_cajasEspeciales = pg.sprite.spritecollide(jugador, sprites_cajas_especiales, False,pg.sprite.collide_circle)
                if segundos == 10 and tiempo_milisegundo < 1:
                    cajas_barril.kill()
                if colicion_jugador_cajasEspeciales:
                    jugador.contadorMunicionExterminador_barril_explota += (3 + 3*minutos)
                    cajas_barril.kill() # como el objeto es solo uno entonces se puede eliminar directamente
                    # bool_activacionDisparo_Grande = True <-- lo va a activar presionando una tecla
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
                    jugador.contadorMunicionExterminador_muros += (3 + 3*minutos)
                    cajas_muro.kill() # como el objeto es solo uno entonces se puede eliminar directamente
                    # bool_activacionDisparo_Grande = True <-- lo va a activar presionando una tecla
                    # revisar es linea

        # SONIDO Y CONTROLADOR DE SONIDO
        #Ojo: solo para la musica en bucle(FONDO DEL JUEGO)
        
        controladorSonido.update(pantalla) # mira si se presionaron las teclas de controlador de sonifo 

        #Poner si el volumen es nulo 
        print(es_volumen_nulo)
        
        imagenes_disparosGrandes =[ 
            pg.image.load("imagenes/disparo_grande/disparo_grande_derecha.png"),
            pg.image.load("imagenes/disparo_grande/disparo_grande_izquierda.png"),
            pg.image.load("imagenes/disparo_grande/disparo_grande_arriba.png"),
            pg.image.load("imagenes/disparo_grande/disparo_grande_abajo.png")
        ]

        imagenes_cajasEspeciales = [
            pg.image.load("imagenes/caja_barril_explota.png"),
            pg.image.load("imagenes/caja_disparo_grande.png"),
            pg.image.load("imagenes/muro_blanco.png")
        ]

        # imprimir en la pantalla el cronometro
        pg.font.init()
        font = pg.font.SysFont("Chiller", 35) # crear fuente
        fuente = pg.font.Font(None,30)  # otra forma de crear fuente
        texto = font.render(f'Tiempo <{minutos}:{segundos}>', 1, NEGRO) # imprimir el
        pantalla.blit(texto, (ANCHO -170, 0))

        #imprimir por pantalla a los atributos(balas, poderes, especiales, muros, etc)´
        font = pg.font.SysFont("Chiller", 20)
        pantalla.blit(pg.transform.scale(imagenes_disparosGrandes[1],(20,20)), (ANCHO-80, 90))
        texto=  font.render(f'X {jugador.contadorMunicionExterminador_balas_disparoGrande}', 1, NEGRO)
        pantalla.blit(texto, (ANCHO -50, 90))

        pantalla.blit(pg.transform.scale(imagenes_cajasEspeciales[0],(20,20)), (ANCHO-80, 110))
        texto=  font.render(f'X {jugador.contadorMunicionExterminador_barril_explota}', 1, NEGRO)
        pantalla.blit(texto, (ANCHO -50, 110))

        pantalla.blit(pg.transform.scale(imagenes_cajasEspeciales[2],(20,20)), (ANCHO-80, 130))
        texto=  font.render(f'X {jugador.contadorMunicionExterminador_muros}', 1, NEGRO)
        pantalla.blit(texto, (ANCHO -50, 130))

        # imprimir la puntuacion
        texto = font.render(f" SCORE: 0{puntuacion}",1,BLANCO)
        pantalla.blit(texto, (0, 20))

        
        #actualizar conteniddo de pantalla
        pg.display.flip()

inicializarJuego()

