from lib.texttransform import TextTransform
from lib.imagehandler import ImageHandler
import sys

clear_text_file = sys.argv[1]
base_image_path = sys.argv[2]
new_image_path = sys.argv[3]

print("Image encoder - Reedphish Heavy Industries 2017")

try:
	encoded_text = TextTransform.encode(open(clear_text_file, "r").read())
	encoding_key = ImageHandler.encode(base_image_path, new_image_path, encoded_text)

	print("\nImage {0} encoded with key {1}\n".format(new_image_path, encoding_key))
except Exception as e:
	print("[ERROR] Unable to encode image: {0}".format(e))