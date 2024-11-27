import pygame as pg
import math


def rotar(image, angle):
    """ROTAR UNA IMAGEN MIENTRAS MANTENEMOS SU CENTRO Y SU TAMAÑO"""

    # Obtener el centro de la imagen
    origen = image.get_rect()

    # Rotar la imagen subida en pygame
    imagen_rotada = pg.transform.rotate(image, angle)

    # Rotar la imagen basado en su centro
    rect_rotation = origen.copy()
    rect_rotation.center = imagen_rotada.get_rect().center

    # Fijar la nueva superficie rotada
    imagen_rotada = imagen_rotada.subsurface(rect_rotation).copy()

    return imagen_rotada


def calcular_lados(coords, angle):
    """CALCULA 4 PUNTOS DEL CARRO ARRIBA, ABAJO, DERECHA, IZQUIERDA"""
    tam = 50
    top_left = [
        coords[0] + math.cos(math.radians(360 - (angle + 30))) * tam,
        coords[1] + math.sin(math.radians(360 - (angle + 30))) * tam
    ]
    top_right = [
        coords[0] + math.cos(math.radians(360 - (angle + 150))) * tam,
        coords[1] + math.sin(math.radians(360 - (angle + 150))) * tam
    ]
    bottom_left = [
        coords[0] + math.cos(math.radians(360 - (angle + 210))) * tam,
        coords[1] + math.sin(math.radians(360 - (angle + 210))) * tam
    ]
    bottom_right = [
        coords[0] + math.cos(math.radians(360 - (angle + 330))) * tam,
        coords[1] + math.sin(math.radians(360 - (angle + 330))) * tam
    ]

    return [top_left, top_right, bottom_left, bottom_right]
