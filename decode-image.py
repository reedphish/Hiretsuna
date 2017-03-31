from lib.texttransform import TextTransform
from lib.imagehandler import ImageHandler
import sys, argparse

print("Image decoder - Reedphish Heavy Industries 2017")

parser = argparse.ArgumentParser(description="Encode image with secret text")
parser.add_argument("outputfilepath", metavar="ofp", type=str, help="Path where to write extracted content")
parser.add_argument("encodedimagepath", metavar="eip", type=str, help="Path image to decode")
parser.add_argument("key", metavar="key", type=int, help="Key to decode")

args = parser.parse_args()

decoded_text = ImageHandler.decode(args.encodedimagepath, args.key)
file = open(args.outputfilepath, "w")
file.write(decoded_text)
file.close()

print("\nImage {0} decoded using key {1}. Written to {2}\n".format(args.encodedimagepath, args.key, args.outputfilepath))
