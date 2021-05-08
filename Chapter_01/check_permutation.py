def check_permutation(string1, string2):
	if len(string1) == len(string2):
		if string1 == string2:
			return False
	if len(string1) < len(string2):
		for i in range(0, len(string2)-(len(string1)+1)):
			if string2[i: i+len(string1)] == string1:
				return True

		return False

	return check_permutation(string2, string1)


if __name__ == '__main__':
	print(check_permutation("abc", "xyxyxyxyxabcxyxyxyxyxy"))

