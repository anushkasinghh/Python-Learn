from csv import writer, reader, DictWriter,DictReader

with open("marksheet.csv", "a", newline="") as file:
	csv_writer = writer(file)
	# csv_writer.writerow(["Subject", "Marks"])
	csv_writer.writerow(["Physics", 90])
	csv_writer.writerow(["Chemistry", 94])
	csv_writer.writerow(["Maths", 95])
	csv_writer.writerow(["English", 86])

# with open("marksheet.csv") as file:
# 	csv_reader = reader(file)
# 	print(list(csv_reader))

# with open("marksheet.csv", "r+", newline="") as file:
# 	csv_writer = DictWriter(file, fieldnames=["Subject", "Marks"])
# 	csv_writer.writeheader()
# 	csv_writer.writerow({"Subject": "P.Ed", "Marks": 86})
	# file.truncate()

with open("marksheet.csv") as file:
	csv_reader = DictReader(file)
	print(list(csv_reader))