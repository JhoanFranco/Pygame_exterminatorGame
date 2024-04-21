import pygame as pg
import sys
from button import Button
from  mainVariables import pantalla, clock, BLANCO,NEGRO, controladorSonido
from  logicaJuego import iniciarJuego

ANCHO, ALTO = 1000,600
FPS = 10
NEGRO = (0,0,0)

pg.init()

pg.display.set_caption("Menu")

pg.mixer.music.load("musica/Music Ever_ Everything Ends Here.mp3")# cargar musica python
    # reproducir la musica infinitamente
pg.mixer.music.play(-1)

#icono
icono = pg.image.load("imagenes\zombies\zombies_morado_der_2.png")
icono = pg.transform.scale(icono,(20,20))
pg.display.set_icon(icono)

# Background
Background = pg.transform.scale(pg.image.load("imagenes/fondos/fondoMenu.png"),(ANCHO,ALTO))

# Font 
fontHallowen = pg.font.Font("fuentes/HalloweenFont.otf", 50)

# squareImage
imageSquare = pg.image.load("imagenes/fondos/cuadroSinFondo.png")
posxDraw, posyDraw = 0, 0
squareDraw = pg.draw.rect(pantalla,(200,200,200),(posxDraw,posyDraw,100,100))# the other 100, 100 are the size of the draw

# Creacion de botones 
buttonInstructionSquare = pg.transform.scale(imageSquare,(400,100))
buttonInstructions= Button(buttonInstructionSquare,(500,380), "Instructions", fontHallowen,(0,0,0),(240,94,46))

buttonPlaySquare = pg.transform.scale(imageSquare,(300,80))
buttonPlay= Button(buttonPlaySquare,(500,120), "Play",fontHallowen,(0,0,0),(240,94,46))

buttonBackSquare = pg.transform.scale(imageSquare,(150,70))
buttonBack = Button(buttonBackSquare,(900,50),"Back", fontHallowen, (0,0,0),(240,94,46))

buttonOptionSquare = pg.transform.scale(imageSquare,(250,80))
buttonOption = Button(buttonBackSquare,(500,250),"Options", fontHallowen, (0,0,0),(240,94,46))

buttonExitSquare = pg.transform.scale(imageSquare,(250,80))
buttonExit = Button(buttonExitSquare,(500,500),"Exit", fontHallowen, (0,0,0),(240,94,46))

buttonScoreSquare = pg.transform.scale(imageSquare,(250,80))
buttonScore = Button(buttonScoreSquare,(800,550), "Score",fontHallowen,(0,0,0),(240,94,46))


buttonPlayersOneSquare = pg.transform.scale(imageSquare,(300,80))
buttonPlayersOne = Button(buttonPlayersOneSquare,(500,120), "One player",fontHallowen,(0,0,0),(240,94,46))

buttonPlayersTwoSquare = pg.transform.scale(imageSquare,(300,80))
buttonPlayersTwo = Button(buttonPlayersTwoSquare,(500,250), "Two player",fontHallowen,(0,0,0),(240,94,46))

buttonInstructions2Square = pg.transform.scale(imageSquare,(250,80))
buttonInstructions2 = Button(buttonInstructions2Square,(850,550), "Instructions2",fontHallowen,(0,0,0),(240,94,46))



listButtonsMain = [buttonInstructions, buttonPlay, buttonOption, buttonExit, buttonScore]
listButtonMenuOption = [buttonBack]
listButtonMenuInstruction = [buttonBack, buttonInstructions2]
listButtonMenuInstruction2 = [buttonBack]
listButtonMenuPlay = [buttonBack, buttonPlayersOne, buttonPlayersTwo]
listButtonMenuScore =[buttonBack]


# menu de opciones 
def menuOption():
    while True:
        positionMouse = pg.mouse.get_pos() # obtener la posicion del mouse en la ventana de pygame 
        Background2 = pg.transform.scale(pg.image.load("imagenes/fondos/fondoMenu2.png"),(ANCHO,ALTO)) # ponerle el fondo 
        pantalla.blit(Background2, (0,0)) #Whitout margin, poner el fondo 

        # por cada boton en la lista ponerlo en la pantalla
        for button in listButtonMenuOption:
            button.update(pantalla)
            button.updateColor(positionMouse) # para actualizar el color  si el mouse toca el boton 

        controladorSonido.update(pantalla)
        
        # para coger los eventos o click del mouse 
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in listButtonMenuOption:
                    if button.checkoutPositionInside(positionMouse):
                        nombreButton = button.inputText
                        # para devolverse al menu principal 
                        if nombreButton == "Back":
                            menuPrincipal()
                   

        pg.display.update() #actualizar el contenido de la pantalla
        clock.tick(60) #60fps


# menu de opciones 
def menuScores():
    while True:
        positionMouse = pg.mouse.get_pos() # obtener la posicion del mouse en la ventana de pygame 
        Background2 = pg.transform.scale(pg.image.load("imagenes/fondos/fondoMenu2.png"),(ANCHO,ALTO)) # ponerle el fondo 
        pantalla.blit(Background2, (0,0)) #Whitout margin, poner el fondo 

        # por cada boton en la lista ponerlo en la pantalla
        for button in listButtonMenuScore:
            button.update(pantalla)
            button.updateColor(positionMouse) # para actualizar el color  si el mouse toca el boton 

        controladorSonido.update(pantalla)
        # para coger los eventos o click del mouse 
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in listButtonMenuScore:
                    if button.checkoutPositionInside(positionMouse):
                        nombreButton = button.inputText
                        # para devolverse al menu principal 
                        if nombreButton == "Back":
                            menuPrincipal()

        try:
            with open("puntuaciones.txt", "r") as file:
                altoDeMas = 0
                for linea in file:
                    if altoDeMas == 0:
                        linea_sinComas = linea.replace(",", " ")
                        linea_saltoLinea = linea_sinComas.replace("\n", " ") 

                        fontHallowen = pg.font.Font("fuentes/HalloweenFont.otf", 35) # crear fuente
                        texto = fontHallowen.render(linea_saltoLinea, True,BLANCO)
                        pantalla.blit(texto,(100,100 +altoDeMas))
                        altoDeMas += 35
                    else:
                        campos = linea.strip().split(",")
                        campos_justificados = [campo.ljust(13) for campo in campos]
                        linea_formateada = " ".join(campos_justificados)
                        
                        # Renderizar y mostrar la línea en la pantalla
                        texto = fontHallowen.render(linea_formateada, True, NEGRO)
                        pantalla.blit(texto, (100, 100 + altoDeMas))
                        altoDeMas += 25

        except FileNotFoundError:
            print("¡El archivo no fue encontrado!")
                    
       
        pg.display.update() #actualizar el contenido de la pantalla
        clock.tick(60) #60fps


def menuInstrucciones():
    while True:
        positionMouse = pg.mouse.get_pos() # obtener la posicion del mouse en la ventana de pygame 
        # instrucciones
        BackgroundInstrucciones = pg.transform.scale(pg.image.load("imagenes/instrucciones/Instrucciones1.png"),(ANCHO,ALTO))
        pantalla.blit(BackgroundInstrucciones, (0,0)) #Whitout margin, poner el fondo 

        # por cada boton en la lista ponerlo en la pantalla
        for button in listButtonMenuInstruction :
            button.update(pantalla)
            button.updateColor(positionMouse) # para actualizar el color  si el mouse toca el boton 

        controladorSonido.update(pantalla)
        # para coger los eventos o click del mouse 
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in listButtonMenuInstruction:
                    if button.checkoutPositionInside(positionMouse):
                        nombreButton = button.inputText
                        # para devolverse al menu principal 
                        if nombreButton == "Back":
                            menuPrincipal()
                        if nombreButton == "Instructions2":
                            menuInstrucciones2()
                            


        pg.display.update() #actualizar el contenido de la pantalla
        clock.tick(60) #60fps



def menuInstrucciones2():
    while True:
        positionMouse = pg.mouse.get_pos() # obtener la posicion del mouse en la ventana de pygame 
        # instrucciones
        BackgroundInstrucciones = pg.transform.scale(pg.image.load("imagenes/instrucciones/Instrucciones2.png"),(ANCHO,ALTO))
        pantalla.blit(BackgroundInstrucciones, (0,0)) #Whitout margin, poner el fondo 

        # por cada boton en la lista ponerlo en la pantalla
        for button in listButtonMenuInstruction2 :
            button.update(pantalla)
            button.updateColor(positionMouse) # para actualizar el color  si el mouse toca el boton 

        controladorSonido.update(pantalla)
        # para coger los eventos o click del mouse 
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in listButtonMenuInstruction2:
                    if button.checkoutPositionInside(positionMouse):
                        nombreButton = button.inputText
                        # para devolverse al menu principal 
                        if nombreButton == "Back":
                            menuInstrucciones()

        pg.display.update() #actualizar el contenido de la pantalla
        clock.tick(60) #60fps

def menuPlay():
    while True:
        positionMouse = pg.mouse.get_pos() # obtener la posicion del mouse en la ventana de pygame 
        # instrucciones
        BackgroundInstrucciones = pg.transform.scale(pg.image.load("imagenes/fondos/fondoMenu2.png"),(ANCHO,ALTO))
        pantalla.blit(BackgroundInstrucciones, (0,0)) #Whitout margin, poner el fondo 

        # por cada boton en la lista ponerlo en la pantalla
        for button in listButtonMenuPlay :
            button.update(pantalla)
            button.updateColor(positionMouse) # para actualizar el color  si el mouse toca el boton 

        controladorSonido.update(pantalla)
        # para coger los eventos o click del mouse 
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in listButtonMenuPlay:
                    if button.checkoutPositionInside(positionMouse):
                        nombreButton = button.inputText
                        # para devolverse al menu principal 
                        if nombreButton == "Back":
                            menuPrincipal()
                        elif nombreButton == "One player":
                            pg.mixer.music.stop()
                            iniciarJuego(1)
                        elif nombreButton == "Two player":
                            pg.mixer.music.stop()
                            iniciarJuego(2)

        pg.display.update() #actualizar el contenido de la pantalla
        clock.tick(60) #60fps


# menu principal del juego 
def menuPrincipal():
    while True:
        positionMouse = pg.mouse.get_pos() # position of Mouse  

        for event in pg.event.get():
            if event.type == pg.QUIT:
                print(event.type)
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                print("someone Click")
                for button in listButtonsMain:
                    if button.checkoutPositionInside(positionMouse):
                        # llamar al menu de opciones
                        if button.inputText == "Options":
                            menuOption()
                        # LLAMAR AL JUEGO 
                        elif button.inputText == "Play":
                            menuPlay()
                            print("llamar el juego")
                        # llamar al menu de instrucciones     
                        elif button.inputText == "Instructions":   
                            menuInstrucciones()
                        # salir del juego 
                        elif button.inputText == "Exit":
                            print("salir del juego")
                            pg.quit()
                        # puntuacion
                        elif button.inputText == "Score":
                            menuScores()

        # poner otra vez los botones 
        pantalla.blit(Background,(0,0)) # Whitout Margin in the backgrounds
        controladorSonido.update(pantalla)
        for button in listButtonsMain:
            button.update(pantalla)
            button.updateColor(positionMouse)

        # look position in the pantalla
        # pantalla.blit(fontHallowen.render(f"{positionMouse}",True, "White"),(800,200))

        pg.display.flip() #Update content in the pantalla
        clock.tick(60) #60fps



