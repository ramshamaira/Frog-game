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

# Load images
Frogpic = image.load("frog.jpg")  
Frogpic = transform.scale(Frogpic, (50, 50))
frogRect = Rect((width - 100) // 2, height - 50, 50, 50)
frog_speed = 10  

Carpic1 = image.load("car.jpg")  
Carpic1 = transform.scale(Carpic1, (80, 40))  

Carpic2 = image.load("car2.jpg")  
Carpic2 = transform.scale(Carpic2, (80, 40))  

# Cars (rectangles & speeds)
cars = [
    {"rect": Rect(width, 100, 80, 40), "speed": -5, "image": Carpic1},  # Moves left
    {"rect": Rect(-80, 200, 80, 40), "speed": 5, "image": Carpic2}      # Moves right
]

mixer.music.load("frog.mp3")
mixer.music.play()

endGame = False
while not endGame:
    for e in event.get():
        if e.type == QUIT:
            endGame = True

    # Move cars left and right
    for car in cars:
        car["rect"].move_ip(car["speed"], 0)

        # Reset car position when off screen
        if car["rect"].x < -80:  # If car moves off left side
            car["rect"].x = width
        if car["rect"].x > width:  # If car moves off right side
            car["rect"].x = -80

    # **Collision detection (FIXED)**
    for c in cars:
        if c["rect"].colliderect(frogRect):  
            print("Game Over!")  # Debug message
            endGame = True

    # Frog movement
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
    screen.fill(WHITE)

    # Horizontal kerbs
    draw.rect(screen, GREY, (0, 0, width, 40))  
    draw.rect(screen, GREY, (0, height - 40, width, 40)) 

    # Road in the center
    draw.rect(screen, BLACK, (0, 40, width, height - 80))

    # Draw cars
    for car in cars:
        screen.blit(car["image"], car["rect"].topleft)

    # Draw frog
    screen.blit(Frogpic, frogRect)

    display.update()
    time.delay(30)



   
  
