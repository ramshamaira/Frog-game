from pygame import *

init()

# Window setup
width, height = 600, 400
screen = display.set_mode((width, height))
display.set_caption('Frogger')

# Colors
BLACK = (0, 0, 0)      
GREY = (128, 128, 128) 
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Load images
Frogpic = image.load("frog.jpg")  
Frogpic = transform.scale(Frogpic, (50, 50))
frogRect = Rect((width - 100) // 2, height - 50, 50, 50)
frog_speed = 10  

Carpic1 = image.load("car.jpg")  
Carpic1 = transform.scale(Carpic1, (50, 30))  

Carpic2 = image.load("car2.jpg")  
Carpic2 = transform.scale(Carpic2, (60, 30)) 

# Load logs
log_img = image.load("logs.jpg")
log_img = transform.scale(log_img, (60, 30))

# Logs 
logs = [
    {"rect": Rect(width, 20, 80, 40), "speed": -3, "image": log_img},  # Moves left
    {"rect": Rect(-80, 60, 80, 40), "speed": 3, "image": log_img}  # Moves right
]

# Cars (
cars = [
    {"rect": Rect(width, 150, 60, 30), "speed": -5, "image": Carpic1},  # Moves left
    {"rect": Rect(-80, 200, 80, 40), "speed": 5, "image": Carpic2}      # Moves right
]

# Music
mixer.music.load("frog.mp3")
mixer.music.play()

# Game loop
endGame = False
on_log = False  # To check if frog is standing on a log

while not endGame:
    for e in event.get():
        if e.type == QUIT:
            endGame = True

    # Move cars 
    for car in cars:
        car["rect"].move_ip(car["speed"], 0)

        # Reset car position
        if car["rect"].x < -80:  
            car["rect"].x = width
        if car["rect"].x > width:  
            car["rect"].x = -80

    # Move logs 
    on_log = False  # Reset flag
    for log_obj in logs:
        log_obj["rect"].move_ip(log_obj["speed"], 0)

        # Reset first log when off-screen (moving left)
        if log_obj["speed"] < 0 and log_obj["rect"].x < -80:
            log_obj["rect"].x = width

        # Reset second log when off-screen (moving right)
        if log_obj["speed"] > 0 and log_obj["rect"].x > width:
            log_obj["rect"].x = -80

        # Check if frog is standing on a log
        if frogRect.colliderect(log_obj["rect"]):
            frogRect.move_ip(log_obj["speed"], 0)  # Move frog with log
            on_log = True  # Frog is safe on a log

    # **Game ends only if the frog is in the river but NOT on a log**
    if frogRect.top < 100 and not on_log:
        print("GAME OVER! The frog fell into the river.")
        break  # End the game

    # Collision detection with cars
    for c in cars:
        if c["rect"].colliderect(frogRect):  
            print("GAME OVER! The frog got hit by a car.")
            break  # End the game

    # Frog movement (player controls)
    keys = key.get_pressed()
    if keys[K_w] or keys[K_UP]: 
        frogRect.move_ip(0, -frog_speed)
    if keys[K_s] or keys[K_DOWN]:  
        frogRect.move_ip(0, frog_speed)
    if keys[K_a] or keys[K_LEFT]:
        frogRect.move_ip(-frog_speed, 0)
    if keys[K_d] or keys[K_RIGHT]:  
        frogRect.move_ip(frog_speed, 0)

    # Draw background
    screen.fill(BLACK)

    # River
    river_height = 100
    draw.rect(screen, BLUE, (0, 0, width, river_height))  

    # Kerb
    kerb_height = 40
    draw.rect(screen, GREY, (0, river_height, width, kerb_height))  

    # Road
    road_height = 100
    draw.rect(screen, BLACK, (0, river_height + kerb_height, width, road_height))  

    # Kerb
    draw.rect(screen, GREY, (0, river_height + kerb_height + road_height, width, kerb_height))  
 
    # Draw logs
    for log_obj in logs:
        screen.blit(log_obj["image"], log_obj["rect"].topleft)

    # Draw cars
    for car in cars:
        screen.blit(car["image"], car["rect"].topleft)

    # Draw frog
    screen.blit(Frogpic, frogRect)

    display.update()
    time.delay(30)
