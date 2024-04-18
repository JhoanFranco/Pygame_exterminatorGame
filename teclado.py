import pygame as pg

class Teclado():
    def __init__(self):
        self.dicTodasLasTeclas  = {
            'a': pg.K_a,
            'b': pg.K_b,
            'c': pg.K_c,
            'd': pg.K_d,
            'e': pg.K_e,
            'f': pg.K_f,
            'g': pg.K_g,
            'h': pg.K_h,
            'i': pg.K_i,
            'j': pg.K_j,
            'k': pg.K_k,
            'l': pg.K_l,
            'm': pg.K_m,
            'n': pg.K_n,
            'o': pg.K_o,
            'p': pg.K_p,
            'q': pg.K_q,
            'r': pg.K_r,
            's': pg.K_s,
            't': pg.K_t,
            'u': pg.K_u,
            'v': pg.K_v,
            'w': pg.K_w,
            'x': pg.K_x,
            'y': pg.K_y,
            'z': pg.K_z,
            'up arrow': pg.K_UP,
            'down arrow': pg.K_DOWN,
            'right arrow': pg.K_RIGHT,
            'left arrow': pg.K_LEFT,
            '0': pg.K_0,
            '1': pg.K_1,
            '2': pg.K_2,
            '3': pg.K_3,
            '4': pg.K_4,
            '5': pg.K_5,
            '6': pg.K_6,
            '7': pg.K_7,
            '8': pg.K_8,
            '9': pg.K_9,
            'space': pg.K_SPACE,
            'keypad 0':pg.K_KP0, 
            'keypad 1': pg.K_KP1, 
            'keypad 2': pg.K_KP2, 
            'keypad 3': pg.K_KP3, 
            'keypad 4': pg.K_KP4, 
            'keypad 5': pg.K_KP5, 
            'keypad 6': pg.K_KP6, 
            'keypad 7': pg.K_KP7, 
            'keypad 8': pg.K_KP8, 
            'keypad 9': pg.K_KP9,
            
        }
        self.listTeclasUtilizadas_todas_claves = ["1","2","3","4"]
        self.listTeclasUtilizadas_ControladorAudio_claves = ["1","2","3","4"]

    def ingresarTecla_List_todas_claves(self, tecla:str):
        if tecla not in self.listTeclasUtilizadas_todas_claves:
            self.listTeclasUtilizadas_todas_claves.append(tecla)
            return(True)
        else:
            # print("tecla ya fue ingresada, error Teclado")
            return(False)
    
    def borrarTecla_List_todas_claves(self, tecla:str):
        if tecla in self.listTeclasUtilizadas_todas_claves:
            self.listTeclasUtilizadas_todas_claves.remove(tecla)
            return(True)
        else:
            # print("tecla no esta en la lista no se puede borrar")
            return(False)
        
    def obtenerTeclaPygame(self, tecla:str):
        if tecla in self.listTeclasUtilizadas_todas_claves:
            teclaPG = self.dicTodasLasTeclas[tecla]
            return(teclaPG)
        return(None)


## TECLADO EXTERMINADOR 1
class TecladoExterminador1(Teclado):
    def __init__(self):
        super().__init__() 
        self.listTeclasUtilizadas_jugador1_claves = ["d", "a", "w", "s", "g", "r", "f","space"]
        # insertar los valores de una lista dentro de otra
        self.listTeclasUtilizadas_todas_claves.extend(self.listTeclasUtilizadas_jugador1_claves)
        #
        self.tecla_movDerecha = ["d", "movimientoDerecha"]
        self.tecla_movIzquierda = ["a", "movimientoIzquierda"]
        self.tecla_movArriba = ["w", "movimientoArriba"]
        self.tecla_movAbajo = ["s", "movimientoAbajo"]
        self.tecla_activarPoderDisparoGrande = ["g", "activarPoderDisparoGrande"]
        self.tecla_colocarPoderMurosExplosivos = ["r", "colocarPoderMurosExplosivos"]
        self.tecla_colocarPoderMuro = ["f", "colocarPoderMuro"]
        self.tecla_colocarBala = ["space", "colocarBala"]        
    
    def cambiarTecla(self, teclaVieja:str, nombreAccionTecla, teclaNueva:str):
        # tecla nueva dentro del dic como clave
        if teclaNueva in self.dicTodasLasTeclas:
            if teclaNueva not in self.listTeclasUtilizadas_jugador1_claves: 
                if (teclaVieja in self.listTeclasUtilizadas_todas_claves):
                    if(self.tecla_movDerecha[1] == nombreAccionTecla):
                        # cambiar listas 
                        self.CambiarListas_alCambiarTecla(teclaVieja,teclaNueva)
                        # self.tecla_movDerecha[0] 
                        self.tecla_movDerecha[0] = teclaNueva
                        return("Cambio correcto", True)
                    
                    elif(self.tecla_movIzquierda[1] == nombreAccionTecla):
                        # cambiar listas 
                        self.CambiarListas_alCambiarTecla(teclaVieja,teclaNueva)
                        # self.tecla_movIzquierda[0] 
                        self.tecla_movIzquierda[0] = teclaNueva
                        return("Cambio correcto", True)
                    
                    elif(self.tecla_movArriba[1] == nombreAccionTecla):
                        # cambiar listas 
                        self.CambiarListas_alCambiarTecla(teclaVieja,teclaNueva)
                        # self.tecla_movIzquierda[0] 
                        self.tecla_movArriba[0] = teclaNueva
                        return("Cambio correcto", True)
                    
                    elif(self.tecla_movAbajo[1] == nombreAccionTecla):
                        # cambiar listas 
                        self.CambiarListas_alCambiarTecla(teclaVieja,teclaNueva)
                        # self.tecla_movAbajo[0] 
                        self.tecla_movAbajo[0] = teclaNueva
                        return("Cambio correcto", True)
                    
                    elif(self.tecla_activarPoderDisparoGrande[1] == nombreAccionTecla):
                         # cambiar listas 
                        self.CambiarListas_alCambiarTecla(teclaVieja,teclaNueva)
                        # self.tecla_activarPoderDisparoGrande[0] 
                        self.tecla_activarPoderDisparoGrande[0] = teclaNueva
                        return("Cambio correcto", True)
                    
                    elif(self.tecla_colocarPoderMurosExplosivos[1] == nombreAccionTecla):
                         # cambiar listas 
                        self.CambiarListas_alCambiarTecla(teclaVieja,teclaNueva)
                        # self.tecla_colocarPoderMurosExplosivos[0] 
                        self.tecla_colocarPoderMurosExplosivos[0] = teclaNueva
                        return("Cambio correcto", True)
                    
                    elif(self.tecla_colocarPoderMuro[1] == nombreAccionTecla):
                        # cambiar listas 
                        self.CambiarListas_alCambiarTecla(teclaVieja,teclaNueva)
                        # self.tecla_colocarPoderMuro[0] 
                        self.tecla_colocarPoderMuro[0] = teclaNueva
                        return("Cambio correcto", True)
                    
                    elif(self.tecla_colocarBala[1] == nombreAccionTecla):
                        # cambiar listas 
                        self.CambiarListas_alCambiarTecla(teclaVieja,teclaNueva)
                        # self.tecla_colocarPoderMuro[0] 
                        self.tecla_colocarBala[0] = teclaNueva
                        return("Cambio correcto", True)
                    
                    else:
                        return("el nombre de la accionTecla es incorrecto", False)  
                else:
                    return("la tecla vieja no esta en la lista de teclas utilizadas", False)     
            else:
                return("la tecla nueva esta en las utilizadas por otra accion del jugador") 
        else:
            return("La tecla nueva es utilizada en otra tecla", False)
            
    def CambiarListas_alCambiarTecla(self, teclaVieja:str, teclaNueva:str):
        ## cambiar listas 
        # listTeclasUtilizadas_jugador1_claves
        indicelistTeclasUtilizadas_jugador1_claves = self.listTeclasUtilizadas_jugador1_claves.index(teclaVieja)
        self.listTeclasUtilizadas_jugador1_claves[indicelistTeclasUtilizadas_jugador1_claves] = teclaNueva
        # listTeclasUtilizadas_todas_claves
        indicelistTeclasUtilizadas_todas_claves = self.listTeclasUtilizadas_todas_claves.index(teclaVieja)
        self.listTeclasUtilizadas_todas_claves[indicelistTeclasUtilizadas_todas_claves] = teclaNueva
        
    

## TECLADO EXTERMINADOR 2
class TecladoExterminador2(Teclado):
    def __init__(self):
        super().__init__() 

        self.listTeclasUtilizadas_jugador2_claves = ['up arrow', 'down arrow', "right arrow", "left arrow", "keypad 0", "keypad 1", "keypad 2","keypad 3"]
        # insertar los valores de una lista dentro de otra
        self.listTeclasUtilizadas_todas_claves.extend(self.listTeclasUtilizadas_jugador2_claves)
        #
        self.tecla_movDerecha = ["right arrow", "movimientoDerecha"]
        self.tecla_movIzquierda = ["left arrow", "movimientoIzquierda"]
        self.tecla_movArriba = ["up arrow", "movimientoArriba"]
        self.tecla_movAbajo = ["down arrow", "movimientoAbajo"]
        self.tecla_activarPoderDisparoGrande = ["keypad 3", "activarPoderDisparoGrande"]
        self.tecla_colocarPoderMurosExplosivos = ["keypad 2", "colocarPoderMurosExplosivos"]
        self.tecla_colocarPoderMuro = ["keypad 1", "colocarPoderMuro"]
        self.tecla_colocarBala = ["keypad 0", "colocarBala"]        
    
    def cambiarTecla(self, teclaVieja:str, nombreAccionTecla, teclaNueva:str):
        # tecla nueva dentro del dic como clave
        if teclaNueva in self.dicTodasLasTeclas:
            if teclaNueva not in self.listTeclasUtilizadas_jugador2_claves: 
                if (teclaVieja in self.listTeclasUtilizadas_todas_claves):
                    if(self.tecla_movDerecha[1] == nombreAccionTecla):
                        # cambiar listas 
                        self.CambiarListas_alCambiarTecla(teclaVieja,teclaNueva)
                        # self.tecla_movDerecha[0] 
                        self.tecla_movDerecha[0] = teclaNueva
                        return("Cambio correcto", True)
                    
                    elif(self.tecla_movIzquierda[1] == nombreAccionTecla):
                        # cambiar listas 
                        self.CambiarListas_alCambiarTecla(teclaVieja,teclaNueva)
                        # self.tecla_movIzquierda[0] 
                        self.tecla_movIzquierda[0] = teclaNueva
                        return("Cambio correcto", True)
                    
                    elif(self.tecla_movArriba[1] == nombreAccionTecla):
                        # cambiar listas 
                        self.CambiarListas_alCambiarTecla(teclaVieja,teclaNueva)
                        # self.tecla_movIzquierda[0] 
                        self.tecla_movArriba[0] = teclaNueva
                        return("Cambio correcto", True)
                    
                    elif(self.tecla_movAbajo[1] == nombreAccionTecla):
                        # cambiar listas 
                        self.CambiarListas_alCambiarTecla(teclaVieja,teclaNueva)
                        # self.tecla_movAbajo[0] 
                        self.tecla_movAbajo[0] = teclaNueva
                        return("Cambio correcto", True)
                    
                    elif(self.tecla_activarPoderDisparoGrande[1] == nombreAccionTecla):
                         # cambiar listas 
                        self.CambiarListas_alCambiarTecla(teclaVieja,teclaNueva)
                        # self.tecla_activarPoderDisparoGrande[0] 
                        self.tecla_activarPoderDisparoGrande[0] = teclaNueva
                        return("Cambio correcto", True)
                    
                    elif(self.tecla_colocarPoderMurosExplosivos[1] == nombreAccionTecla):
                         # cambiar listas 
                        self.CambiarListas_alCambiarTecla(teclaVieja,teclaNueva)
                        # self.tecla_colocarPoderMurosExplosivos[0] 
                        self.tecla_colocarPoderMurosExplosivos[0] = teclaNueva
                        return("Cambio correcto", True)
                    
                    elif(self.tecla_colocarPoderMuro[1] == nombreAccionTecla):
                        # cambiar listas 
                        self.CambiarListas_alCambiarTecla(teclaVieja,teclaNueva)
                        # self.tecla_colocarPoderMuro[0] 
                        self.tecla_colocarPoderMuro[0] = teclaNueva
                        return("Cambio correcto", True)
                    
                    elif(self.tecla_colocarBala[1] == nombreAccionTecla):
                        # cambiar listas 
                        self.CambiarListas_alCambiarTecla(teclaVieja,teclaNueva)
                        # self.tecla_colocarPoderMuro[0] 
                        self.tecla_colocarBala[0] = teclaNueva
                        return("Cambio correcto", True)
                    
                    else:
                        return("el nombre de la accionTecla es incorrecto", False)  
                else:
                    return("la tecla vieja no esta en la lista de teclas utilizadas", False)     
            else:
                return("la tecla nueva esta en las utilizadas por otra accion del jugador") 
        else:
            return("La tecla nueva es utilizada en otra tecla", False)
            
    def CambiarListas_alCambiarTecla(self, teclaVieja:str, teclaNueva:str):
        ## cambiar listas 
        # listTeclasUtilizadas_jugador1_claves
        indicelistTeclasUtilizadas_jugador2_claves = self.listTeclasUtilizadas_jugador2_claves.index(teclaVieja)
        self.listTeclasUtilizadas_jugador2_claves[indicelistTeclasUtilizadas_jugador2_claves] = teclaNueva
        # listTeclasUtilizadas_todas_claves
        indicelistTeclasUtilizadas_todas_claves = self.listTeclasUtilizadas_todas_claves.index(teclaVieja)
        self.listTeclasUtilizadas_todas_claves[indicelistTeclasUtilizadas_todas_claves] = teclaNueva
        
    




