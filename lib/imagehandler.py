from lib.texttransform import TextTransform
from PIL import Image
import shutil

class ImageHandler:
	@staticmethod
	def encodeImage(image_base, image_new, encoded_text):
		""" Encode image """
		image = Image.open(image_base)
		pixel_map = image.load()

		for index, rgb in enumerate(encoded_text):
			pixel_map[0, index] = rgb

		image.save(image_new)

		return len(encoded_text)

	@staticmethod
	def decodeImage(image_name, length):
		""" Decode image """
		image = Image.open(image_name)
		pixel_map = image.load()

		encoded_text = []

		for index in range(length):
			pm = pixel_map[0, index]

			if len(pm) > 3:
				pm = pm[0:3]

			encoded_text.append(pm)

		return TextTransform.decode(encoded_text)