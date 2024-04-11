import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    screen.fill((255, 255, 255))
    color = 'red'
    shape = "circle"
    prevColor = color

    while True:
        cursorCord = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.display.set_caption("Paint")
        
        #draw mode
        pygame.draw.circle(screen, 'black', (20, 20), 15)
        circleButton = pygame.Rect(5, 5, 30, 30)

        pygame.draw.rect(screen, 'black', (50, 5, 45, 30))
        rectButton = pygame.Rect(50, 5, 45, 30)

        pygame.draw.polygon(screen, 'black',[[130, 5], [155, 5], [135, 35], [110, 35]])
        eraserButton = pygame.Rect(110, 5, 45, 30)

        pygame.draw.rect(screen, 'black', (170, 5, 30, 30))
        squareButton = pygame.Rect(170, 5, 30, 30)

        pygame.draw.polygon(screen, 'black', [[230, 5], [215, 35], [245, 35], [246, 35]])
        triangleButton = pygame.Rect(215, 5, 30, 30)

        pygame.draw.polygon(screen, 'black', [[260, 20], [270, 5], [280, 20], [270, 35]])
        rhombButton = pygame.Rect(260, 5, 20, 30)



        pygame.draw.circle(screen, 'red', (620, 20), 15)
        redButton = pygame.Rect(560, 5, 30, 30)
        pygame.draw.circle(screen, 'blue', (575, 20), 15)
        blueButton = pygame.Rect(605, 5, 30, 30)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        #making logic
        pressed = pygame.key.get_pressed()
        if(circleButton.collidepoint(cursorCord)):
            if(click[0] and not clicked): 
                clicked = True
                print("Circle picked")
                shape = "circle"
                color = prevColor
            if(not click[0]): clicked = False

        if(rectButton.collidepoint(cursorCord)):
            if(click[0] and not clicked): 
                clicked = True
                print("rectangle picked")
                shape = "rect"
                color = prevColor
            if(not click[0]): clicked = False

        if(eraserButton.collidepoint(cursorCord)):
            if(click[0] and not clicked): 
                clicked = True
                print("eraser picked")
                shape = "eraser"
                prevColor = color
                color = "white"
            if(not click[0]): clicked = False

        if(redButton.collidepoint(cursorCord)):
            if(click[0] and not clicked): 
                clicked = True
                print("red color picked")
                color = "blue"
            if(not click[0]): clicked = False

        if(blueButton.collidepoint(cursorCord)):
            if(click[0] and not clicked): 
                clicked = True
                print("blue color picked")
                color = "red"
            if(not click[0]): clicked = False

        if(squareButton.collidepoint(cursorCord)):
            if(click[0] and not clicked): 
                clicked = True
                print("square picked")
                shape = "square"
                color = prevColor
            if(not click[0]): clicked = False

        if(triangleButton.collidepoint(cursorCord)):
            if(click[0] and not clicked): 
                clicked = True
                print("triangle picked")
                shape = "triangle"
                color = prevColor
            if(not click[0]): clicked = False

        if(rhombButton.collidepoint(cursorCord)):
            if(click[0] and not clicked): 
                clicked = True
                print("rhombus picked")
                shape = "rhomb"
                color = prevColor
            if(not click[0]): clicked = False

        if(not click[0]): clicked = False

        #drawing shapes
        if click[0] and not clicked:
            if(shape == "circle"): pygame.draw.circle(screen, color, cursorCord, 5)
            elif(shape == "rect"): pygame.draw.rect(screen, color, (cursorCord[0]-5, cursorCord[1]-3, 10, 6))
            elif(shape == "eraser"): pygame.draw.rect(screen, color, (cursorCord[0]-5, cursorCord[1]-3, 10, 6))
            elif(shape == "square"): pygame.draw.rect(screen, color, (cursorCord[0]-5, cursorCord[1]-3, 10, 10))
            elif(shape == "triangle"): pygame.draw.polygon(screen, color, [[cursorCord[0]-5, cursorCord[1]+5], [cursorCord[0], cursorCord[1]-5], [cursorCord[0]+5, cursorCord[1]+5], [cursorCord[0]+6, cursorCord[1]+5]])
            elif(shape == "rhomb"): pygame.draw.polygon(screen, color, [[cursorCord[0]-5, cursorCord[1]], [cursorCord[0], cursorCord[1]-5], [cursorCord[0]+5, cursorCord[1]], [cursorCord[0], cursorCord[1]+5]])


        
        
        pygame.display.flip()
        clock.tick(144)
    

main()