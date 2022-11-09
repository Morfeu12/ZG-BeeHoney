import pygame

class Obj: # Criar objetos sprites com imagens

    def __init__(self, image, x, y):

        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)
        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y
        self.frame = 1
        self.tick = 0

    def drawing(self, window):
        self.group.draw(window)
    
    def animation(self, obj, frames, tick = 8, extension = "png"):
        self.tick += 1

        if self.tick >= tick: # A cada 8 frames (padrão) vai trocar a imagem
            self.tick = 0
            self.frame += 1

        if self.frame >= frames:
            self.frame = 1
        
        self.sprite.image = pygame.image.load(f'assets/{obj}{self.frame}.{extension}') 

class Bee(Obj):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)

        self.sound_pts = pygame.mixer.Sound("assets/sounds/score.ogg")
        self.sound_colision = pygame.mixer.Sound("assets/sounds/bateu.ogg")
        self.life = 3
        self.pts = 0
    
    def move_bee(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35 # Metade da largura da imagem
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 29 # Metade da altura da imagem

    def colision(self, group, name):
        colison = pygame.sprite.spritecollide(self.sprite, group, True)

        if name == "Flower" and colison:
            self.pts += 1
            self.sound_pts.play()
            
        elif name == "Spider" and colison:
            self.life -= 1
            self.sound_colision.play()

class Text: 
    
    def __init__(self, size, text, color = (255,255,255), fontfamily = "Arial bold"):
        self.font = pygame.font.SysFont(fontfamily, size)
        self.render = self.font.render(text, True,color)

    def draw(self, window, x, y): 
        window.blit(self.render, (x,y))
    
    def update_text(self, text, color = (255,255,255)):
        self.render = self.font.render(text, True, color)

    

