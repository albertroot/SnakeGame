import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set display size
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake settings
snake_block = 10
snake_speed = 15

# Font and clock
font = pygame.font.SysFont("bahnschrift", 25)
clock = pygame.time.Clock()

def message(msg, color, x, y):
    mesg = font.render(msg, True, color)
    win.blit(mesg, [x, y])

def game_loop():
    game_over = False
    game_close = False
    
    x, y = width / 2, height / 2
    dx, dy = 0, 0
    
    snake = []
    snake_length = 1
    
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    
    while not game_over:
        while game_close:
            win.fill(black)
            message("Game Over! Press Q-Quit or C-Play Again", red, 50, height / 2)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = snake_block, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -snake_block
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, snake_block
        
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        
        x += dx
        y += dy
        win.fill(black)
        pygame.draw.rect(win, green, [food_x, food_y, snake_block, snake_block])
        
        snake.append([x, y])
        if len(snake) > snake_length:
            del snake[0]
        
        for segment in snake[:-1]:
            if segment == [x, y]:
                game_close = True
        
        for segment in snake:
            pygame.draw.rect(win, blue, [segment[0], segment[1], snake_block, snake_block])
        
        pygame.display.update()
        
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1
        
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

game_loop()
