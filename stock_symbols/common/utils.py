def invert_dict(dic):
	return dict((val, key) for key in dic for val in dic[key])
