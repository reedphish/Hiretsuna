class TextTransform:
	""" Utility class for encoding and decoding text """
	chunk_size = 3

	@staticmethod
	def encode(clear_text):
		""" Encode text into its Ordinal representation. """
		words_list = list(clear_text)
		chunk_list = [words_list[i:i+TextTransform.chunk_size] for i in range(0,len(words_list),TextTransform.chunk_size)]

		for chunk_index, chunk in enumerate(chunk_list):
			# Pad chunk if length < TextTransform.chunk_size
			if len(chunk) < TextTransform.chunk_size:
				for index in range(0, TextTransform.chunk_size-len(chunk)):
					chunk.append(None)

			# Encode chunk
			encoded = []
			for character_index, character in enumerate(chunk):
				if character == None:
					encoded.append(0)
				else:
					encoded.append(ord(character))

			if len(encoded) == 3:
				encoded.append(0)

			chunk_list[chunk_index] = tuple(encoded)

		return chunk_list

	@staticmethod
	def decode(encoded_text):
		""" Decode text from Ordinal structure to string """
		decoded_list = []

		for chunk in encoded_text:
			for ordinal in chunk:
				if ordinal != 0:
					decoded_list.append(chr(ordinal))

		return "".join(decoded_list)