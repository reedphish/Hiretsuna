from lib.texttransform import TextTransform
from PIL import Image
import shutil

class ImageHandler:
	@staticmethod
	def encode(image_base, image_new, encoded_text):
		""" Encode image """
		image = Image.open(image_base)
		image = image.convert("RGBA")
		pixel_map = image.load()


		height = image.height
		text_length = len(encoded_text)

		if text_length > height:
			raise "Encoded text to big to fit"
		else:
			# Insert encoded text in first "column"
			for index, rgb in enumerate(encoded_text):
				pixel_map[0, index] = rgb
			
			# Pad image height
			for pad_index in range(text_length, height):
				rgba_list = list(pixel_map[0, pad_index])
				rgba_list[-1] = 0

				pixel_map[0, pad_index] = tuple(rgba_list)

			image.save(image_new)

		return len(encoded_text)

	@staticmethod
	def decode(image_name, length):
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