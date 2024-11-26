from pygame.locals import *
import pygame
import random
import math
from scalling import scale_image


pygame.init()
#set up screen
disp=pygame.display.set_mode((1024,1381))
pygame.display.set_caption('Pranto car game')

logo=pygame.image.load('l1.jpg')
pygame.display.set_icon(logo)

pygame.mixer.music.load('bgm1.wav')
pygame.mixer.music.play()


#variable
game_exit=False
bg=pygame.image.load('race_track.jpg')
score=0
font=pygame.font.Font("freesansbold.ttf",50)
score_x=750
score_y=300
gameover_x=350
gameover_y=500


# car
car=scale_image(pygame.image.load('car.png'),0.07)
car_x=470
car_y=1050
def pic(x,y):
   disp.blit(car,(x,y))
car_xmove=0
car_ymove=0


#enemy car
e_car1=scale_image(pygame.image.load('ecar2.png'),0.09)
e_car1_x=370
e_car1_y=150
e_car1_xmove=0
e_car1_ymove=10
def pic1(x,y):
   disp.blit(e_car1,(x,y))

e_car2=scale_image(pygame.image.load('car3.png'),0.05)
e_car2_x=570
e_car2_y=150
e_car2_xmove=0
e_car2_ymove=6
def pic2(x,y):
   disp.blit(e_car2,(x,y))   

e_car3=scale_image(pygame.image.load('car4.png'),0.15)
e_car3_x=570
e_car3_y=550
e_car3_xmove=0
e_car3_ymove=8
def pic3(x,y):
   disp.blit(e_car3,(x,y))  

e_car4=scale_image(pygame.image.load('car5.png'),0.20)
e_car4_x=370
e_car4_y=550
e_car4_xmove=0
e_car4_ymove=5
def pic4(x,y):
   disp.blit(e_car4,(x,y))   


def iscrashed1(car_x,car_y,e_car1_x,e_car1_y):
   distance1=math.sqrt((math.pow(car_x-e_car1_x,2)+math.pow(car_y-e_car1_y,2)))
   if distance1<40:
      return True
   else:
      return False

def iscrashed2(car_x,car_y,e_car2_x,e_car2_y):
   distance2=math.sqrt((math.pow(car_x-e_car2_x,2)+math.pow(car_y-e_car2_y,2)))
   if distance2<50:
      return True
   else:
      return False      

def iscrashed3(car_x,car_y,e_car3_x,e_car3_y):
   distance3=math.sqrt((math.pow(car_x-e_car3_x,2)+math.pow(car_y-e_car3_y,2)))
   if distance3<40:
      return True
   else:
      return False

def iscrashed4(car_x,car_y,e_car4_x,e_car4_y):
   distance4=math.sqrt((math.pow(car_x-e_car4_x,2)+math.pow(car_y-e_car4_y,2)))
   if distance4<70:
      return True
   else:
      return False

def show_score(x,y):
   result=font.render("Score: "+str(score),True,(0,240,0))
   disp.blit(result,(x,y))

def game_over(x,y):
   final_score=font.render("Car Crashed",True,(255,0,0))
   disp.blit(final_score,(x,y))


FPS=60
clock=pygame.time.Clock()

while not game_exit:
    clock.tick(FPS)

    disp.blit(bg,(0,0)) # type: ignore
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
          game_exit=True
        if event.type==pygame.KEYDOWN:
           if event.key==pygame.K_RIGHT: 
              car_xmove=+4
           if event.key==pygame.K_LEFT: 
              car_xmove=-4 

    car_x+=car_xmove
    e_car1_y+=e_car1_ymove
    e_car2_y+=e_car2_ymove
    e_car3_y+=e_car3_ymove
    e_car4_y+=e_car4_ymove
    if car_x<=370:
       car_x=370
    elif car_x>=585:
       car_x=585   

    if e_car1_y>1381:
          e_car1_y=-100
          e_car1_x=random.randint(370,585)
          score+=1
          print(score)
   #  crash1=iscrashed1(car_x,car_y,e_car1_x,e_car1_y)
    

    if e_car2_y>1381:
          e_car2_y=-100  
          e_car2_x=random.randint(370,585)
          score+=1
          print(score)
   #  crash2=iscrashed2(car_x,car_y,e_car2_x,e_car2_y)
    

    if e_car3_y>1381:
          e_car3_y=-100 
          e_car3_x=random.randint(370,585)
          score+=1
          print(score)
   #  crash3=iscrashed3(car_x,car_y,e_car3_x,e_car3_y)
    

    if e_car4_y>1381:
          e_car4_y=-100 
          e_car4_x=random.randint(370,585)
          score+=1
          print(score)
    
                      
    crash1=iscrashed1(car_x,car_y,e_car1_x,e_car1_y)
    crash2=iscrashed2(car_x,car_y,e_car2_x,e_car2_y)
    crash3=iscrashed3(car_x,car_y,e_car3_x,e_car3_y)
    crash4=iscrashed4(car_x,car_y,e_car4_x,e_car4_y)

    pic(car_x,car_y) 
    show_score(score_x,score_y)
    pic1(e_car1_x,e_car1_y)
    pic2(e_car2_x,e_car2_y)
    pic3(e_car3_x,e_car3_y)
    pic4(e_car4_x,e_car4_y)
     

    if crash1:
       pygame.mixer.music.stop()
       crash_sound=pygame.mixer.Sound('crash.wav')
       crash_sound.play()
       disp.fill((255,255,0))
       e_car1_ymove=0
       e_car2_ymove=0
       e_car3_ymove=0
       e_car4_ymove=0
       car_xmove=0
       game_over(gameover_x,gameover_y)
       show_score(score_x,score_y)
       


    elif crash2:
       pygame.mixer.music.stop()
       crash_sound=pygame.mixer.Sound('crash.wav')
       crash_sound.play()
       disp.fill((255,255,0))  
       e_car1_ymove=0
       e_car2_ymove=0
       e_car3_ymove=0
       e_car4_ymove=0
       car_xmove=0
       game_over(gameover_x,gameover_y)
       show_score(score_x,score_y)

    elif crash3:
       pygame.mixer.music.stop()
       crash_sound=pygame.mixer.Sound('crash.wav')
       crash_sound.play()
       disp.fill((255,255,0))
       e_car1_ymove=0
       e_car2_ymove=0
       e_car3_ymove=0
       e_car4_ymove=0
       car_xmove=0
       game_over(gameover_x,gameover_y)
       show_score(score_x,score_y)



    elif crash4:
       pygame.mixer.music.stop()
       crash_sound=pygame.mixer.Sound('crash.wav')
       crash_sound.play()
       disp.fill((255,255,0)) 
       e_car1_ymove=0
       e_car2_ymove=0
       e_car3_ymove=0
       e_car4_ymove=0
       car_xmove=0
       game_over(gameover_x,gameover_y)
       show_score(score_x,score_y)



    pygame.display.update()

pygame.quit()
quit()

        
