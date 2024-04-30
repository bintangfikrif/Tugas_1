import pygame
import math
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Pendopo load gambar
pendopo_img_100 = pygame.image.load('DvD/img/castle/castle_100.png').convert_alpha()
pendopo_img_50 = pygame.image.load('DvD/img/castle/castle_50.png').convert_alpha()
pendopo_img_25 = pygame.image.load('DvD/img/castle/castle_25.png').convert_alpha()

class Pendopo():
    def __init__(self, image100, image50, image25, x, y, scale):
        self.kesehatan = 1000
        self.maks_kesehatan = self.kesehatan
        self.ditembak = False
        self.uang = 0
        self.skor = 0

        width = image100.get_width()
        height = image100.get_height()

        self.gambar100 = pygame.transform.scale(image100, (int(width * scale), int(height * scale)))
        self.gambar50 = pygame.transform.scale(image50, (int(width * scale), int(height * scale)))
        self.gambar25 = pygame.transform.scale(image25, (int(width * scale), int(height * scale)))
        self.rect = self.gambar100.get_rect()
        self.rect.x = x
        self.rect.y = y

    def render(self):
        if self.kesehatan <= 250:
            self.gambar = self.gambar25
        elif self.kesehatan <= 500:
            self.gambar = self.gambar50
        else:
            self.gambar = self.gambar100

        screen.blit(self.gambar, self.rect)

    def perbaiki(self):
        if self.uang >= 1000 and self.kesehatan < self.maks_kesehatan:
            self.kesehatan += 500
            self.uang -= 1000
            if self.kesehatan > self.maks_kesehatan:
                self.kesehatan = self.maks_kesehatan

    def pertahanan(self):
        if self.uang >= 500:
            self.maks_kesehatan += 250
            self.uang -= 500

# Serangan load gambar
img_serangan = pygame.image.load('DvD/img/bullet.png').convert_alpha()
b_w = img_serangan.get_width()
b_h = img_serangan.get_height()
img_serangan = pygame.transform.scale(img_serangan, (int(b_w * 0.07), int(b_h * 0.07)))

class Serangan(pygame.sprite.Sprite):
    def __init__(self, img, x, y, angle):
        pygame.sprite.Sprite.__init__(self)
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle = math.radians(angle)
        self.speed = 12
        self.dx = math.cos(self.angle) * self.speed
        self.dy = -(math.sin(self.angle) * self.speed)
    
    def update(self):
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()
        
        self.rect.x =+ self.dx
        self.rect.y =+ self.dy

# Grouping Serangan
group_serangan = pygame.sprite.Group()

# Buat Pendoponya
pendopo = Pendopo(pendopo_img_100, pendopo_img_50, pendopo_img_25, SCREEN_WIDTH - 250, SCREEN_HEIGHT - 300, 0.3)