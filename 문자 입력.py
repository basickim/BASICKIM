import pygame

pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode([1800,1000])
base_font = pygame.font.Font(None, 32)


input_rect = pygame.Rect(800,200,140,32)
color = pygame.Color('black')

user_text=''
price=''

running=True

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
  
             
        if event.type==pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif event.key == pygame.K_RETURN:
                running=False
                price=user_text
                    
            else:
                user_text+=event.unicode
            
    screen.fill((0,0,0))
    
       
    pygame.draw.rect(screen,color,input_rect,2)
                     
    text_surface=base_font.render(user_text,True,(255,255,255))
    text_surface2=base_font.render('enter price',True,(255,255,255))
 
    screen.blit(text_surface,(input_rect.x+5,input_rect.y+5))
    screen.blit(text_surface2,(input_rect.x+5,input_rect.y-30))

    
    pygame.display.flip()
    clock.tick(60)
        
