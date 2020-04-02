def write_to_file(data, file_path):
	data.to_csv(file_path, index=False, header=False)
