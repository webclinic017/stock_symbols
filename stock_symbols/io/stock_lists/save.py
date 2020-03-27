def write_stock_list_to_file(stock_list_data, file_path):
	stock_list_data.to_csv(file_path, index=False, header=False)
