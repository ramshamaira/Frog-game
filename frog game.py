from pygame import *


init()


width, height = 600, 400
screen = display.set_mode((width, height))
display.set_caption('Frogger')

# Colors
BLACK = (0, 0, 0)      
GREY = (128, 128, 128) 
WHITE = (255, 255, 255)
road_width = 300
kerb_width = (width - road_width) // 2

Frogpic = image.load("frog.jpg")  
Frogpic = transform.scale(Frogpic, (50, 50))
frogRect = Rect((width - 100) // 2, height - 50, 50, 50)
frog_speed = 10  

Carpic = image.load("car.jpg")  
Carpic = transform.scale(Carpic, (80, 40))  

Carpic2 = image.load("car2.jpg")  
Carpic2 = transform.scale(Carpic2, (80, 40))  


#  car positions
cars = [
    {"rect": Rect(200, 0, 80, 40), "speed": 5,"image": Carpic},
    {"rect": Rect(350, -100, 80, 40), "speed": 3,"image": Carpic2}
]

mixer.music.load("frog.mp3")
mixer.music.play()


endGame = False
while not endGame:
    for e in event.get():
        if e.type == QUIT:
            endGame = True
     
    for car in cars:
        car["rect"].y += car["speed"]

     
        if car["rect"].y > height:
            car["rect"].y = -40  

    for c in cars:
         if car["rect"].colliderect(frogRect):  
            endGame = True

    # Movement handling
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
    draw.rect(screen, GREY, (0, 0, kerb_width, height))  
    draw.rect(screen, GREY, (kerb_width + road_width, 0, kerb_width, height)) 
    draw.rect(screen, BLACK, (kerb_width, 0, road_width, height))

   
    for c in cars:
        
         screen.blit(car["image"], car["rect"].topleft)

   
    screen.blit(Frogpic, frogRect)

    display.update()
    time.delay(30)
