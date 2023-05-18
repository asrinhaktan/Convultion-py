from PIL import Image
import numpy as np

image = Image.open("/Users/asrinhaktansahin/Downloads/1.OdevBalon-2.png")
image = image.convert("L")
image_array = np.array(image)

maske = np.array([[1, 1, 1],
                 [1, 0, 1],
                 [1, 1, 1]])

maske = maske.reshape(3, 3, 1)

output_array = np.zeros_like(image_array)

for i in range(1, image_array.shape[0]-1):
    for j in range(1, image_array.shape[1]-1):
        pixel_region = image_array[i-1:i+2, j-1:j+2]
        konvulsiyon_pixel = np.sum(maske * pixel_region.reshape(3,3,1))
        output_array[i, j] = konvulsiyon_pixel
        
output_image = Image.fromarray(output_array.astype(np.uint8))
output_image.save("/Users/asrinhaktansahin/Downloads/ornek_konvulsiyon.png")
