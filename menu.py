import pygame as pg
import sys
from button import Button

ANCHO, ALTO = 1000,600
FPS = 10

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

# Creation of Bottons
buttonInstructionSquare = pg.transform.scale(imageSquare,(400,100))
buttonInstructions= Button(buttonInstructionSquare,(500,400), "Instructions", fontHallowen,(0,0,0),(240,94,46))

buttonPlaySquare = pg.transform.scale(imageSquare,(300,80))
buttonPlay= Button(buttonPlaySquare,(500,80), "Play",fontHallowen,(0,0,0),(240,94,46))

buttonBackSquare = pg.transform.scale(imageSquare,(150,70))
buttonBack = Button(buttonBackSquare,(900,50),"Back", fontHallowen, (0,0,0),(240,94,46))

buttonOptionSquare = pg.transform.scale(imageSquare,(250,80))
buttonOption = Button(buttonBackSquare,(500,250),"Options", fontHallowen, (0,0,0),(240,94,46))

buttonOptionSquare = pg.transform.scale(imageSquare,(250,80))
buttonOption = Button(buttonBackSquare,(500,250),"Options", fontHallowen, (0,0,0),(240,94,46))

listButtonsMain = [buttonInstructions, buttonPlay, buttonOption]
listMenuOption = [buttonBack]

def menuOption():
    while True:
        positionMouse = pg.mouse.get_pos()
        Background2 = pg.transform.scale(pg.image.load("imagenes/fondoMenu2.png"),(ANCHO,ALTO))
        screen.blit(Background2, (0,0)) #Whitout margin

        for button in listMenuOption:
            button.update(screen)
            button.updateColor(positionMouse)


        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                for button in listMenuOption:
                    if button.checkoutPositionInside(positionMouse):
                        nombreButton = button.inputText
                        if nombreButton == "Back":
                            principalMenu()
                            
        pg.display.update() #Update content in the screen but a small portion
        clock.tick(60) #60fps

     
def menuPlay():
    while True:
        positionMouse = pg.mouse.get_pos()
        Background2 = pg.transform.scale(pg.image.load("imagenes/fondoMenu2.png"),(ANCHO,ALTO))
        screen.blit(Background2, (0,0)) #Whitout margin

        for button in listMenuOption:
            button.update(screen)
            button.updateColor(positionMouse)

    



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
                        if button.inputText == "Options":
                            menuOption()
                        elif button.inputText == "Play":
                            # llamar al juego
                            print("llamar el juego")

        screen.blit(Background,(0,0)) # Whitout Margin in the background

        for i in listButtonsMain:
            i.update(screen=screen)
            i.updateColor(positionMouse)


        # look position in the screen
        screen.blit(fontHallowen.render(f"{positionMouse}",True, "White"),(800,200))


        pg.display.flip() #Update content in the screen
        clock.tick(60) #60fps

principalMenu()


