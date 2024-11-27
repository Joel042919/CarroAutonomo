
import sys     #Salir del programa con un código de salida
import pygame
from carro import Carro
import neat    #Manejo de algoritmos de evolución neuronal y aprendizaje



# VARIABLES CONSTANTES
ALTURA_SCREEN = 1500
ANCHO_SCREEN = 800
GENERATION = 0


# CONFIGURAMOS LA PANTALLA A MOSTRAR
pygame.display.set_caption("MANEJO AUTONOMO Y ALGORITMO GENETICO")
icono = pygame.image.load('modelocarro.png')
pygame.display.set_icon(icono)


# CARGA LA PISTA DE CARRERAS
carretera = pygame.image.load('pista.png')
    
def run_carro(genomas,config):
    # Iniciamos NEAT
    redes = []
    carros = []

    for id, adn in genomas:
        red = neat.nn.FeedForwardNetwork.create(adn, config)
        redes.append(red)
        adn.fitness = 0

        # Iniciar carros
        carros.append(Carro(carretera))

    # Iniciamos el juego
    pygame.init()
    screen = pygame.display.set_mode((
        ALTURA_SCREEN, ANCHO_SCREEN
    ))

    clock = pygame.time.Clock()
    font_generacion = pygame.font.SysFont("Arial", 70)
    font = pygame.font.SysFont("Arial", 30)

    # BUCLE PRINCIPAL
    global GENERATION
    GENERATION += 1
    while True:
        screen.blit(carretera, (0, 0))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit(0)

        #DATOS DE ENTRADA Y RESULTADOS OBTENIDOS DE LA RED
        for index, car in enumerate(carros):
            output = redes[index].activate(car.obtener_datos())
            i = output.index(max(output))
            if i == 0:
                car.angulo += 10
            else:
                car.angulo -= 10

        # ACTUALIZAR CARROS Y AJUSTAR
        carros_restantes = 0
        for i, car in enumerate(carros):
            if not(car.obtener_colision()):
                carros_restantes += 1
                car.actualizar()
                genomas[i][1].fitness += car.recompensa()

        # REVISAR
        if carros_restantes == 0:
            break

        # DIBUJANDO
        screen.blit(carretera, (0, 0))  #blit ==> dibuja (el centro de coordenadas de la pantalla es la esquina superior izquierda)
        for car in carros:
            if not(car.obtener_colision()):
                car.dibujar(screen)

        text = font_generacion.render(
            "Generacion : " + str(GENERATION), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (ANCHO_SCREEN + 300, 150)
        screen.blit(text, text_rect)

        text = font.render("Carros Restantes: " +
                           str(carros_restantes), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (ANCHO_SCREEN + 300, 200)
        screen.blit(text, text_rect)

        text = font.render("# de sensores : " +
                           str(5), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (ANCHO_SCREEN + 300, 230)
        screen.blit(text, text_rect)  

        #MOSTRAMOS LO DIBUJADO
        pygame.display.flip()  #Actualiza la ventana de la pantalla con todos los elementos que han sido dibujados en el buffer desde la última vez que se llamó a este método
        clock.tick(0)


if __name__ == "__main__":

    # CONFIGURAR EL ARCHIVO
    config_path = "./config-feedforward.txt"
    
    
    #CONFIGURAMOS LA RED NEURONAL CON EL ALGORITMO DE EVOLUCION
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    # CREAMOS UNA CLASE DEL ALGORITMO DE EVOLUCION
    p = neat.Population(config)

    # Reportar al final del juego
    p.add_reporter(neat.StdOutReporter(True))
    reporte = neat.StatisticsReporter()
    p.add_reporter(reporte)

    # CORREMOS NEAT - ESPECIFICANDO LA FUNCION DE AJUSTE Y EL MAXIMO NUMERO DE GENERACIONES
    p.run(run_carro, 1000)

