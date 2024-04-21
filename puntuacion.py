import pygame as pg
import os
from variablesMain import NEGRO ,ANCHO,ALTO

class Puntuacion():
    def __init__(self):
        self.puntuacion = 0
        self.nombreArchivoTxt = "puntuaciones.txt"
        self.textoIngresadoUsuario = ''
        self.MAX_LETTERS = 10
        self.superficieTexto = None
        self.superficieLineas = None
        
        #inicializar superficies
        font = pg.font.SysFont("Chiller", 70) # crear fuente
        self.superficieTexto = font.render(self.textoIngresadoUsuario, True, NEGRO)
        texto2 = '-' * self.MAX_LETTERS
        self.superficieLineas = font.render(texto2, True, NEGRO)
        
    def sumarPuntuacion(self, puntuacionSumar:int):
        self.puntuacion += puntuacionSumar 

    def crearArchivoPuntuacion(self):
        # verificar si el archivo existe
        if not os.path.exists(self.nombreArchivoTxt):
            # Si no existe, crear el archivo
            with open(self.nombreArchivoTxt, 'w') as file :
                file.write("indice,nombre,numeroJugadores,puntuacion,#ZombiesMuertos\n")
                for i in range(10):
                    file.write(f"{i+1},vacio,vacio,0,vacio\n")
            file.close()
        else:
            # Si ya existe, no hacer nada
            print("El archivo ya existe. No se hace nada.")

    def obtenerListaDatosDeArchivoPuntuacion(self):
        file = open(self.nombreArchivoTxt, "r")
        listaDatos = []
        for linea in file:
            # strip() eliminar espacio en blanco y salto de linea
            datos = linea.strip().split(",")
            if datos[0] == "indice":
                pass
            else:
                listaDatos.append(datos)
        # ingresaranDatos asi: [['1', ' Messi', ' 11', ' 100', '20'], ['2', ' Ronaldo', ' 11', ' 95', '20'], ['3', ' Neymar', ' 10', ' 90', '20']]
        file.close()
        return(listaDatos)
    
    def PonerNuevoValorEnListaPuntuacion(self, nombre, numeroJugadores, puntuacion, numeroZombiesMuertos):
        listaDatos= self.obtenerListaDatosDeArchivoPuntuacion()
        nuevaPuntuacion = ["11", f"{nombre}", f"{numeroJugadores}", f"{puntuacion}", f"{numeroZombiesMuertos}"]
        listaDatos.append(nuevaPuntuacion)
        # ordenar la lista por la puntuacion
        listaDatos =  sorted(listaDatos, key=lambda x: int(x[3]), reverse=True)
        # borrar el ultimo dato
        listaDatos.pop()
        #print(listaDatos)
        # Organizar el contador de indices
        contadorIndice = 1
        for array in listaDatos:
            array[0] = contadorIndice
            contadorIndice += 1 

        #print(listaDatos)
        return(listaDatos)
    
    def escribirNuevaListaEnArchivo(self, listaDatos:list):
        file = open(self.nombreArchivoTxt, "w")
        file.write("indice,nombre,numeroJugadores,puntuacion,#ZombiesMuertos\n")
        for arrayLista in listaDatos:
            cadenaArray = ','.join(map(str, arrayLista)) ## map convierte cada elemento del arreglo en un str, porque no puede tener int
            cadenaArray = f"{cadenaArray}\n"
            file.write(cadenaArray)
        file.close()

    def procesarUnaNuevaPuntuacion(self, nombre, numeroJugadores, puntuacion, numeroZombiesMuertos):
        # primero crear un archivo de puntuacion si no existe
        self.crearArchivoPuntuacion()
        # luego traer la lista de datos del archivo
        listaDatos = self.PonerNuevoValorEnListaPuntuacion(nombre, numeroJugadores, puntuacion, numeroZombiesMuertos)
        # ahora ya organizada la lista escribir en ella
        self.escribirNuevaListaEnArchivo(listaDatos)

    def imprimirEnPantalla(self, pantalla):
        font = pg.font.SysFont("Chiller", 70) # crear fuente
        texto = font.render("INGRESE SU NOMBRE", True, NEGRO)
        pantalla.blit(texto, (ANCHO/2 -200, 10))
        pantalla.blit(self.superficieTexto, (ANCHO/2 -200, 80))
        pantalla.blit(self.superficieLineas, (ANCHO/2 -200, 100))

    def procesarPuntuacion_ingresoDeTextoPantalla(self, numeroJugadores, puntuacion, numeroZombiesMuertos, pantalla):    
        # Manejo de eventos
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN: # si toca la telca enter
                    print("Texto ingresado:", self.textoIngresadoUsuario)
                    ## PROCESAR UNA NUEVA PUNTUACION
                    self.procesarUnaNuevaPuntuacion( self.textoIngresadoUsuario, numeroJugadores, puntuacion, numeroZombiesMuertos)
                    self.textoIngresadoUsuario = ''
                    return(True)
                elif event.key == pg.K_BACKSPACE: # si toca la tecla de borrar
                    self.textoIngresadoUsuario = self.textoIngresadoUsuario[:-1]
                elif len(self.textoIngresadoUsuario) < self.MAX_LETTERS: # sino entonces agregar esa entrada a la var  self.textoIngresadoUsuario
                    self.textoIngresadoUsuario += event.unicode
        
        # Renderizar texto ingresado en la pantalla
        font = pg.font.SysFont("Chiller", 70) # crear fuente
        self.superficieTexto = font.render(self.textoIngresadoUsuario, True, NEGRO)
        # screen.blit(text_surface, (10, 10))
        
        # Renderizar guión debajo del texto
        remaining_letters = self.MAX_LETTERS - len(self.textoIngresadoUsuario)
        if remaining_letters >= 0:
            underscore_text = '-' * remaining_letters
            self.superficieLineas = font.render(underscore_text, True, NEGRO)
            # screen.blit(underscore_surface, (10, 40))

        # imprimir pantalla
        # self.imprimirEnPantalla(pantalla)
        return(False)
        

