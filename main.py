import pygame
import numpy as np
import random
import time

class pawn:

    def __init__(self,ndx,ndy,a=True):
        self.isplayer=a
        self.nodex=ndx
        self.nodey = ndy

        if a==True:
            self.color= (0,random.randrange(125)+125,random.randrange(125)+125)
            self.tix = 20
        else:
           self.color=(255,0,0)
           self.tix = 21
        self.prl = np.full((200, 100, 3), self.color)
        self.pl = np.full((4, 11, 3), self.color)
        self.pl1 = np.full((4, 11, 3), (30,30,30))
        self.sr = pygame.surfarray.make_surface(self.prl)
        self.sr2 = pygame.surfarray.make_surface(self.pl)
        self.sr3 = pygame.surfarray.make_surface(self.pl1)
    def turn(self,num):
        if self.tix>0:
            if (num==3 or num==10 or num==16) and self.isplayer==False :
                screen.blit(self.sr2, (28+self.nodex*67, 17+self.nodey*67))

            self.text = font.render("taxi: "+str(self.tix)+"   ", True, (255,255, 0), (150, 150, 150))
            screen.blit(self.text,(810,110))
            screen.blit(self.sr, (800, 0))
            self.text2 = font.render(str(self.nodex * 12 + self.nodey), True, (0, 0, 0), self.color)
            screen.blit(self.text2, (810, 20))
            pygame.display.flip()
            flag=True
            ng=con(nodesconn,self.nodex,self.nodey)
            screen.blit(surf4, (800, 200))
            for i in range(len(ng)):

                self.plate = np.full((80, 50, 3), (255,255,i+1))
                self.sr1 = pygame.surfarray.make_surface(self.plate)
                self.text1 = font.render(str(ng[i][0]*12+ng[i][1]), True, (0, 0, 0), (255, 255, 0))
                screen.blit(self.sr1,(820,200+i*100))
                screen.blit(self.text1, (830, 220+i*100))
                pygame.display.flip()
            while flag:
                for event in pygame.event.get():
                    if pygame.mouse.get_pressed()[0]==True:
                        if screen.get_at(pygame.mouse.get_pos())[2]>0 and screen.get_at(pygame.mouse.get_pos())[2]<10:
                            screen.blit(self.sr3, (28 + self.nodex * 67, 17 + self.nodey * 67))
                            pygame.display.flip()
                            self.tix=self.tix-1
                            self.temp=ng[screen.get_at(pygame.mouse.get_pos())[2]-1]
                            self.nodex = self.temp[0]

                            self.nodey = self.temp[1]
                            if self.isplayer == True:
                                screen.blit(self.sr2, (28 + self.nodex * 67, 17 + self.nodey * 67))

                            flag=False
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
        else:
            screen.blit(self.sr2, (28 + self.nodex * 67, 17 + self.nodey * 67))

def con(nc,x,y):
    ls=[]
    for i in range(144):
        if nc[x*12+y][i]==1:
            ls.append([i//12,i%12])

    return ls

def dispmap(nodes):
    nodepos = np.ones((12, 12,2))
    node = np.full((11, 11, 3), (200, 200, 0))
    surf = pygame.surfarray.make_surface(node)
    for i in range(len(nodes)):
        for j in range(len(nodes[1])):
            text=font.render(str(i*len(nodes)+j), True, (0, 0, 00), (200, 200, 0))
            screen.blit(surf, (28+i*67, 28+j*67))
            screen.blit(text, (28+i*67, 28+j*67))
            nodepos[i][j][0]=33+i*67
            nodepos[i][j][1] =33+j*67

    return nodepos

def gencon(nc,nodes):
    for i in range(len(nodes)):
        for j in range(len(nodes[1])):
            nebhr=[]
            for a in range(3):
                for b in range(3):
                    if (i-1+a>-1 and i-1+a<12 and j-1+b>-1 and j-1+b<12)  :
                        if not(i-1+a==i and j-1+b==j):
                            nebhr.append( [i-1+a,j-1+b])

            nebhr=random.sample(nebhr,2)
            for c in range(len(nebhr)):
                nc[(nebhr[c][0]) * 12 + nebhr[c][1]][i*12+j] = 1

                nc[i*12+j][(nebhr[c][0])*12+nebhr[c][1]]=1
    for i in range(len(nodes)):
        nc[i][i]=0

    return nc


def dispcon(nc,nodepos,gamearea):
    for i in range(len(nc)):
        for j in range(len(nc[1]-i)):
            if nc[i][j]==1:
                t1 = i // 12
                t2 = i % 12
                t3 = j // 12
                t4 = j % 12

                pygame.draw.line(gamearea, (200,200,0),nodepos[t1][t2],nodepos[t3][t4],3)


    return None


nodes=np.ones((12,12))
nodesconn=np.zeros((144,144),int)
pygame.init()
screen = pygame.display.set_mode((1000,800))
font = pygame.font.Font('freesansbold.ttf', 12)
Running=True


nodepos=dispmap(nodes)
gamearea=np.full((800,800,3),30)
nodesconn=gencon(nodesconn,nodes)

gamearea=np.full((800,800,3),30)
infarea1=np.full((200,100,3),200)
infarea2=np.full((200,100,3),150)
infarea3=np.full((200,600,3),100)
surf1 = pygame.surfarray.make_surface(gamearea)
surf2 = pygame.surfarray.make_surface(infarea1)
surf3 = pygame.surfarray.make_surface(infarea2)
surf4 = pygame.surfarray.make_surface(infarea3)
dispcon(nodesconn,nodepos,surf1)
screen.blit(surf1, (0, 0))
screen.blit(surf2, (800, 0))
screen.blit(surf3, (800, 100))
screen.blit(surf4, (800, 200))
dispmap(nodes)

ls=[[0,0],[11,11],[0,11],[11,0],[5,5],[3,7],[9,2],[8,4]]
ls=random.sample(ls,3)
pol1=pawn(ls[0][0],ls[0][1])
pol2=pawn(ls[1][0],ls[1][1])
uc=pawn(ls[2][0],ls[2][1],a=False)
num=0
while Running:

    uc.turn(num)
    if (uc.nodex==pol1.nodex and uc.nodey==pol1.nodey) or (uc.nodex==pol2.nodex and uc.nodey==pol2.nodey):
        font = pygame.font.Font('freesansbold.ttf', 40)
        end = font.render("YOU DIED", True, (255,255, 255), (0, 0, 0))
        screen.blit(end, (300, 500))
    time.sleep(0.1)
    pol1.turn(num)
    time.sleep(0.1)
    pol2.turn(num)
    time.sleep(0.1)
    if (uc.nodex==pol1.nodex and uc.nodey==pol1.nodey) or (uc.nodex==pol2.nodex and uc.nodey==pol2.nodey):
        font = pygame.font.Font('freesansbold.ttf', 40)
        end = font.render("YOU DIED", True, (255,255, 255), (0, 0, 0))
        screen.blit(end, (300, 500))
        pygame.display.flip()
        time.sleep(10)

    if num>18:

        font = pygame.font.Font('freesansbold.ttf', 40)
        end = font.render("YOU ESCAPED", True, (255,255, 255), (0, 0, 0))
        screen.blit(end, (300, 500))
        pygame.display.flip()
        time.sleep(10)

    num=num+1
    flag=True
    while flag:
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0] == True:


                    flag = False





