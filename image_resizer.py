import os
from PIL import Image

# Set input and output folder paths
input_folder = "images"              # folder with original images
output_folder = "resized_images"     # folder to save resized images
new_size = (800, 800)                # desired size

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Resize image
        img = img.resize(new_size)

        # Save resized image to output folder (can change format if needed)
        output_path = os.path.join(output_folder, filename)
        img.save(output_path)

print(" All images resized and saved in:", output_folder)
