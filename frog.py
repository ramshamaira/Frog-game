import pygame
from pygame import *
import time
pygame.init()

# Window setup
width, height = 600, 400
screen = display.set_mode((width, height))
display.set_caption('Frogger')

# Colors
BLACK = (0, 0, 0)      
GREY = (128, 128, 128) 
BROWN = (139, 69, 19)  
BLUE = (0, 0, 255)     
WHITE = (255, 255, 255) 
RED = (255, 0, 0)      
PINK = (255, 6, 100)   

# Load images
Frogpic = image.load("frog.jpg")  
Frogpic = transform.scale(Frogpic, (40, 40))
frogRect = Rect((width - 100) // 2, height - 50, 50, 50)
frog_speed = 5  

Carpic1 = image.load("car.jpg")  
Carpic1 = transform.scale(Carpic1, (60, 30))  

Carpic2 = image.load("car2.jpg")  
Carpic2 = transform.scale(Carpic2, (60, 30)) 

log_img = image.load("logs.jpg")
log_img = transform.scale(log_img, (80, 40))

# Logs 
logs = [
    {"rect": Rect(width, 120, 120, 40), "speed": -2, "image": log_img},
    {"rect": Rect(width-160, 140, 120, 40), "speed": 2, "image": log_img} ,
    {"rect": Rect(width-320,160, 120, 40), "speed": -2, "image": log_img}  # Middle log positioned in river area
]


# Cars
cars = [
    {"rect": Rect(width, 200, 60, 30), "speed": -3, "image": Carpic1},  
    {"rect": Rect(-80, 250, 80, 40), "speed": 3, "image": Carpic2}     
]

# Music
mixer.music.load("frog.mp3")
mixer.music.play(-1) 

# Timer
max_time = 1000  
current_time = max_time  
timer_bar_width = 200  
timer_x = 10  

# Game loop
endGame = False
on_log = False  
game_over = False  
win_game= False

while not endGame:
    for e in event.get():
        if e.type == QUIT:
            endGame = True

    if not game_over and not win_game: 

        # cars
        for car in cars:
            car["rect"].move_ip(car["speed"], 0)
            if car["rect"].x < -80:  
                car["rect"].x = width
            if car["rect"].x > width:  
                car["rect"].x = -80

        # Move logs
        on_log = False 
        for log_obj in logs:
            log_obj["rect"].move_ip(log_obj["speed"], 0)
            if log_obj["speed"] < 0 and log_obj["rect"].x < -80:
                log_obj["rect"].x = width
            if log_obj["speed"] > 0 and log_obj["rect"].x > width:
                log_obj["rect"].x = -80

            if frogRect.colliderect(log_obj["rect"]):
                frogRect.move_ip(log_obj["speed"], 0)  
                on_log = True  

        # Check if frog is in the river
        if 100 < frogRect.top < 200 and not on_log:
            print("GAME OVER! The frog fell into the river.")
            game_over = True  

        # Collision cars
        for c in cars:
            if c["rect"].colliderect(frogRect):  
                print("GAME OVER! The frog got hit by a car.")
                game_over = True
                break

        # Frog movement
        keys = key.get_pressed()
        if keys[K_w] or keys[K_UP]: 
            if frogRect.top > 0:
                frogRect.move_ip(0, -frog_speed)
        if keys[K_s] or keys[K_DOWN]:  
            if frogRect.bottom < height:
                frogRect.move_ip(0, frog_speed)
        if keys[K_a] or keys[K_LEFT]:
            if frogRect.left > 0:
                frogRect.move_ip(-frog_speed, 0)
        if keys[K_d] or keys[K_RIGHT]:  
            if frogRect.right < width:
                frogRect.move_ip(frog_speed, 0)

        # Timer
        current_time -= 2 
        if current_time <= 0:
            print("GAME OVER! Time ran out.")
            game_over = True  

        # If frog reaches top pink pavement, stop the game
        if frogRect.top <= 40:
            print("YOU WIN! Frog reached safety.")
            win_game = True  

    # Draw background
    screen.fill(BLACK)
    draw.rect(screen, BROWN, (0, 300, width, 40))  
    draw.rect(screen, GREY, (0, 200, width, 100))  
    draw.rect(screen, BLUE, (0, 100, width, 100))  
    draw.rect(screen, PINK, (0, 40, width, 60))
    draw.rect(screen, BROWN, (0, 0, width, 40))    

    # Draw logs
    for log_obj in logs:
        screen.blit(log_obj["image"], log_obj["rect"].topleft)

    # Draw cars
    for car in cars:
        screen.blit(car["image"], car["rect"].topleft)

    # Draw frog
    screen.blit(Frogpic, frogRect)

    # Draw Timer Bar
    timer_ratio = current_time / max_time  
    timer_width = int(timer_ratio * timer_bar_width)  
    draw.rect(screen, WHITE, (timer_x, 10, timer_bar_width, 20))  
    draw.rect(screen, RED, (timer_x, 10, timer_width, 20))  

    # Display
    if game_over:
        font = pygame.font.SysFont("Arial", 50)
        text = font.render("GAME OVER!", True, WHITE)  
        screen.blit(text, (width // 2 - 100, height // 2))  
    if win_game:
        font = pygame.font.SysFont("Arial", 50)
        text = font.render("YOU WIN!", True, WHITE)  
        screen.blit(text, (width // 2 - 100, height // 2))  


    display.update()
    pygame.time.delay(30)

mixer.music.stop()
