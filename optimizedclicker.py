import sys
import pygame
import random

global cash
cash = 0.00
day = 0
year = 18
food = 1
radio = False
pygame.font.init()


pygame.display.set_caption('Clicker Game')

surface = pygame.display.set_mode((300,300))
color = (67, 40, 24)

screen = pygame.display.set_mode((800,800))
background_colour = (187, 148, 87)
screen.fill(background_colour)



 
def button(a, b, c, d):
    pygame.draw.rect(surface, color, pygame.Rect(a, b, c, d))       

def clear_screen():
    pygame.draw.rect(screen, (187, 148, 87), (0, 0, 800, 800))
    
    


def clicklocation(a, b, c, d):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pos()[0] > a and pygame.mouse.get_pos()[0] < a+c:
            if pygame.mouse.get_pos()[1] > b and pygame.mouse.get_pos()[1] < b+d:
                return True
            
def continuegame():
    global cash, day, year, food, radio
    filename = open('clicker.txt', 'r')
    cash = float(filename.readline())
    day = int(filename.readline())
    year = int(filename.readline())
    food = int(filename.readline())
    radio = bool(filename.readline())
    filename.close()
                
    


                    

    
                
def font(t, s=72, c=(255,255,0), b=False, i=False):
    font = pygame.font.SysFont("Arial", 72)
    text = font.render(str(round(cash, 2)), True, ((153, 88, 42)))
    return text

def dailycost():
    global cash
    cash -= food 
    
def time():
    global day
    global year
    day += 1
    
    if day >= 365:
        year += 1
        day = 0

def beg():
    global cash
    beggar_earnings = round(random.uniform(0.00, 3.00), 2)
    cash += beggar_earnings
    time()
    dailycost()
    
        

def printing(fontsize, text, a, b, c):
    font = pygame.font.SysFont("Arial", fontsize)
    text = font.render(text, True, (a, b, c))
    return text

def filesave():
    if event.type == pygame.QUIT:
            
        filename = open('clicker.txt', 'w')
        filename.write(str(round(cash, 2)))
        filename.write("\n")
        filename.write(str(day))
        filename.write("\n")
        filename.write(str(year))
        filename.write("\n")
        filename.write(str(food))
        filename.write("\n")
        filename.write(str(bool(radio)))
        filename.close()
            
        exit()    
        
def dancer():
    global cash
    if radio == True:
        dancer_earnings = round(random.uniform(0.00, 6.00), 2)
        cash += dancer_earnings
        time()
        dailycost()
               
        
        
        
startup = True               
while startup == True:
    
    screen.blit(printing(72, "Continue", 153, 88, 42), (20,10))
    button(200, 200, 90, 90)
    screen.blit(printing(72, "New Game", 153, 88, 42), (400,10))
    button(600, 200, 90, 90)
    
    for event in pygame.event.get():
        
        if pygame.mouse.get_pressed() == (1, 0, 0):
            
            if clicklocation(200, 200, 90, 90) == True:
                continuegame()     
                startup = False
                menu = True
                
            if clicklocation(600, 200, 90, 90) == True:
                startup = False
                menu = True
           
            
            
        if event.type == pygame.QUIT:
            exit()
            
    pygame.display.flip()
      

while menu == True:
    
    clear_screen()
    screen.blit(printing(72, "Menu", 153, 88, 42), (328,10))
    
    button(10, 100, 90, 90)
    screen.blit(printing(20, "Street", 153, 88, 42), (30, 110))
    screen.blit(printing(20, "Jobs", 153, 88, 42), (30, 140))
    
    button(10, 210, 90, 90)
    screen.blit(printing(20, "Store", 153, 88, 42), (30, 230))
    
    for event in pygame.event.get():
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if clicklocation(10, 100, 90, 90) == True:
                streetjobs = True
                
                menu = False
                
            if clicklocation(10, 210, 90, 90) == True:
                store = True
                streetjobs = False
                menu = False
                    
        filesave()
    
    pygame.display.flip()
    
while streetjobs == True:
    
    
    clear_screen()
    
    countprint = font(cash)
    screen.blit(countprint, (10,10))
    
    screen.blit(printing(72, "Street Jobs", 153, 88, 42), (400, 10))
    
    button(110, 100, 50, 50)
    screen.blit(printing(20, "Beg", 0, 0, 0), (20, 100))
    
    button(110, 170, 50, 50)
    screen.blit(printing(20, "Dancer", 0, 0, 0), (20, 170))
    
       
    for event in pygame.event.get():
        
        if pygame.mouse.get_pressed() == (1, 0, 0):
            
            if clicklocation(110, 100, 50, 50) == True:
                beg()
                 
            if clicklocation(110, 170, 50, 50) == True:
                dancer()
               
        filesave()
      
    pygame.display.flip()    
    
while store == True:
    clear_screen()
    
    button(10, 100, 50, 50)
    screen.blit(printing(20, "Street", 0, 0, 0), (20, 130))
    screen.blit(printing(20, "Items", 0, 0, 0), (20, 150))
    for event in pygame.event.get():
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if clicklocation(10, 100, 50, 50) == True:
                street_item_store = True
                store = False

        filesave()
    pygame.display.flip()

    
while street_item_store == True:
    clear_screen()
    
    button(100, 100, 50, 50)
    screen.blit(printing(20, "radio", 0, 0, 0), (10, 100))
    screen.blit(printing(20, "Cost: 50", 0, 0, 0), (10, 120))
    for event in pygame.event.get():
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if clicklocation(100, 100, 50, 50) == True:
                if radio == True:
                    screen.blit(printing(20, "Already bought", 0, 0, 0), (10, 50))
                    print('hi')
                if radio == False:
                    if cash >= 50.00:
                        cash = cash - 50.00
                        radio = True
                        print('llllllll')
                
        filesave()
    pygame.display.flip()

    
