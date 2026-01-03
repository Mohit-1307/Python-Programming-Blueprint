# Import necessary libraries to handle command line arguments, open images, and save GIFs.
import sys
from PIL import Image

# Initialize an empty list to store the images.
images = []

# Open each image specified in the command line arguments and append them to the list.
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# Check Mark
if not images:
    print("Usage: python script.py img1.png img2.png ...")
    sys.exit(1)

# Save the merged images into a GIF named "costumes.gif". The duration of each frame is 200 milliseconds, and the GIF repeats infinitely.
images[0].save(
    "costumes.gif",
    save_all = True,
    append_images=images[1:],
    duration = 200,
    loop =0,
)