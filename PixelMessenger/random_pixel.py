from PIL import Image
import random

# Define the size of the image
width, height = 250, 250

# Create a new image with the RGB mode
image = Image.new('RGB', (width, height))

# Generate random colors for each pixel
for x in range(width):
    for y in range(height):
        # Generate random color
        r = random.randint(0, 150)
        g = random.randint(0, 175)
        b = random.randint(0, 150)
        
        # Set the pixel color
        image.putpixel((x, y), (r, g, b))

# Save the image
image.save("random_pixels.png")

# Show the image
image.show()
