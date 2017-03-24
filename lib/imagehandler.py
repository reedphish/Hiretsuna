from lib.texttransform import TextTransform
import png

class ImageHandler:
	""" Utility class for inserting data into image and extract it """
	@staticmethod
	def createImage(image_name, encoded_text):
		""" Create image and insert encoded text into it """
		image = open(image_name, "wb")

		w = png.Writer(1, len(encoded_text))
		w.write(image, encoded_text);
		image.close()

		return True

	@staticmethod
	def extractFromImage(image_name):
		""" Extract encoded text """
		reader = png.Reader(file=open(image_name, "rb"))
		image_data = reader.read()

		width = image_data[0]
		height = image_data[1]
		pixel_data = list(image_data[2])

		return TextTransform.decode(pixel_data)