#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abiodun Obafemi, Brandon Deliz, Rahul Patel
CPS 3320-01
Project 2

Pygame Library
"""
# Importing pygame library and random module
import pygame as game
from random import randrange

# Defining the screen size, size of the tiles, and the range of the tile size
screenSize = 800
tileSize = 50
rangeOfTiles = (tileSize // 2, screenSize - tileSize // 2, tileSize)

# Generates random position on the window
randomPosition = lambda: [randrange(*rangeOfTiles), randrange(*rangeOfTiles)]

# Creating snake and placing snake in a random position
snake = game.rect.Rect([0, 0, tileSize -2, tileSize - 2])
snake.center = randomPosition()
length = 1
segments = [snake.copy()]
snakeDirection = (0, 0)

# Setting the frame rate
time, time_step = 0, 110

# Creating apple and placing apple in a random position
apple = snake.copy()
apple.center = randomPosition()

# Setting up the screen, clock, and direction keys
screen = game.display.set_mode([screenSize] * 2)
clock = game.time.Clock()
direction = {game.K_w: 1, game.K_s: 1, game.K_a: 1, game.K_d: 1}

# While loop
while True:
    # Checks for events
    for event in game.event.get():
        if event.type == game.QUIT:
            exit()
        if event.type == game.KEYDOWN:
            # Checking if direction key is pressed
            if event.key == game.K_w and direction[game.K_w]:
                snakeDirection = (0, -tileSize)
                direction = {game.K_w: 1, game.K_s: 0, game.K_a: 1, game.K_d: 1}
            if event.key == game.K_s and direction[game.K_s]:
                snakeDirection = (0, tileSize)
                direction = {game.K_w: 0, game.K_s: 1, game.K_a: 1, game.K_d: 1}
            if event.key == game.K_a and direction[game.K_a]:
                snakeDirection = (-tileSize, 0)
                direction = {game.K_w: 1, game.K_s: 1, game.K_a: 1, game.K_d: 0}
            if event.key == game.K_d and direction[game.K_d]:
                snakeDirection = (tileSize, 0)
                direction = {game.K_w: 1, game.K_s: 1, game.K_a: 0, game.K_d: 1}
    
    # Setting background as blue
    screen.fill("dark blue")
    
    # Adding a title of the game
    game.display.set_caption('Snake Game')
    
    # Check out of bounds and if self-eaten
    selfEating = game.Rect.collidelist(snake, segments[:-1]) != -1
    if snake.left < 0 or snake.right > screenSize or snake.top < 0 or snake.bottom > screenSize or selfEating: 
        # if snake goes out of bounds or the snake collides with itself, then game resets
        snake.center, apple.center = randomPosition(), randomPosition() 
        length, snakeDirection = 1, (0,0)
        segments = [snake.copy()]
        
    # Checking for apple
    if snake.center == apple.center:
        # if snake eats the apple, then a new apple appears in a new spot
        apple.center = randomPosition()
        length += 1
        
    # Drawing the apple
    game.draw.rect(screen, 'red', apple)
    
    # Drawing the snake
    [game.draw.rect(screen, 'green', segment) for segment in segments]
    
    # Moving snake
    time_now = game.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snakeDirection)
        segments.append(snake.copy())
        segments = segments[-length:]
        
    # Updates the screen
    game.display.flip()
    
    # Sets the frame rate
    clock.tick(10)