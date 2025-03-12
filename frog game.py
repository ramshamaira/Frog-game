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

log= image.load("logs.jpg")
log= transform.scale(log,(60,30))
log_width, log_height = 80, 40
log_x = width 
log_y = 20  
log_speed = -3 
logRect = Rect(log_x, log_y, log_width, log_height)


# Cars (rectangles & speeds)
cars = [
    {"rect": Rect(width, 150, 60, 30), "speed": -5, "image": Carpic1},  # Moves left
    {"rect": Rect(-80, 200, 80, 40), "speed": 5, "image": Carpic2}      # Moves right
]

#music
mixer.music.load("frog.mp3")
mixer.music.play()

#loop
endGame = False
while not endGame:
    for e in event.get():
        if e.type == QUIT:
            endGame = True

    # Move cars left and right
    for car in cars:
        car["rect"].move_ip(car["speed"], 0)

        # Reset car position when off screen
        if car["rect"].x < -80:  
            car["rect"].x = width
        if car["rect"].x > width:  
            car["rect"].x = -80
            
    logRect.move_ip(log_speed, 0)
    if logRect.x < -log_width:
	     logRect.x = width 

    #ollision detection 
    for c in cars:
        if c["rect"].colliderect(frogRect):  
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

   
    screen.fill(BLACK)
     #river
    river_height = 100
    draw.rect(screen, BLUE, (0, 0, width, river_height))  

    #kerb
    kerb_height = 40
    draw.rect(screen, GREY, (0, river_height, width, kerb_height))  

    #road
    
    road_height =100
    draw.rect(screen, BLACK, (0, river_height + kerb_height, width, road_height))  

    #Kerb
    kerb_height=40
    draw.rect(screen, GREY, (0, river_height + kerb_height + road_height, width, kerb_height))  
 
     #draw log
    screen.blit(log, logRect)

  
    # Draw cars
    for car in cars:
        screen.blit(car["image"], car["rect"].topleft)

    # Draw
    screen.blit(Frogpic, frogRect)
   
    display.update()
    time.delay(30)



   
  
