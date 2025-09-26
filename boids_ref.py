# Boids Particle System
# - create boids class that updates and draws position. 
# - add velocity, acceleration, max speed and max force
# - add and apply behaviours: alignment, cohesion, seperation
# - create boids function to add many of them
#
 
import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boids Simulation")

class Boid:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.acceleration = pygame.Vector2(0, 0)
        self.max_speed = 2
        self.max_force = 0.03

    def update(self):
        self.velocity += self.acceleration
        if self.velocity.length() > self.max_speed:
            self.velocity.scale_to_length(self.max_speed) 
        self.position += self.velocity
        self.acceleration *= 0

        # Boundary conditions
        if self.position.x < 0: self.position.x = WIDTH
        if self.position.x > WIDTH: self.position.x = 0
        if self.position.y < 0: self.position.y = HEIGHT
        if self.position.y > HEIGHT: self.position.y = 0

    def apply_behavior(self, boids):
        alignment = self.align(boids)
        cohesion = self.cohere(boids)
        separation = self.separate(boids)

        self.acceleration += alignment * 1.0
        self.acceleration += cohesion * 1.0
        self.acceleration += separation * 1.5

    def align(self, boids):
        perception_radius = 50
        steering = pygame.Vector2(0, 0)
        total = 0
        for other in boids:
            if other is not self and self.position.distance_to(other.position) < perception_radius:
                steering += other.velocity
                total += 1
        if total > 0:
            steering /= total
            steering = steering.normalize() * self.max_speed
            steering -= self.velocity
            steering = steering.normalize() * self.max_force
        return steering

    def cohere(self, boids):
        perception_radius = 50
        steering = pygame.Vector2(0, 0)
        total = 0
        for other in boids:
            if other is not self and self.position.distance_to(other.position) < perception_radius:
                steering += other.position
                total += 1
        if total > 0:
            steering /= total
            steering -= self.position
            steering = steering.normalize() * self.max_speed
            steering -= self.velocity
            steering = steering.normalize() * self.max_force
        return steering

    def separate(self, boids):
        perception_radius = 25
        steering = pygame.Vector2(0, 0)
        total = 0
        for other in boids:
            if other is not self and self.position.distance_to(other.position) < perception_radius:
                diff = self.position - other.position
                diff /= self.position.distance_to(other.position)
                steering += diff
                total += 1
        if total > 0:
            steering /= total
            if steering.length() != 0:
                steering = steering.normalize() * self.max_speed
                steering -= self.velocity
                steering = steering.normalize() * self.max_force
        return steering
  
    def draw_boid(self, screen, color, height, width,strokew):
        top = pygame.Vector2(self.position + height*self.velocity.normalize())
        right = pygame.Vector2(self.position + width*self.velocity.normalize().rotate(90))
        left = pygame.Vector2(self.position + width*self.velocity.normalize().rotate(-90))
        dir = self.velocity.normalize()*height
        #center triangle
        top -= dir*.4
        right -= dir*.4
        left -= dir*.4
        pygame.draw.polygon(screen, color, [top, left, right], strokew)

    def draw(self, screen):
        self.draw_boid(screen, 'white', 14, 7, 2)


def create_boids(num_boids):
    return [Boid(random.uniform(0, WIDTH), random.uniform(0, HEIGHT)) for _ in range(num_boids)]

def main():
    num_boids = 300
    boids = create_boids(num_boids)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('black')

        for boid in boids:
            boid.apply_behavior(boids)
            boid.update()
            boid.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()