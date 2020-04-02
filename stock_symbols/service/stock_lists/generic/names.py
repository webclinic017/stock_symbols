from stock_symbols.common.utils import invert_dict


def create_stock_list_name_col(data, stock_list_map, stock_list_col=None, map_col=None):
	inverted_list_map = invert_dict(stock_list_map)
	data[stock_list_col] = data[map_col].map(inverted_list_map)
	
	return data
