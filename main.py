import pygame
import math
import random
from pygame import Vector2

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Player:
    def __init__(self):
        self.position = Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.velocity = Vector2(0, 0)
        self.acceleration = 0.5
        self.rotation = 0
        self.rotation_speed = 5
        self.points = [(0, -20), (-10, 10), (10, 10)]
        
    def rotate(self, direction):
        self.rotation += direction * self.rotation_speed
        
    def thrust(self):
        # Convert rotation to radians and calculate thrust vector
        angle = math.radians(self.rotation - 90)
        thrust = Vector2(math.cos(angle), math.sin(angle))
        self.velocity += thrust * self.acceleration
        
    def update(self):
        # Update position based on velocity
        self.position += self.velocity
        
        # Screen wrapping
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT
        
        # Apply friction
        self.velocity *= 0.98
        
    def draw(self, screen):
        # Rotate and translate points
        angle = math.radians(self.rotation)
        rotated_points = []
        for point in self.points:
            x = point[0] * math.cos(angle) - point[1] * math.sin(angle)
            y = point[0] * math.sin(angle) + point[1] * math.cos(angle)
            rotated_points.append((x + self.position.x, y + self.position.y))
            
        pygame.draw.polygon(screen, WHITE, rotated_points, 2)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Blasteroids")
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.running = True
        
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.rotate(-1)
        if keys[pygame.K_RIGHT]:
            self.player.rotate(1)
        if keys[pygame.K_UP]:
            self.player.thrust()
    
    def update(self):
        self.player.update()
    
    def draw(self):
        self.screen.fill(BLACK)
        self.player.draw(self.screen)
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_input()
            self.update()
            self.draw()
        
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
