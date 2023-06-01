import pygame
import pymunk

# Initialize Pygame
pygame.init()

# Set up the window
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pymunk Demo")

# Set up the clock
clock = pygame.time.Clock()

# Set up the physics space
space = pymunk.Space()
space.gravity = (0, 1000)

# Set up the ball
radius = 25
mass = 10
moment = pymunk.moment_for_circle(mass, 0, radius)
body = pymunk.Body(mass, moment)
body.position = (width/2, height/2)
shape = pymunk.Circle(body, radius)
space.add(body, shape)

# Set up the floor
floor_y = 550
floor = pymunk.Segment(space.static_body, (0, floor_y), (width, floor_y), 5)
space.add(floor)

# Set up the key interaction
bounce = False

# Set up the impulse for bouncing
impulse = 5000

# Run the simulation
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bounce = True

    # Clear the screen
    screen.fill((255, 255, 255))

    # Update the physics space
    dt = 1/60.0
    if bounce:
        body.apply_impulse_at_local_point((0, -impulse))
        bounce = False
    space.step(dt)

    # Draw the ball
    pos = body.position
    pygame.draw.circle(screen, (255, 0, 0), (int(pos.x), int(pos.y)), radius)

    # Draw the floor
    pygame.draw.line(screen, (0, 0, 0), (0, floor_y), (width, floor_y), 5)

    # Update the display
    pygame.display.update()

    # Wait for the next frame
    clock.tick(60)

# Clean up
pygame.quit()
