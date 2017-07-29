def all_prefixes(st):
	import string
	if not type(st) == str:
		return None
	for i in st:
		if i not in string.ascii_letters:
			return None
	end = []
	ls = []
	s = ''
	var = st[0]
	for i in st:
		if i == var:
			for k in range(st.index(i), len(st)):
				s += st[k]
				ls.append(s)
			st = st[st.index(i) + 1:]
			end.append(set(ls))
			ls = []
			s = ''
	return end
