def string_compression(string):
	char_count = 0
	compressed_string = string[0]
	for char in string:
		if char in compressed_string:
			char_count += 1
		else:
			compressed_string = compressed_string + str(char_count)
			char_count = 1
			compressed_string = compressed_string + char

	compressed_string = compressed_string + str(char_count)

	if len(compressed_string) >= len(string):
		return string
	else:
		return compressed_string



if __name__ == '__main__':
	print(string_compression("aabbccc"))



