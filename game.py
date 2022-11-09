from obj import Obj, Bee, Text
import random

class Game:

    def __init__(self):
        
        # Wall paper
        self.bg = Obj("assets/bg.png", 0, 0)
        self.bg2 = Obj("assets/bg.png", 0, -640)

        # Enemy
        self.spider = Obj("assets/spider1.png", random.randrange(0,280), -10)
        self.speed_spider = 8

        # Personagem 
        self.bee = Bee("assets/bee1.png", 150, 550)
        
        # Pontos
        self.flower = Obj("assets/florwer1.png", random.randrange(0,330), -100)
        self.speed_flower = 5

        # Score 
        self.score = Text(80, str(self.bee.pts))
        self.lifes = Text(25, f'Lifes: {str(self.bee.life)}')

        # Controlador de cenas
        self.change_scene = False

    def draw(self, window): 
        self.bg.group.draw(window)
        self.bg2.group.draw(window)
        self.spider.group.draw(window)
        self.flower.group.draw(window)
        self.bee.group.draw(window)
        self.score.draw(window, 160, 12)
        self.lifes.draw(window, 8, 12)

    def update(self): 
        self.move_bg() 
        self.spider.animation("spider",5)
        self.bee.animation("bee",5, 2)
        self.flower.animation("florwer", 3)
        self.move_spider()
        self.move_flower()
        self.bee.colision(self.flower.group, "Flower")
        self.bee.colision(self.spider.group, "Spider")
        self.score.update_text(str(self.bee.pts))
        self.lifes.update_text(f'Lifes: {str(self.bee.life)}')
        self.gameover()
        
    def move_bg(self):
        self.bg.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4
        if self.bg.sprite.rect[1] >= 640:
            self.bg.sprite.rect[1] = 0
        if self.bg2.sprite.rect[1] >= 0:
            self.bg2.sprite.rect[1] = -640

    def move_spider(self):
        self.spider.sprite.rect[1] += self.speed_spider
        if self.spider.sprite.rect[1] >= 690:
            self.spider.sprite.kill()
            self.spider = Obj("assets/spider1.png", random.randrange(-40,320), -10)
    
    def move_flower(self):
        self.flower.sprite.rect[1] += self.speed_flower
        if self.flower.sprite.rect[1] >= 690:
            self.flower.sprite.kill()
            self.flower = Obj("assets/florwer1.png", random.randrange(0,330), -20)

    def gameover(self):
        if self.bee.life <= 0:
            self.change_scene = True
        
