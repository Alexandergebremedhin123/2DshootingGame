import pygame
import random 
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
pygame.init()
score_value=0
width=500
height=600
size=(width,height)
screen=pygame.display.set_mode(size)

pygame.display.set_caption("ShooterGame")
clock=pygame.time.Clock()
font=pygame.font.Font(None,32)
textX=10
textY=550

def show_score(x,y):
     score=font.render("Score: "+str(score_value),True,blue)
     screen.blit(score,(x,y))
def play_again():
    text = font.render('Play again?', 13, (0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), ((textX - 5, textY - 5),
                                               (width + 10, height +
                                                10)))

    screen.blit(text, (width/ 2 - text.get_width() / 2,
                       height/ 2 - text.get_height() / 2))
def again():
    losetext=font.render("you lost",False,blue)
    screen.blit(losetext,((width/2),(height/2)))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((30,20))
        self.image.fill(green)
        self.rect=self.image.get_rect()
        self.rect.bottom=height-10
        self.rect.left=width/2
        self.speedx=0
        self.speedy=0
 
    def update(self):
        self.speedx=0
        self.speedy=0
        keyboard=pygame.key.get_pressed()
        if keyboard[pygame.K_LEFT]:
            self.speedx=-5
        if keyboard[pygame.K_RIGHT]:
            self.speedx=5
        if keyboard[pygame.K_UP]:
            self.speedy=-5
        if keyboard[pygame.K_DOWN]:
            self.speedy=5
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.right>width:
            self.rect.right=width
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.bottom>height-10:
            self.rect.bottom=height-10
        if self.rect.top<0:
            self.rect.top=0
   

    def shoot(self):
        bullet=Bullet(self.rect.centerx,self.rect.top)
        all_sprites.add(bullet)
        bullets_sprites.add(bullet)

class Enemy(pygame.sprite.Sprite):
     def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((40,30))
        self.image.fill(red)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(0,width-self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speedy=random.randrange(1,8)
     def update(self):
         self.rect.y+=self.speedy
         if self.rect.top>height+10:
            self.rect.x=random.randrange(0,width-self.rect.x)
            self.rect.y=random.randrange(-100,-40)
            self.speedy=random.randrange(1,8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((5,10))
        self.image.fill(yellow)
        self.rect=self.image.get_rect()
        self.rect.bottom=y
        self.rect.centerx=x
        self.speedy=-10;
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0:
              self.kill()
            
           
    
all_sprites=pygame.sprite.Group()
enemy_sprites=pygame.sprite.Group()
bullets_sprites=pygame.sprite.Group()
player=Player()
all_sprites.add(player)
for i in range(8):
    temp=Enemy();
    all_sprites.add(temp)
    enemy_sprites.add(temp)
done=False

while not done:
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        elif event.type==pygame.MOUSEBUTTONDOWN:
                player.shoot()
           
           
        
        all_sprites.update()
        try:
            hits=pygame.sprite.groupcollide(enemy_sprites,bullets_sprites,True,True)
          
        except Exception as e:
            print(e)
            print("alex")
        for hit in hits:
            m=Enemy()
            all_sprites.add(m)
            enemy_sprites.add(m)
            score_value+=10
           
        
        
        hits=pygame.sprite.spritecollide(player,enemy_sprites,False)
        if hits:
            done=True
        
        screen.fill(black)
        all_sprites.draw(screen)
        show_score(textX,textY)
 
        pygame.display.update()
        clock.tick(40)


pygame.quit()
quit()


        
        
