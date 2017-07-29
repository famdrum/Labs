def line_intersect(ls):
	if (ls[0] or ls[1]) == []:
		return None
	if ls[0] == ls[1]:
		return ls[0]
	x1_1, y1_1 = ls[0][0]
	x1_2, y1_2 = ls[0][1]
	x2_1, y2_1 = ls[1][0]
	x2_2, y2_2 = ls[1][1]
	if not type(x1_1) == type(x1_2) == type(x2_1) == type(x2_2) == float:
		return None
	if not type(y1_1) == type(y1_2) == type(y2_1) == type(y2_2) == float:
		return None
	A1 = y1_1 - y1_2
	B1 = x1_2 - x1_1
	C1 = x1_1*y1_2 - x1_2*y1_1
	A2 = y2_1 - y2_2
	B2 = x2_2 - x2_1
	C2 = x2_1*y2_2 - x2_2*y2_1
	if B1*A2 - B2*A1 != 0:
		y = (C2*A1 - C1*A2) / (B1*A2 - B2*A1)
		x = (-C1 - B1*y) / A1
		if min(x1_1, x1_2) <= x <= max(x1_1, x1_2) and min(y1_1, y1_2) <= y <= max(y1_1, y1_2):
			return (x, y)
		else:
			return None
	if B1*A2 - B2*A1 == 0: return '||'
