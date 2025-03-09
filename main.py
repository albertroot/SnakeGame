import pygame
import random

# Initialize pygame
pygame.init()

# Set display size
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 10
SNAKE_SPEED = 15

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Font and clock
FONT = pygame.font.SysFont("bahnschrift", 25)
CLOCK = pygame.time.Clock()

class SnakeGame:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.running = True
        self.snake = [[WIDTH // 2, HEIGHT // 2]]
        self.dx, self.dy = 0, 0
        self.food = self.generate_food()
        
    def generate_food(self):
        return [random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE),
                random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)]
    
    def draw_snake(self):
        for segment in self.snake:
            pygame.draw.rect(self.win, BLUE, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])
    
    def move_snake(self):
        new_head = [self.snake[-1][0] + self.dx, self.snake[-1][1] + self.dy]
        if new_head in self.snake or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
            return False
        self.snake.append(new_head)
        if new_head == self.food:
            self.food = self.generate_food()
        else:
            self.snake.pop(0)
        return True
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.dx == 0:
                    self.dx, self.dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and self.dx == 0:
                    self.dx, self.dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and self.dy == 0:
                    self.dx, self.dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and self.dy == 0:
                    self.dx, self.dy = 0, BLOCK_SIZE
    
    def run(self):
        while self.running:
            self.handle_events()
            if not self.move_snake():
                self.running = False
            self.win.fill(BLACK)
            pygame.draw.rect(self.win, GREEN, [self.food[0], self.food[1], BLOCK_SIZE, BLOCK_SIZE])
            self.draw_snake()
            pygame.display.update()
            CLOCK.tick(SNAKE_SPEED)
        pygame.quit()

if __name__ == "__main__":
    SnakeGame().run()
