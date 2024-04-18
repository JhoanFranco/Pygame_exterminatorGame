import pygame as pg
import sys
from button import Button
from  logicaJuegoAnterior import inicializarJuego

ANCHO, ALTO = 1000,600
FPS = 10
NEGRO = (0,0,0)

pg.init()
screen = pg.display.set_mode((ANCHO,ALTO))
pg.display.set_caption("Menu")
clock = pg.time.Clock()

# Background
Background = pg.transform.scale(pg.image.load("imagenes/fondoMenu.png"),(ANCHO,ALTO))


# Font 
fontHallowen = pg.font.Font("fuentes/HalloweenFont.otf", 50)

# squareImage
imageSquare = pg.image.load("imagenes/cuadroSinFondo.png")
posxDraw, posyDraw = 0, 0
squareDraw = pg.draw.rect(screen,(200,200,200),(posxDraw,posyDraw,100,100))# the other 100, 100 are the size of the draw

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

listButtonsMain = [buttonInstructions, buttonPlay, buttonOption, buttonExit]
listButtonMenuOption = [buttonBack]
listButtonMenuInstruction = [buttonBack]

# menu de opciones 
def menuOption():
    while True:
        positionMouse = pg.mouse.get_pos() # obtener la posicion del mouse en la ventana de pygame 
        Background2 = pg.transform.scale(pg.image.load("imagenes/fondoMenu2.png"),(ANCHO,ALTO)) # ponerle el fondo 
        screen.blit(Background2, (0,0)) #Whitout margin, poner el fondo 

        # por cada boton en la lista ponerlo en la pantalla
        for button in listButtonMenuOption:
            button.update(screen)
            button.updateColor(positionMouse) # para actualizar el color  si el mouse toca el boton 

        # para coger los eventos o click del mouse 
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in listButtonMenuOption:
                    if button.checkoutPositionInside(positionMouse):
                        nombreButton = button.inputText
                        # para devolverse al menu principal 
                        if nombreButton == "Back":
                            principalMenu()
                   
        # fontHallowen = pg.font.Font("fuentes/HalloweenFont.otf", 25) # crear fuente
        # texto = fontHallowen.render(
        #     """  
        #     ↑ correr arriba el exterminador \n
        #     ↓ correr abajo el exterminador \n
        #     → correr derecha el exterminador \n
        #     ← correr izquierda el exterminador \n

        #     """
        #     , 1, NEGRO) # imprimir el
        # screen.blit(texto, (100, 100))


        pg.display.update() #actualizar el contenido de la pantalla
        clock.tick(60) #60fps

def menuInstrucciones():
    while True:
        positionMouse = pg.mouse.get_pos() # obtener la posicion del mouse en la ventana de pygame 
        # instrucciones
        BackgroundInstrucciones = pg.transform.scale(pg.image.load("imagenes/Instrucciones.png"),(ANCHO,ALTO))
        screen.blit(BackgroundInstrucciones, (0,0)) #Whitout margin, poner el fondo 

        # por cada boton en la lista ponerlo en la pantalla
        for button in listButtonMenuInstruction :
            button.update(screen)
            button.updateColor(positionMouse) # para actualizar el color  si el mouse toca el boton 

        # para coger los eventos o click del mouse 
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in listButtonMenuInstruction:
                    if button.checkoutPositionInside(positionMouse):
                        nombreButton = button.inputText
                        # para devolverse al menu principal 
                        if nombreButton == "Back":
                            principalMenu()

        pg.display.update() #actualizar el contenido de la pantalla
        clock.tick(60) #60fps



# menu principal del juego 
def principalMenu():
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
                            inicializarJuego()
                            print("llamar el juego")
                        # llamar al menu de instrucciones     
                        elif button.inputText == "Instructions":   
                            menuInstrucciones()
                        # salir del juego 
                        elif button.inputText == "Exit":
                            print("salir del juego")
                            pg.quit()

        # poner otra vez los botones 
        screen.blit(Background,(0,0)) # Whitout Margin in the backgrounds

        for i in listButtonsMain:
            i.update(screen=screen)
            i.updateColor(positionMouse)

        # look position in the screen
        screen.blit(fontHallowen.render(f"{positionMouse}",True, "White"),(800,200))

        pg.display.flip() #Update content in the screen
        clock.tick(60) #60fps


#principalMenu()


