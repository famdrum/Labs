def is_sorted(ls):
	if not type(ls) == list:
		return None
	for i in ls:
		if not type(i) == int:
			return None
	for i in range(len(ls)):
		if i == 0:
			pass
		else:
			if not (ls[i] >= ls[i - 1]):
				return False
	return True

