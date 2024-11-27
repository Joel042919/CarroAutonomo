import math

import pygame as pg
from sensor import rotar, calcular_lados


# CONSTANTES
ANCHO = 100
ALTURA = 100
COLOR_RADAR = (0,0,255) 
COLOR_BLANCO = (255,255,255,255)

class Carro(object):
    
    def __init__(self, carretera):
        self.carretera = carretera;
        self.modeloCar = pg.image.load('modeloCarro.png')
        self.modeloCar = pg.transform.scale(self.modeloCar, (ANCHO,ALTURA))
        self.rotarCarro = self.modeloCar
        self.x_pos = 600  #600
        self.y_pos = 655  #655
        self.veloc = 10
        self.angulo = 0
        self.distancia = 0
        self.colision = False
        self.puntos_colision = []
        self.radares = []
        self.centro = [self.x_pos+50, self.y_pos+50]
        
    def dibujar(self, screen):
        screen.blit(self.rotarCarro, [self.x_pos, self.y_pos]) 
        self.dibujar_radar(screen)
        
    def actualizar(self):
        self.distancia += self.veloc
        
        self.x_pos += math.cos(math.radians(360-self.angulo))* self.veloc
        self.y_pos += math.sin(math.radians(360-self.angulo))* self.veloc
        self.centro = [int(self.x_pos+50), int(self.y_pos +50)]
        self.rotarCarro = rotar(self.modeloCar, self.angulo)
        
        self.actualizar_puntos_colision()
        self.revisar_colision()
        self.radares.clear()  
        
        #DIBUJAMOS LOS RADARES EN LOS ANGULOS DADOS -90 -45 0 45 90
        #Le pondremos 5 sensores  
        sensores = [-90,-45,0,45,90]
        for grado in sensores:
            self.actualizar_radar(grado)
            
    def actualizar_radar(self, grado):
        largo = 0
        
        #CALCULAR EL CENTRO "X" y "Y" DEL CARRO, CONSIDERANDO SU ROTACION
        x_pos = int(
            self.centro[0]+math.cos(
                math.radians(360-(self.angulo+grado))
            )*largo
        )
        y_pos = int(
            self.centro[1]+math.sin(
                math.radians(360-(self.angulo+grado))
            )*largo
        )  
        
        #REVISAMOS QUE EL PIXEL CALCULADO NO ESTA FUERA DEL RANGO
        try:
            pixel=self.carretera.get_at((x_pos,y_pos))
        except IndexError:
            pixel = COLOR_BLANCO;
            
        #REVISAR SI UNO DE LOS LADOS ESTA FUERA DE LA CARRETERA
        while pixel != COLOR_BLANCO and largo<300:
            try:
                #OBTENER EL PUNTO MAS LEJANO
                pixel = self.carretera.get_at((x_pos,y_pos))
            except IndexError:
                pixel = COLOR_BLANCO
            else:
                largo = largo+1
            
            #ACTUALIZAR VALORES DE X y Y
            x_pos = int(
                self.centro[0] + math.cos(
                    math.radians(360 - (self.angulo + grado))
                ) * largo
            )
            
            y_pos = int(
                self.centro[1] + math.sin(
                    math.radians(360 - (self.angulo + grado))
                ) * largo
            )
            
        #OBTENER EL LADO VERTICAL Y HORIZONTAL DEL CARRO
        horizontal = math.pow(x_pos - self.centro[0], 2)
        vertical = math.pow(y_pos - self.centro[1], 2)
            
        #SI OBTENEMOS LA HIPOTENUSA DEL TRIANGULO,
        #OBTENEMOS TAMBIEN LA DISTANCIA DEL RADAR
            
        distanciaRadar = int(math.sqrt(horizontal+vertical))
        self.radares.append([(x_pos,y_pos),distanciaRadar])
        
    
    def dibujar_radar(self, screen):
        self.obtener_datos()
        for radar in self.radares:
            position, _ = radar
            pg.draw.line(screen, COLOR_RADAR,self.centro, position,1)
            pg.draw.circle(screen, COLOR_RADAR, position,2)
            
    def actualizar_puntos_colision(self):
        self.puntos_colision = calcular_lados(self.centro, self.angulo)
        
    def revisar_colision(self):
        self.colision = False
        
        for punto in self.puntos_colision:
            try:
                if self.carretera.get_at((
                    int(punto[0]),int(punto[1])
                )) == COLOR_BLANCO:
                    self.colision=True
                    break
            except:
                self.colision = True
    
    
    def obtener_colision(self):
        return self.colision
    
    def recompensa(self):
        return self.distancia/50.0
    
    def obtener_datos(self):
        capaEntrada = []
        for i in range(5):
            capaEntrada.append(0)
        
        for i, radar in enumerate(self.radares):
            capaEntrada[i] = int(radar[1]/30)
        return capaEntrada
        
            
        
            
            
                
        
        
        
        
        
        
        
        
        
               

