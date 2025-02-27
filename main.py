import pygame
import math
import random
import time
from pygame import Vector2
from game_objects import Asteroid, Bullet, check_collision
from sound_manager import SoundManager

# Initialize Pygame and its mixer
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

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
        self.radius = 20
        self.invulnerable = False
        self.invulnerable_timer = 0
        self.lives = 3
        
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

        # Update invulnerability
        if self.invulnerable:
            self.invulnerable_timer -= 1
            if self.invulnerable_timer <= 0:
                self.invulnerable = False
        
    def draw(self, screen):
        if self.invulnerable and pygame.time.get_ticks() % 200 < 100:
            return  # Skip drawing to create blinking effect

        # Rotate and translate points
        angle = math.radians(self.rotation)
        rotated_points = []
        for point in self.points:
            x = point[0] * math.cos(angle) - point[1] * math.sin(angle)
            y = point[0] * math.sin(angle) + point[1] * math.cos(angle)
            rotated_points.append((x + self.position.x, y + self.position.y))
            
        pygame.draw.polygon(screen, WHITE, rotated_points, 2)

    def shoot(self):
        return Bullet(Vector2(self.position), self.rotation)

    def hit(self):
        if not self.invulnerable:
            self.lives -= 1
            self.invulnerable = True
            self.invulnerable_timer = 90  # 1.5 seconds at 60 FPS
            self.position = Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            self.velocity = Vector2(0, 0)
            return True
        return False

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Blasteroids")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 64)
        self.small_font = pygame.font.Font(None, 36)
        self.reset_game()
        
    def reset_game(self):
        """Reset the game state for a new game"""
        self.player = Player()
        self.asteroids = []
        self.bullets = []
        self.running = True
        self.game_over = False
        self.score = 0
        self.level = 1
        self.sound_manager = SoundManager()
        self.spawn_asteroids(3)  # Start with 3 asteroids

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.game_over:
                        self.running = False
                    else:
                        self.game_over = True
                        self.sound_manager.play('game_over')
                elif event.key == pygame.K_SPACE:
                    if self.game_over:
                        self.reset_game()
                    else:
                        self.bullets.append(self.player.shoot())
                        self.sound_manager.play('shoot')
                    
        if not self.game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.rotate(-1)
            if keys[pygame.K_RIGHT]:
                self.player.rotate(1)
            if keys[pygame.K_UP]:
                self.player.thrust()
                self.sound_manager.play_thrust()
            else:
                self.sound_manager.stop_thrust()

    def draw_game_over(self):
        """Draw the game over screen"""
        # Create semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(128)
        self.screen.blit(overlay, (0, 0))

        # Draw "GAME OVER" text
        game_over_text = self.font.render("GAME OVER", True, WHITE)
        score_text = self.small_font.render(f"Final Score: {self.score}", True, WHITE)
        level_text = self.small_font.render(f"Level Reached: {self.level}", True, WHITE)
        continue_text = self.small_font.render("Press SPACE to Play Again", True, WHITE)
        quit_text = self.small_font.render("Press ESC to Quit", True, WHITE)

        # Position all text elements
        game_over_rect = game_over_text.get_rect(centerx=SCREEN_WIDTH//2, centery=SCREEN_HEIGHT//2 - 80)
        score_rect = score_text.get_rect(centerx=SCREEN_WIDTH//2, centery=SCREEN_HEIGHT//2)
        level_rect = level_text.get_rect(centerx=SCREEN_WIDTH//2, centery=SCREEN_HEIGHT//2 + 40)
        continue_rect = continue_text.get_rect(centerx=SCREEN_WIDTH//2, centery=SCREEN_HEIGHT//2 + 100)
        quit_rect = quit_text.get_rect(centerx=SCREEN_WIDTH//2, centery=SCREEN_HEIGHT//2 + 140)

        # Draw all text elements
        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(score_text, score_rect)
        self.screen.blit(level_text, level_rect)
        self.screen.blit(continue_text, continue_rect)
        self.screen.blit(quit_text, quit_rect)

    def spawn_asteroids(self, count):
        for _ in range(count):
            # Spawn asteroids away from the player
            while True:
                pos = Vector2(random.randrange(SCREEN_WIDTH),
                            random.randrange(SCREEN_HEIGHT))
                if (pos - self.player.position).length() > 100:
                    self.asteroids.append(Asteroid(pos))
                    break

    def update(self):
        if not self.game_over:
            current_time = time.time()
            self.sound_manager.update_background(self.level, current_time)
            
            self.player.update()

            # Update bullets
            for bullet in self.bullets[:]:
                bullet.update(SCREEN_WIDTH, SCREEN_HEIGHT)
                if not bullet.alive:
                    self.bullets.remove(bullet)

            # Update asteroids
            for asteroid in self.asteroids[:]:
                asteroid.update(SCREEN_WIDTH, SCREEN_HEIGHT)

                # Check for bullet collisions
                for bullet in self.bullets[:]:
                    if check_collision(asteroid, bullet):
                        self.asteroids.remove(asteroid)
                        self.bullets.remove(bullet)
                        self.score += (4 - asteroid.size) * 100
                        
                        # Play appropriate explosion sound
                        if asteroid.size >= 2:
                            self.sound_manager.play('explosion_large')
                        else:
                            self.sound_manager.play('explosion_small')
                        
                        # Split asteroid
                        new_asteroids = asteroid.split()
                        self.asteroids.extend(new_asteroids)
                        break

                # Check for player collision
                if check_collision(self.player, asteroid):
                    if self.player.hit():
                        self.sound_manager.play('explosion_large')
                        if self.player.lives <= 0:
                            self.game_over = True
                            self.sound_manager.play('game_over')
                        break

            # Check if all asteroids are destroyed
            if not self.asteroids:
                self.level += 1
                self.sound_manager.play('level_up')
                self.spawn_asteroids(2 + self.level)
    
    def draw(self):
        self.screen.fill(BLACK)
        
        # Draw game objects
        self.player.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
        for asteroid in self.asteroids:
            asteroid.draw(self.screen)

        # Draw HUD
        score_text = self.small_font.render(f"Score: {self.score}", True, WHITE)
        lives_text = self.small_font.render(f"Lives: {self.player.lives}", True, WHITE)
        level_text = self.small_font.render(f"Level: {self.level}", True, WHITE)
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 50))
        self.screen.blit(level_text, (SCREEN_WIDTH - 100, 10))

        if self.game_over:
            self.draw_game_over()
        
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
