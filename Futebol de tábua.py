import pygame
from pygame.locals import *
from sys import exit
import random
import time

pygame.init()

screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Futebol de tábua!")

back = pygame.Surface((640,480))
background = back.convert()
background.fill((0,153,0))

bar = pygame.Surface((10,50))
bar1 = bar.convert()
bar1.fill((0,0,255))
bar2 = bar.convert()
bar2.fill((255,0,0))

circ_sur = pygame.Surface((15,15))
circ = pygame.draw.circle(circ_sur,(255,255,255),(7,7),7)
circle = circ_sur.convert()
circle.set_colorkey((0,0,0))

bar1_x, bar2_x = 10. , 620.
bar1_y, bar2_y = 215. , 215.

circle_x, circle_y = 307.5, 232.5

bar1_move, bar2_move = 0. , 0.

speed_x, speed_y, speed_circ = 250., 250., 250.

bar1_score, bar2_score = 0,0

clock = pygame.time.Clock()
font = pygame.font.Font("score.ttf", 60)
font1 = pygame.font.Font("game.ttf", 150)
font2 = pygame.font.Font("game.ttf", 90)
font3 = pygame.font.Font("score.ttf", 40)

tela = 0
escolhido = 47

fimDeJogo = ""

while True:
    if(tela == 1): #Tela do jogo
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    bar1_move = -ai_speed
                elif event.key == K_DOWN:
                    bar1_move = ai_speed
            elif event.type == KEYUP:
                if event.key == K_UP:
                    bar1_move = 0.
                elif event.key == K_DOWN:
                    bar1_move = 0.
        
        score1 = font.render(str(bar1_score), True,(255,255,0))
        score2 = font.render(str(bar2_score), True,(255,255,0))
        score3 = font.render("x", True,(255,255,0))
        
        screen.blit(background,(0,0))
        
        frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
        area1 = pygame.draw.rect(screen,(255,255,255),Rect((5,125),(100,225)),2)
        area2 = pygame.draw.rect(screen,(255,255,255),Rect((535,125),(100,225)),2)
        middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
        middle_circle = pygame.draw.circle(screen,(255,255,255), [330, 240],70, 3)
        scoreBoard = pygame.Surface((170,52))
        scoreBoard = scoreBoard.convert()
        scoreBoard.fill((0,0,0))

        screen.blit(scoreBoard, (240., 15.))
        screen.blit(bar1,(bar1_x,bar1_y))
        screen.blit(bar2,(bar2_x,bar2_y))
        screen.blit(circle,(circle_x,circle_y))
        
        screen.blit(score1,(245. ,0.))
        screen.blit(score2,(382.,0.))
        screen.blit(score3,(318.,0.))

        bar1_y += bar1_move
        
        #Velocidade do jogo
        time_passed = clock.tick(30)
        time_sec = time_passed / 1000.0
        circle_x += speed_x * time_sec
        circle_y += speed_y * time_sec
        ai_speed = speed_circ * time_sec

        #IA da inimigo
        if circle_x >= 305.:
            if not bar2_y == circle_y + 7.5:
                if bar2_y < circle_y + 7.5:
                    bar2_y += ai_speed
                if  bar2_y > circle_y - 42.5:
                    bar2_y -= ai_speed
            else:
                bar2_y == circle_y + 7.5

        #Impede de sair da tela
        if bar1_y >= 420.:
            bar1_y = 420.
        elif bar1_y <= 10. :
            bar1_y = 10.
        if bar2_y >= 420.:
            bar2_y = 420.
        elif bar2_y <= 10.:
            bar2_y = 10.

        #Colisão da bola na tábua 1
        if circle_x <= bar1_x + 10.:
            if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
                circle_x = 20.
                speed_x = -speed_x
        #Colisão da bola na tábua 2
        if circle_x >= bar2_x - 15.:
            if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
                circle_x = 605.
                speed_x = -speed_x

        #Colisão na parede
        if circle_y <= 10.:
            speed_y = -speed_y
            circle_y = 10.
        elif circle_y >= 457.5:
            speed_y = -speed_y
            circle_y = 457.5
        
        #Fazer gol
        if circle_x < 5.:
            bar2_score += 1
            circle_x, circle_y = 320., 232.5
            bar1_y,bar_2_y = 215., 215.
        elif circle_x > 620.:
            bar1_score += 1
            circle_x, circle_y = 307.5, 232.5
            bar1_y, bar2_y = 215., 215.

        if(bar2_score == 5):
            tela = 3
            fimDeJogo = "Sinto muito...!"
            pygame.mixer.music.stop()
            pygame.mixer.music.load("intro.ogg")
            pygame.mixer.music.play(0)
        elif(bar1_score == 5):
            tela = 3
            fimDeJogo = "Você ganhou!!!!"
            pygame.mixer.music.load("intro.ogg")
            pygame.mixer.music.play(0)
    elif(tela == 0): #Tela inicial
        if(pygame.mixer.music.get_busy() == False):
            pygame.mixer.music.load("intro.ogg")
            pygame.mixer.music.play(0)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == MOUSEBUTTONUP:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if(x > 270 and x < 400 and y > 275 and y < 320):
                    tela = 2
                if(x > 290 and x < 381 and y > 350 and y < 392):
                    exit()
                
                
        screen.blit(background,(0,0))
        
        frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
        area1 = pygame.draw.rect(screen,(255,255,255),Rect((5,125),(100,225)),2)
        area2 = pygame.draw.rect(screen,(255,255,255),Rect((535,125),(100,225)),2)
        middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
        middle_circle = pygame.draw.circle(screen,(255,255,255), [330, 240],70, 3)
        
        title = font1.render("Futebol de tábua", True,(255,255,0))
        play = font.render("Jogar", True,(255,255,0))
        sair = font.render("Sair", True,(255,255,0))

        screen.blit(title,(100. ,100.))
        screen.blit(play,(270. ,260.))
        screen.blit(sair,(290. ,330.))
    elif(tela == 2): #Tela de edição de personagem
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == MOUSEBUTTONUP:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if(x > 270 and x < 400 and y > 335 and y < 385):
                    tela = 1
                    pygame.mixer.music.stop()
                elif(x > 273 and x < 381 and y > 405 and y < 430):
                    tela = 0
                elif(y > 150 and y < 250):
                    if(x > 47 and x < 147):
                        #azul
                        escolhido = 47
                        bar1.fill((0,0,255))
                    elif(x > 161 and x < 261):
                        #verde
                        escolhido = 161
                        bar1.fill((0,255,0))
                    elif(x > 278 and x < 378):
                        #amarelo
                        escolhido = 278
                        bar1.fill((255,255,0))
                    elif(x > 391 and x < 491):
                        #branco
                        escolhido = 391
                        bar1.fill((255,255,255))
                    elif(x > 508 and x < 608):
                        #preto
                        escolhido = 508
                        bar1.fill((0,0,0))
                
                
        screen.blit(background,(0,0))
        
        frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
        area1 = pygame.draw.rect(screen,(255,255,255),Rect((5,125),(100,225)),2)
        area2 = pygame.draw.rect(screen,(255,255,255),Rect((535,125),(100,225)),2)
        middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
        middle_circle = pygame.draw.circle(screen,(255,255,255), [330, 240],70, 3)

        s = pygame.Surface((100,100))
        
        azul = s.convert()
        azul.fill((0,0,255))
        
        verde = s.convert()
        verde.fill((0,255,0))
        
        amarelo = s.convert()
        amarelo.fill((255,255,0))

        branco = s.convert()
        branco.fill((255,255,255))

        preto = s.convert()
        preto.fill((0,0,0))
        
        title = font2.render("Escolha a cor do seu jogador", True,(255,255,0))
        play = font3.render("Jogar", True,(255,255,0))
        voltar = font3.render("Voltar", True,(255,255,0))

        screen.blit(title,(100. ,0.))
        screen.blit(play,(285. ,320.))
        screen.blit(voltar,(275. ,390.))

        m = 32.5
        screen.blit(azul, (47.5, 150.))
        screen.blit(verde, (162.5, 150.))
        screen.blit(amarelo, (277.5, 150.))
        screen.blit(branco, (392.5, 150.))
        screen.blit(preto, (507.5, 150.))
        
        s2 = pygame.Surface((100,20))
        o = s2.convert()
        o.fill((255,0,0))

        screen.blit(o,(escolhido ,260.))
    elif(tela == 3): #Tela de fim de jogo
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == MOUSEBUTTONUP:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if(x > 120 and x < 555 and y > 400 and y < 435):
                    tela = 0
                    bar1_score, bar2_score = 0,0
                
        screen.blit(background,(0,0))
        
        frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
        area1 = pygame.draw.rect(screen,(255,255,255),Rect((5,125),(100,225)),2)
        area2 = pygame.draw.rect(screen,(255,255,255),Rect((535,125),(100,225)),2)
        middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
        middle_circle = pygame.draw.circle(screen,(255,255,255), [330, 240],70, 3)
        
        
        title = font2.render("Fim de jogo", True,(255,255,0))
        comemoracao = font3.render(fimDeJogo, True,(255,255,0))
        placar = font2.render(str(bar1_score)+" x "+str(bar2_score), True,(255,255,0))
        voltar = font3.render("Voltar para o menu inicial", True,(255,255,0))

        screen.blit(title,(240. ,0.))
        screen.blit(comemoracao,(230. ,170.))
        screen.blit(placar,(290. ,250.))
        screen.blit(voltar,(120. ,390.))

    pygame.display.update()
