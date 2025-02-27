from PIL import Image, ImageDraw

# Create a new image with a black background
size = (256, 256)
image = Image.new('RGBA', size, (0, 0, 0, 0))
draw = ImageDraw.Draw(image)

# Draw a simple spaceship
ship_points = [
    (128, 50),  # top
    (50, 206),  # bottom left
    (128, 156), # bottom middle
    (206, 206), # bottom right
]
draw.polygon(ship_points, fill=(255, 255, 255, 255))

# Add some asteroids
asteroid_positions = [(60, 60), (200, 100), (150, 180)]
for pos in asteroid_positions:
    draw.ellipse([pos[0]-20, pos[1]-20, pos[0]+20, pos[1]+20], 
                 outline=(255, 255, 255, 255), width=3)

# Save as ICO
image.save('icon.ico', format='ICO')
