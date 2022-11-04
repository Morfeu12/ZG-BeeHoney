import pygame

class Main: 

    def __init__(self, sizex, sizey, title):
        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)
        self.run = True

    def draw(self, path, x, y):
        self.img = pygame.image.load(path)
        # self.rect = self.img.get_rect() # Retorna um array [posicaoX[0], posicaoY[1], tamanhoX[2], tamanhoY[3]]
        # self.rect[0] = x
        # self.rect[1] = y
        # self.window.blit(self.img, (self.rect[0], self.rect[1]))
        self.window.blit(self.img, (x, y))

    def events(self): 
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.run = False
    
    def update(self):

        while self.run == True:
            # self.draw()
            self.events()
            pygame.display.flip() # Renderiza a tela
            pygame.time.Clock().tick(60) # Controla o FPS       

# Chamar a class Main passando as largura, altura e titulo da janela
# game = Main(1200, 720, "Hello world!")
# Iniciar o loop para o game
# game.update()