
# Import a library of functions called 'pygame'
import pygame
from pygame.locals import *
from dice import Dice

# Initialize the game engine
pygame.init()
  
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0, 153, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
GRAY = (127,127,127)
YELLOW=(255,255,0)
BASIC=(0, 204,102)

# Set the height and width of the screen
size   = [1800, 1000]
screen = pygame.display.set_mode(size)
  
pygame.display.set_caption("2021 BLUE MARBLE")
font = pygame.font.SysFont('Constantia', 18)
font2 = pygame.font.SysFont('Constantia', 32)
font2 = pygame.font.SysFont('Constantia', 50)

background=pygame.image.load("D:/temp/background.jpg")
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
clicked = False



#문자 입력



def text_input():
    pygame.init()
    clock=pygame.time.Clock()
    base_font = pygame.font.Font(None, 32)


    input_rect = pygame.Rect(200,200,140,32)
    color = pygame.Color('black')

    
    
    
    
    running=True
    user_text=''
    

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
  
             
            if event.type==pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                        running=False
                        return user_text
                    
            else:
                user_text+=event.unicode

    pygame.draw.rect(screen,color,input_rect,2)
                     
    text_surface=base_font.render(user_text,True,(255,255,255,255))
 
    screen.blit(text_surface,(input_rect.x+5,input_rect.y+5))

    
    pygame.display.flip()
    clock.tick(60)






base_font = pygame.font.Font(None, 50)


input_rect = pygame.Rect(600,500,200,60)
color = pygame.Color('black')







class button():
		
	#colours for button and text
	button_col = (50, 30, 255)
	hover_col = (75, 225, 255)
	click_col = (50, 150, 255)
	text_col = BLACK
	width = 180
	height = 70

	def __init__(self, x, y, text):
		self.x = x
		self.y = y
		self.text = text

	def draw_button(self):

		global clicked
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#create pygame Rect object for the button
		button_rect = Rect(self.x, self.y, self.width, self.height)
		
		#check mouseover and clicked conditions
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				clicked = True
				pygame.draw.rect(screen, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
				clicked = False
				action = True
			else:
				pygame.draw.rect(screen, self.hover_col, button_rect)
		else:
			pygame.draw.rect(screen, self.button_col, button_rect)
		
		#add shading to button
		pygame.draw.line(screen, WHITE, (self.x, self.y), (self.x + self.width, self.y), 2)
		pygame.draw.line(screen, WHITE, (self.x, self.y), (self.x, self.y + self.height), 2)
		pygame.draw.line(screen, BLACK, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
		pygame.draw.line(screen, BLACK, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

		#add text to button
		text_img = font.render(self.text, True, self.text_col)
		text_len = text_img.get_width()
		screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
		return action



left = button(550, 350, 'left')
left_diagonal_down = button(750, 350, 'left diagobal down')
down = button(550, 350, 'down')
right_diagonal_down = button(750, 350, 'right diagobal down')
left_diagonal_down2 = button(550, 350, 'left diagobal down')
buy=button(550,350, 'buy')
not_buy=button(750,350, 'not buy')







class player:
    def __init__(self,name,money,x,y):
        self.x=x
        self.y=y
        self.name=name
        self.money=money
        
    def show(self):
        name = font2.render(self.name,True,BLACK)
        screen.blit(name, (self.x,self.y))
        money = font2.render("money={}".format(self.money),True,BLACK)
        screen.blit(money, (self.x,self.y+40))
    
    def change_money(self,money):
        self.money=money
    
class turn:
    def __init__(self):
        self.turn=15
        self.now=1
    
     
    def show(self):
        turn = font2.render("remaning turn={}".format(self.turn),True,BLACK)
        screen.blit(turn, (600,30))
        
class order:
    def __init__(self):
        self.now=1
    
    def change(self):
        self.now+=1
        
    def show(self):
        if self.now%4==1:
            turn = font2.render("now turn=player1",True,BLACK)
            screen.blit(turn, (0,700))
        if self.now%4==2:
            turn = font2.render("now turn=player2",True,BLACK)
            screen.blit(turn, (0,700))
        if self.now%4==3:
            turn = font2.render("now turn=player3",True,BLACK)
            screen.blit(turn, (0,700))
        if self.now%4==0:
            turn = font2.render("now turn=player4",True,BLACK)
            screen.blit(turn, (0,700))     
        
            
 
    
now=order()      
            
t=turn()




pl1=player("player1",470,0,10)
pl2=player("player2",500,0,110)
pl3=player("player3",500,0,210)
pl4=player("player4",500,0,310)





class obj:
    def __init__(self):
        self.x = 1600
        self.y = 750
        self.move=100
        self.cx=7
        self.cy=7

        
    def put_img(self, address):
        if address[-3:0]=="png":
            self.img= pygame.image.load(address).convert_alpha()
        else:
            self.img= pygame.image.load(address) 
        self.sx, self.sy = self.img.get_size()
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx,sy))
        self.sx, self.sy = self.img.get_size()
        
    def show(self):
        screen.blit(self.img, (self.x, self.y))
    
    def fx_move(self):
        self.x+=100
        self.cx+=1
    def bx_move(self):
        self.x-=100
        self.cs-=1
    def fy_move(self):
        self.y-=100
        self.cy-=1
    def by_move(self):
        self.y+=100
        self.cy+=1
    def lcd_move(self):
        self.x-=100
        self.y+=100
        self.cx-=1
        self.cy+=1
    def rcd_move(self):
        self.x+=100
        self.y+=100
        self.cx+=1
        self.cy+=1
    
    def move_(self, a):
        
        while a!=0:
            if self.cx==7:
                if self.cy==7:
                    self.fy_move()
                    a-=1
                if self.cy==6:
                    self.fy_move()
                    a-=1
                if self.cy==5:
                    self.fy_move()
                    a-=1
                if self.cy==4:
                    self.fy_move()
                    a-=1
                if self.cy==3:
                    self.fy_move()
                    a-=1
                if self.cy==2:
                    self.fy_move()
                    a-=1
                if self.cy==1:
                   
    
                        if left.draw_button():  
                            self.dx_move()
                            a-=1
        
                        if left_diagonal_down.draw_button():
                            self.lcd_move()
                            a-=1
                    
                    

            elif self.cx==6:
                if self.cy==7:
                    self.fx_move()
                    a-=1
                if self.cy==6:
                    self.rcd_move()
                    a-=1
                if self.cy==2:
                    self.lcd_move()
                    a-=1
                if self.cy==1:
                    self.dx_move()
                    a-=1
            
            elif self.cx==5:
                if self.cy==7:
                    self.fx_move()
                    a-=1
                if self.cy==5:
                    self.rcd_move()
                    a-=1
                if self.cy==3:
                    self.lcd_move()
                    a-=1
                if self.cy==1:
                    self.dx_move()
                    a-=1
            elif self.cx==4:
                if self.cy==7:
                    self.fx_move()
                    a-=1
                if self.cy==4:
                  
    
                        if left_diagonal_down2.draw_button():  
                            self.lcd_move()
                            a-=1
        
                        if right_diagonal_down.draw_button():
                            self.rcd_move()
                            a-=1
                            
                                
                if self.cy==1:
                    self.dx_move()
                    a-=1
            elif self.cx==3:
                if self.cy==7:
                    self.fx_move()
                    a-=1
                if self.cy==5:
                    self.lcd_move()
                    a-=1
                if self.cy==3:
                    self.rcd_move()
                    a-=1
                if self.cy==1:
                    self.dx_move()
                    a-=1
                
            elif self.cx==2:
                if self.cy==7:
                    self.fx_move()
                    a-=1
                if self.cy==6:
                    self.lcd_move()
                    a-=1
                if self.cy==2:
                    self.rcd_move()
                    a-=1
                if self.cy==1:
                    self.dx_move()
                    a-=1
            elif self.cx==1:
                if self.cy==7:
                    self.fx_move()
                    a-=1
                if self.cy==6:
                    self.dy_move()
                    a-=1
                if self.cy==5:
                    self.dy_move()
                    a-=1
                if self.cy==4:
                    self.dy_move()
                    a-=1
                if self.cy==3:
                    self.dy_move()
                    a-=1
                if self.cy==2:
                    self.dy_move()
                    a-=1
                if self.cy==1:
                  
                        if down.draw_button():  
                            self.dy_move()
                            a-=1
        
                        if right_diagonal_down.draw_button():
                            self.rcd_move()
                            a-=1
                
        
p1=obj()
p1.put_img("D:/temp/RED.png")
p1.change_size(50,50)
p1.x= 1610
p1.y= 340


p2=obj()
p2.put_img("D:/temp/YELLOW.png")
p2.change_size(35,35)
p2.x= 1590-p2.sx
p2.y= 740-p2.sy
    

p3=obj()
p3.put_img("D:/temp/BLUE.png")
p3.change_size(40,40)
p3.x= 1610
p3.y= 705

p4=obj()
p4.put_img("D:/temp/WHITE.png")
p4.change_size(40,40)
p4.x= 1590-p2.sx
p4.y= 780-p2.sy


class circle:
    def __init__(self,color,x,y):
        self.color=color
        self.size=40
        self.x=x
        self.y=y
        self.price=0
        self.sell_price=0
        
    
    
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.size)
        if self.price!=0:
            price=font.render("{}".format(self.price),True,BLACK)
            screen.blit(price,(self.x-10,self.y-10))
            
            
        
    def change_color(self,player):
        if player==1:
            self.color=RED
        elif player==2:
            self.color=YELLOW
        elif player==3:
            self.color=BLUE
        elif player==4:
            self.color=WHITE
    
    def set_price(self,price):
        self.price=price
        self.sell_price=price*2
    
    def get_sell_price(self):
        return self.sell_price
    

c1=circle(GRAY,1600,750)
c2=circle(BASIC,1600,650)
c3=circle(BASIC,1600,550)
c4=circle(BASIC,1600,450)
c5=circle(RED,1600,350)
c6=circle(BASIC,1600,250)
c7=circle(GRAY,1600,150)
c8=circle(BASIC,1500,150)
c9=circle(BASIC,1400,150)
c10=circle(BASIC,1300,150)
c11=circle(BASIC,1200,150)
c12=circle(BASIC,1100,150)
c13=circle(GRAY,1000,150)
c14=circle(BASIC,1000,250)
c15=circle(BASIC,1000,350)
c16=circle(BASIC,1000,450)
c17=circle(BASIC,1000,550)
c18=circle(BASIC,1000,650)
c19=circle(GRAY,1000,750)
c20=circle(BASIC,1100,750)
c21=circle(BASIC,1200,750)
c22=circle(BASIC,1300,750)
c23=circle(BASIC,1400,750)
c24=circle(BASIC,1500,750)
c25=circle(BASIC,1500,650)
c26=circle(BASIC,1400,550)
c27=circle(GRAY,1300,450)
c28=circle(BASIC,1200,350)
c29=circle(BASIC,1100,250)
c30=circle(BASIC,1500,250)
c31=circle(BASIC,1400,350)
c32=circle(BASIC,1200,550)
c33=circle(BASIC,1100,650)


while not done:
  
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(30)
      
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
  
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
      
    # Clear the screen and set the screen background
    
    
    screen.blit(background,(0,0))
    # Draw a circle outline
    d1=[1600,750]
    d2=[1600,650]
    d3=[1600,550]
    d4=[1600,450]
    d5=[1600,350]
    d6=[1600,250]
    d7=[1600,150]
    d8=[1500,150]
    d9=[1400,150]
    d10=[1300,150]
    d11=[1200,150]
    d12=[1100,150]
    d13=[1000,150]
    d14=[1000,250]
    d15=[1000,350]
    d16=[1000,450]
    d17=[1000,550]
    d18=[1000,650]
    d19=[1000,750]
    d20=[1100,750]
    d21=[1200,750]
    d22=[1300,750]
    d23=[1400,750]
    d24=[1500,750]
    d25=[1500,650]
    d26=[1400,550]
    d27=[1300,450]
    d28=[1200,350]
    d29=[1100,250]
    d30=[1500,250]
    d31=[1400,350]
    d32=[1200,550]
    d33=[1100,650]
    
    
    
    
    c1.draw()
    c2.draw()
    c3.draw()
    c4.draw()
    c5.draw()
    c5.set_price(30)
    c6.draw()
    c7.draw()
    c8.draw()
    c9.draw()
    c10.draw()
    c11.draw()
    c12.draw()
    c13.draw()
    c14.draw()
    c15.draw()
    c16.draw()
    c17.draw()
    c18.draw()
    c19.draw()
    c20.draw()
    c21.draw()
    c22.draw()
    c23.draw()
    c24.draw()
    c25.draw()
    c26.draw()
    c27.draw()
    c28.draw()
    c29.draw()
    c30.draw()
    c31.draw()    
    c32.draw()
    c33.draw()
 
    
    
    p1.show()
    p2.show() 
    p3.show() 
    p4.show() 
    pl1.show()
    pl2.show()
    pl3.show()
    pl4.show()

    t.show()
    now.show()
    pygame.draw.rect(screen,color,input_rect,2)
                     
    text_surface=base_font.render("set price",True,BLACK)
 
    screen.blit(text_surface,(input_rect.x,input_rect.y-60))            
        

 
    
    


    
    



    pygame.display.flip()


    

  
# Be IDLE friendly
pygame.quit()

