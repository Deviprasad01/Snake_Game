#creating window
import pygame
import random
import os

pygame.init()
pygame.mixer.init()


#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,100,0)
blue = (0,0,150)
yellow = (255,255,0)

screen_width = 980
screen_height = 600
gamewindow = pygame.display.set_mode((screen_width,screen_height))
font = pygame.font.SysFont('arial.ttf', 35)


#background image
bgimg = pygame.image.load("welcome.jpg")
bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

bgimg1 = pygame.image.load("play.jpg")
bgimg1 = pygame.transform.scale(bgimg1,(screen_width,screen_height)).convert_alpha()

bgimg2 = pygame.image.load("exit.jpg")
bgimg2 = pygame.transform.scale(bgimg2,(screen_width,screen_height)).convert_alpha()

#game title
pygame.display.set_caption("my first game")
pygame.display.update()
clock=pygame.time.Clock()
font=pygame.font.SysFont('gabriola',60)

def text_screen(text, color, x, y):
    screen_text = font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])   

def plot_snake(gamewindow, color, snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])
        

#welcome screen

def welcome():
    pygame.mixer.music.load('start.mpeg')
    pygame.mixer.music.play()
    exit_game = False
    while not exit_game:
        gamewindow.fill(white)
        gamewindow.blit(bgimg,(0,0))
        text_screen("Welcome To Snakes",black,330,150)
        text_screen("Press SPACE Key",red,330,200)
        text_screen("Let's GOO!!! ",blue,380,250)
        for event in pygame.event.get():
            if event in pygame.event.get():
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mpeg')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(30)

# Game loop
def gameloop():

    #game specific variable
    
    exit_game = False
    game_over = False
    snake_x = 45  #45
    snake_y = 55  #55
    velocity_x=0
    velocity_y=0
    snk_list=[]
    snk_length=1
    with open("hiscore.txt","r")as f:
        hiscore = f.read()

    food_x = random.randint(20,screen_width/2)
    food_y = random.randint(20,screen_height/2)
    snake_size = 20  #10
    init_velocity=5
    score=0
    fps=30

       
    while not exit_game:
        if game_over:
            with open("hiscore.txt","w")as f:
                f.write(str(hiscore))
            gamewindow.fill(white)
            gamewindow.blit(bgimg2,(0,0))
            text_screen("Game over:(((",blue,350,210)
            text_screen("Press ENTER",black,350,290)
            text_screen("Try again!!!",black,380,120)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
                 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0

                    if event.key == pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0

                    if event.key == pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                        
                    if event.key == pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
                
            snake_x=snake_x + velocity_x
            snake_y=snake_y + velocity_y       

            if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
                        score+=10
                        food_x = random.randint(20,screen_width/2)
                        food_y = random.randint(20,screen_height/2)
                        snk_length+=5
                        if score > int(hiscore):
                            hiscore=score

            gamewindow.fill(white)
            gamewindow.blit(bgimg1,(0,0))
            text_screen("score:"+ str(score)+" Hiscore: "+str(hiscore),red,5,5)
            pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load('end.mpeg')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('end.mpeg')
                pygame.mixer.music.play()
            plot_snake(gamewindow, yellow, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()





