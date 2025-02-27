import pygame
import math
import random
from pygame import Vector2

class GameObject:
    def __init__(self, position, velocity=Vector2(0, 0)):
        self.position = Vector2(position)
        self.velocity = Vector2(velocity)
        self.alive = True

    def update(self, screen_width, screen_height):
        self.position += self.velocity
        # Screen wrapping
        self.position.x %= screen_width
        self.position.y %= screen_height

class Asteroid(GameObject):
    def __init__(self, position, size=3):
        # Random velocity between -2 and 2
        velocity = Vector2(random.uniform(-2, 2), random.uniform(-2, 2))
        super().__init__(position, velocity)
        self.size = size
        self.radius = size * 10
        # Create a random polygon shape for the asteroid
        self.points = self._generate_points()
        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-3, 3)

    def _generate_points(self):
        num_points = 8
        points = []
        for i in range(num_points):
            angle = (i / num_points) * 2 * math.pi
            # Add some randomness to the radius
            distance = self.radius * random.uniform(0.8, 1.2)
            x = math.cos(angle) * distance
            y = math.sin(angle) * distance
            points.append((x, y))
        return points

    def update(self, screen_width, screen_height):
        super().update(screen_width, screen_height)
        self.rotation = (self.rotation + self.rotation_speed) % 360

    def draw(self, screen):
        # Rotate and translate points
        angle = math.radians(self.rotation)
        rotated_points = []
        for point in self.points:
            x = point[0] * math.cos(angle) - point[1] * math.sin(angle)
            y = point[0] * math.sin(angle) + point[1] * math.cos(angle)
            rotated_points.append((x + self.position.x, y + self.position.y))
        pygame.draw.polygon(screen, (255, 255, 255), rotated_points, 2)

    def split(self):
        if self.size > 1:
            # Create two smaller asteroids
            new_asteroids = []
            for _ in range(2):
                new_pos = Vector2(self.position)
                new_asteroid = Asteroid(new_pos, self.size - 1)
                new_asteroids.append(new_asteroid)
            return new_asteroids
        return []

class Bullet(GameObject):
    def __init__(self, position, angle):
        # Calculate velocity based on angle
        speed = 10
        velocity = Vector2(math.cos(math.radians(angle - 90)),
                         math.sin(math.radians(angle - 90))) * speed
        super().__init__(position, velocity)
        self.lifetime = 60  # frames
        self.radius = 2

    def update(self, screen_width, screen_height):
        super().update(screen_width, screen_height)
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.alive = False

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

def check_collision(obj1, obj2):
    """Check collision between two objects using circle collision"""
    distance = (obj1.position - obj2.position).length()
    return distance < (obj1.radius + obj2.radius)
