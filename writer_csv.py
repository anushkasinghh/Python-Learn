from csv import writer

with open('file_cat.csv', 'w', newline='') as file:
	csv_writer = writer(file)
	csv_writer.writerow(['Name', 'Age'])
	csv_writer.writerow(['Blue', 3])
	csv_writer.writerow(['Kitty', 1])