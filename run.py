from lib.texttransform import TextTransform
from lib.imagehandler import ImageHandler

"""
Utility script for creating malware PNG's. Remember to pip install the following:
* pypng
"""

clear_file = open("example_texts/Long_poem.txt", "r")
clear_text = clear_file.read()
clear_file.close()

encoded_text = TextTransform.encode(clear_text)

decoded_text = TextTransform.decode(encoded_text)

print("{0}:{1}".format(encoded_text, decoded_text))

if clear_text == decoded_text:
	print("\nEncode decode successfully")
else:
	print("\nEncode decode: FAILED")

# Create image
print("\nCreating image ...")
image_name = "example_images/example.png"
ImageHandler.createImage(image_name, encoded_text)

# Decode image
text_from_image = ImageHandler.extractFromImage(image_name)

print("\nImage decoded")
print(text_from_image)