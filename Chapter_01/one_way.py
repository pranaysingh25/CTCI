def one_way(string1, string2):
	# if one element is less or extra 
	if abs(len(string1) - len(string2)) == 1:
		if (set(string1).intersection(set(string2)).issubset(set(string1))) or (set(string1).intersection(set(string2)).issubset(set(string2))):
			return True

	# if length is same
	if len(string1) == len(string2):
		if len(set(string1) - set(string2)) == 1:
			return True

	# not atleast one way away
	return False


if __name__ == '__main__':
	print(one_way("pale", "bale"))