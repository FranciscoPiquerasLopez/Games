import pygame
from tkinter import messagebox
from tkinter import *
from Snake import Snake
from Food import Food

class Tablero:
    def __init__(self, width, height):
        self.running = True
        self.width = width
        self.height = height

        # Inicializar Pygame
        pygame.init()

        # Crear la pantalla
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Snake Game')

        # Definir dimensiones del juego
        self.grid_size = 20
        self.snake_size = 20
        self.fps = 10

        self.clock = pygame.time.Clock()

        # Inicializar elementos del juego
        self.snake = Snake(100, 100, self.snake_size)
        self.food = Food(self.snake_size, self.width, self.height)

    def show_game_over(self):
        messagebox.showinfo('Derrota','Has perdido')

    def run(self):
        running = True
        direction = 'RIGHT'

        while running:
            self.screen.fill("BLACK")

            # Manejo de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and direction != 'DOWN':
                        direction = 'UP'
                    elif event.key == pygame.K_DOWN and direction != 'UP':
                        direction = 'DOWN'
                    elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                        direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                        direction = 'RIGHT'

            # Mover la serpiente
            self.snake.move(direction, self.snake_size)

            # Comprobar colisiones con la comida
            if self.snake.body[0] == self.food.pos:
                self.snake.grow()
                self.food.pos = self.food.generate_position()

            if len(self.snake.body) > 1:
                # Comprobar colisiones contra sí misma, en este caso la partida se acaba
                self.head_x = self.snake.body[0][0] # Coordenada x
                self.head_y = self.snake.body[0][1] # Coordenada y
                for part in self.snake.body[2:]:
                    x = part[0]
                    y = part[1]

                    # En caso de perder, le avisamos y cerramos el bucle de ejecución principal del programa
                    if self.head_x == x and self.head_y == y:
                        self.show_game_over()
                        running = False

            # Dibujar elementos del juego
            self.snake.draw(self.screen)
            self.food.draw(self.screen)

            pygame.display.flip()
            # Configuramos las velocidades del programa para aumentar la dificultad
            if len(self.snake.body) > 10 and len(self.snake.body) < 20:
                self.fps = 12
            elif len(self.snake.body) > 20:
                self.fps = 15
            # Establecemos los fps(fotogramas por segundo que tendrá nuestra aplicación)
            self.clock.tick(self.fps)

        pygame.quit()

# Crear una instancia de la clase Tablero para iniciar el juego
tablero = Tablero(600, 400)
tablero.run()