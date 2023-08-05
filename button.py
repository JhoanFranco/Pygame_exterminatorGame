import pygame as pg
import sys



class Button():
    def __init__(self, image, position, inputText, fontText, RGBcolor = None, hoveringColor = None):
        """This is the constructor class of Button
        Args:
            image (_type_): _description_
            position (tuple): is a tuple of two values (valuex, valuey)
            inputText (string): Is the text of the box 
            fontText (String): Is the type pf font of the text like "pg.font.Font("dir_font", size)"
            RGBcolor (_type_): _description_
            HoveringColor (_type_): _description_
        if colors are NONE then the color is white
        """
        self.image = image
        self.positionx = position[0]
        self.positiony = position[1]
        self.inputText = inputText
        self.font = fontText
        self.BoolHooveringColor = False
        # if the colors are initialized to none 
        # then the color will be white
        if RGBcolor == None:
            self.RGBcolor = (255,255,255) #white
        else:
            self.RGBcolor = RGBcolor
        if hoveringColor == None:
            self.hoveringColor = (255,255,255) #white
        else:
            self.hoveringColor = hoveringColor
        # Here we are naming a variable "text" that will already have the 
        # values ready to just do a blit and show the text on the screen
        self.text = self.font.render(inputText,True,RGBcolor)
        if image == None:
            self.image = self.text
        # specifically we are giving the center for then 
        # pygame accommodate the coordinates according to that center and the inner values of the img or text
        self.rectImage = self.image.get_rect(center=(self.positionx,self.positiony))
        self.rectText = self.text.get_rect(center=(self.positionx,self.positiony))
        print(f"the position given was: {position}")
        print(f" text with get rect {self.rectImage}, img with get rect {self.rectImage}")
        # ojo: rectobject <left,top,widht, height>

    def update(self, screen):
        """This method allows draw in the screen the button
        Args:
            screen (_type_): is the superface
        """
        if self.image != self.text:
            # print("se ejecuto update y la imagen existe")
            screen.blit(self.image , self.rectImage)
            screen.blit(self.text, self.rectText)
        else: 
            # print(" se ejecuto update y la imagen no existe")
            screen.blit(self.text,self.rectText)

    def checkoutPositionInside(self,positionMouse):
        """This method is for see if the position of the mouse 
        is inside of the box
        Args
            positionMouse (tuple): is a tuple of two values (x,y)
        """
        # Remember rectobject <left,top,widht, height> # Also keep in mmind wight and height always postives
        pmx, pmy = positionMouse[0], positionMouse[1]
        if self.image != self.text:
            position = self.rectImage
            posleft, posRight = position[0], position[0] + position[2]
            posUp, posDown = position[1], position[1] + position[3]
            if (pmx >= posleft and pmx <=posRight) and (pmy >= posUp and pmy <= posDown): # if position mouse is within this ranges then is inside
                return(True)
            else:
                return(False)
            
    def updateColor(self,positionMouse):
        """This methods is for update the color of the button if the postion of Mouse
            is inside the Button 
        Args:
            positionMouse (tuple): is a tuple of two values (x,y)
        """
        choice = self.checkoutPositionInside(positionMouse)
        if choice == True and self.BoolHooveringColor == False:
            self.text = self.font.render(self.inputText,True,self.hoveringColor)
            self.BoolHooveringColor = True
        elif choice == False and self.BoolHooveringColor == True:
            self.text = self.font.render(self.inputText,True,self.RGBcolor)
            self.BoolHooveringColor = False
        else:
            pass