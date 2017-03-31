from lib.texttransform import TextTransform
from lib.imagehandler import ImageHandler
import sys, argparse

print("Image encoder - Reedphish Heavy Industries 2017")

parser = argparse.ArgumentParser(description="Encode image with secret text")
parser.add_argument("cleartextpath", metavar="ctp", type=str, help="Path to clear text file to be inserted into image")
parser.add_argument("baseimagepath", metavar="bip", type=str, help="Path to base image to work on")
parser.add_argument("newimagepath", metavar="nip", type=str, help="Path to output image")

args = parser.parse_args()

try:
	encoded_text = TextTransform.encode(open(args.cleartextpath, "r").read())
	encoding_key = ImageHandler.encode(args.baseimagepath, args.newimagepath, encoded_text)

	print("\nImage {0} encoded with key {1}\n".format(args.newimagepath, encoding_key))
except Exception as e:
	print("[ERROR] Unable to encode image: {0}".format(e))