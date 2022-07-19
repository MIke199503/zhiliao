import pygame,sys,os,random
pygame.init()

bakscreen=pygame.display.set_mode([800,600])
bakscreen.fill([0,160,233])
pygame.display.set_caption('接粽子')
infoObject = pygame.display.Info()

class rect():
    def __init__(self,filename,initial_position):
        self.image=pygame.image.load(filename)
        self.rect=self.image.get_rect()
        self.rect.topleft=initial_position
        
class goldrect(pygame.sprite.Sprite):
    def __init__(self,gold_position,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('image/粽子.png')
        self.image =  pygame.transform.scale(self.image, (40, 40))
        self.image = pygame.transform.rotate(self.image, random.randint(0,360))
        self.rect=self.image.get_rect()
        self.rect.topleft=gold_position
        self.speed=speed
    def move(self):
        self.rect=self.rect.move(self.speed)

def drawback(): 
    my_back=pygame.image.load('image/qi3.jpg') 
    bakscreen.blit(my_back,[0,0])

        
def loadtext(levelnum,score,highscore):
    my_font = pygame.font.Font('欢字卡通手书.ttf', 24)
    levelstr='等级:'+str(levelnum)
    text_screen=my_font.render(levelstr, True, (255, 0, 0))
    bakscreen.blit(text_screen, (650,50))
    highscorestr='最高分:'+str(highscore)
    text_screen=my_font.render(highscorestr, True, (255, 0, 0))
    bakscreen.blit(text_screen, (650,80))
    scorestr='分数:'+str(score)
    text_screen=my_font.render(scorestr, True, (255, 0, 0))
    bakscreen.blit(text_screen, (650,110))    

def loadgameover(scorenum,highscore):
    my_font = pygame.font.Font('欢字卡通手书.ttf', 50)
    levelstr='游戏结束'
    over_screen=my_font.render(levelstr, True, (255, 0, 0))
    bakscreen.blit(over_screen, (infoObject.current_w / 4 , infoObject.current_h / 4 ))
    highscorestr='你的成绩为： '+str(scorenum)
    over_screen=my_font.render(highscorestr, True, (255, 0, 0))
    bakscreen.blit(over_screen, (infoObject.current_w / 4, infoObject.current_h / 4 * 2))
    if scorenum>int(highscore):
        highscorestr='你获得了最高分哟～'
        text_screen=my_font.render(highscorestr, True, (255, 0, 0))
        bakscreen.blit(text_screen, (infoObject.current_w / 4 , infoObject.current_h / 4 * 3))
        highfile=open('highscore','w')
        highfile.writelines(str(scorenum))  
        highfile.close()  
    
def gethighscore():
    if os.path.isfile('highscore'):
        highfile=open('highscore','r')
        highscore=highfile.readline() 
        highfile.close() 
    else:
        highscore=0
    return highscore
                  

drawback()



levelnum=1 
scorenum=0 
highscore=gethighscore()
ileft=1  
iright=10 
x=100
y=450
filename='image/1.png'
backimg_ren=rect(filename,[x,y])
bakscreen.blit(backimg_ren.image,backimg_ren.rect)
loadtext(levelnum,scorenum,highscore)
goldx=random.randint(50,580)
speed=[0,levelnum*2.2]
mygold=goldrect([goldx,100],speed) 
pygame.display.update()

while True:
    if scorenum>0 and scorenum/50.0==int(scorenum/50.0):
        levelnum=scorenum/50+1
        speed=[0,levelnum*2.2]
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    #make gold    

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT]:

        drawback()  
        loadtext(levelnum,scorenum,highscore)

        if iright > 14 :iright=10
        iright=iright+1
        filename='image/'+str(iright)+'.png'
        if x<50 :
            x=50
        else:
            x=x-10

        backimg_surface=rect(filename,[x,y])
        bakscreen.blit(backimg_surface.image,backimg_surface.rect)

        
    if pressed_keys[pygame.K_RIGHT]:

        drawback()
        loadtext(levelnum,scorenum,highscore)

        if ileft > 4 :ileft=0
        ileft=ileft+1
        filename='image/'+str(ileft)+'.png'
        if x>560:
            x=560
        else:
            x=x+10

        backimg_surface=rect(filename,[x,y])
        bakscreen.blit(backimg_surface.image,backimg_surface.rect)

    drawback()
    loadtext(levelnum,scorenum,highscore)
    mygold.move()
    bakscreen.blit(mygold.image,mygold.rect) 
    
    backimg_surface=rect(filename,[x,y])
    bakscreen.blit(backimg_surface.image,backimg_surface.rect)

    if mygold.rect.top > 600:
        
        loadgameover(scorenum,highscore)
        print(mygold.rect.top)
    if mygold.rect.colliderect(backimg_surface.rect):
        scorenum+=5
        loadtext(levelnum,scorenum,highscore)
        goldx=random.randint(50,580)
        mygold=goldrect([goldx,100],speed) 
    pygame.display.update()
