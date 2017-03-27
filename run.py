from lib.texttransform import TextTransform
from lib.imagehandler import ImageHandler

"""
Utility script for creating malware PNG's. Remember to pip install the following:
* pypng
"""

clear_file = open("example_texts/Short_poem.txt", "r")
clear_text = clear_file.read()
clear_file.close()

encoded_text = TextTransform.encode(clear_text)
decoded_text = TextTransform.decode(encoded_text)

if clear_text == decoded_text:
	print("\nEncode decode successfully")
else:
	print("\nEncode decode: FAILED")

original_image = "base_images/psychedelic-4.png"
encoded_image = "example_images/psychedelic-4.png"

length = ImageHandler.encodeImage(original_image, encoded_image, encoded_text)
decoded_text = ImageHandler.decodeImage(encoded_image, length)

print("Decoded text from image:\n{0}".format(decoded_text))
