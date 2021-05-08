# using doubly nested for loop
def isunique_loop(string):
	for one_index in range(0, len(string)):
		for another_index in range(one_index+1, len(string)):
			if string[one_index] == string[another_index]:
				return False
	return True


# using python sets
def isunique_set(string):
	return len(set(string)) == len(string)



# using python dictionary
def is_unique_dict(string):
	char_count = {}
	for char in string:
		if char in char_dict:
			return False
		char_count[char] = 1
	return True
