import pygame as pg
from variablesMain import ANCHO, ALTO

imagenes_barraVida = [
    pg.image.load("imagenes/barra_vida/barraVida_1.png"),
    pg.image.load("imagenes/barra_vida/barraVida_2.png"),
    pg.image.load("imagenes/barra_vida/barraVida_3.png"),
    pg.image.load("imagenes/barra_vida/barraVida_4.png"),
    pg.image.load("imagenes/barra_vida/barraVida_5.png"),
    pg.image.load("imagenes/barra_vida/barraVida_6.png")
]

class BarraVida(pg.sprite.Sprite):
   def __init__(self, numeroJugador=1):
      super().__init__()
      self.image = pg.transform.scale(imagenes_barraVida[0],(100,100))
      
      # posicion 
      self.rect = self.image.get_rect()
      self.rect.x = ANCHO -100
      self.rect.y = 15

      # contadorVida
      self.contadorVida = 51
      self.barraVida_Numerojugador = numeroJugador

      if self.barraVida_Numerojugador == 2:
         self.rect.x = ANCHO -100
         self.rect.y = 140

   def update(self):
      if self.contadorVida >= 0 and  self.contadorVida < 11 :
         self.image = pg.transform.scale(imagenes_barraVida[5],(100,100)) 
      elif self.contadorVida >= 11 and  self.contadorVida < 21:
         self.image = pg.transform.scale(imagenes_barraVida[4],(100,100)) 
      elif self.contadorVida >= 21 and self.contadorVida < 31:
         self.image = pg.transform.scale(imagenes_barraVida[3],(100,100))
      elif self.contadorVida >= 31 and self.contadorVida  < 41:
         self.image = pg.transform.scale(imagenes_barraVida[2],(100,100)) 
      elif self.contadorVida  >= 41 and self.contadorVida < 51 :
         self.image = pg.transform.scale(imagenes_barraVida[1],(100,100)) 
      else:
         self.image = pg.transform.scale(imagenes_barraVida[0],(100,100)) 
   
   
   def quitarVida(self, danoGolpe:int):
       self.contadorVida -= danoGolpe

   def PonerNumeroJugadorPerteneceBarraVida(self, numeroJugador:int):
      self.barraVida_Numerojugador = numeroJugador

   def CambiarPosicionBarraVida(self, x:int, y:int):
      self.rect.x = ANCHO -100 -x
      self.rect.y = y

   def aumentarVida(self, cantidadAumentar):   
      if (self.contadorVida + cantidadAumentar) >= 51:
            self.contadorVida = 51
      else:
            self.contadorVida += cantidadAumentar


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
        
   