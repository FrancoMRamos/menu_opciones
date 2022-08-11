import pygame, sys
from button import Button

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")
img_fondo = pygame.image.load("assets/Background.png")

def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        pos_mouse = pygame.mouse.get_pos()

        screen.fill("black")

        iniciar_texto = get_font(45).render("Pantalla de Flappy.", True, "White")
        iniciar_rect = iniciar_texto.get_rect(center=(640, 260))
        screen.blit(iniciar_texto, iniciar_rect)

        finiciar_salida = Button(image=None, pos=(640, 460), 
                            text_input="Retroceder", font=get_font(75), base_color="White", hovering_color="Green")

        finiciar_salida.changeColor(pos_mouse)
        finiciar_salida.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if finiciar_salida.checkForInput(pos_mouse):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = get_font(45).render("Pantalla opciones.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        fopciones_salida = Button(image=None, pos=(640, 460), 
                            text_input="Retroceder", font=get_font(75), base_color="Black", hovering_color="Green")

        fopciones_salida.changeColor(OPTIONS_MOUSE_POS)
        fopciones_salida.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if fopciones_salida.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        screen.blit(img_fondo, (0, 0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("Menu principal", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        #BOTONES DEL MENU
        boton_jugar = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="Jugar", font=get_font(36), base_color="#d7fcd4", hovering_color="White")
        boton_opciones = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="Opciones", font=get_font(36), base_color="#d7fcd4", hovering_color="White")
        boton_salir = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="Salir", font=get_font(36), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [boton_jugar, boton_opciones, boton_salir]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.checkForInput(MENU_MOUSE_POS):
                    play()
                if boton_opciones.checkForInput(MENU_MOUSE_POS):
                    options()
                if boton_salir.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()