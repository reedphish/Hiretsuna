from lib.texttransform import TextTransform
from lib.imagehandler import ImageHandler
import sys

clear_text_file = sys.argv[1]
image_path = sys.argv[2]
key = sys.argv[3]

print("Image decoder - Reedphish Heavy Industries 2017")

decoded_text = ImageHandler.decode(image_path, int(key))
file = open(clear_text_file, "w")
file.write(decoded_text)
file.close()

print("\nImage {0} decoded using key {1}. Written to {2}\n".format(image_path, key, clear_text_file))
