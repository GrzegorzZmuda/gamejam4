import pygame
import numpy as np
import random
import time

class pawn:

    def __init__(self,ndx,ndy,a=True):
        self.isplayer=a
        self.nodex=ndx
        self.nodey = ndy
        self.tix=20
        if a==True:
            self.color= (0,random.randrange(255),random.randrange(255))
        else:
           self.color=(255,0,0)
        self.prl = np.full((200, 100, 3), self.color)
        self.sr = pygame.surfarray.make_surface(self.prl)
    def turn(self):

        screen.blit(self.sr, (800, 0))
        pygame.display.flip()
        flag=True
        while flag:
            for event in pygame.event.get():
                if pygame.mouse.get_pressed()[0]==True:
                    flag=False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
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
                        nebhr.append( [i-1+a,j-1+b])

            nebhr=random.sample(nebhr,random.randrange(2,min(len(nebhr),5)))
            for c in range(len(nebhr)):
                nc[(nebhr[c][0]) * 12 + nebhr[c][1]][i*12+j] = 1

                nc[i*12+j][(nebhr[c][0])*12+nebhr[c][1]]=1


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
while Running:

    uc.turn()


    pol1.turn()

    pol2.turn()






