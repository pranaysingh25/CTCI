def URLify(string):
	modified_string = ""
	for char_index in range(len(string)):
		if string[char_index] == " ":
			modified_string = modified_string + "%20"
		elif string[char_index] == "	":
			modified_string = modified_string + ("%20")*4
		else:
			modified_string = modified_string + string[char_index]

	return modified_string

if __name__ == '__main__':
	print(URLify("hey there,	This is Pranay!"))
