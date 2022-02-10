from csv import DictWriter

with open("example.csv", "w", newline="") as file:
	headers = ['Name', "Breed", "Age"]
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	csv_writer.writerow({
		"Name": "Garfeild",
		"Breed": "Orange Tabby",
		"Age": 10
		})