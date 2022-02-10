from csv import writer

with open('anu.csv', 'w', newline='') as file:
	csv_writer = writer(file)
	csv_writer.writerow(["name","Age"])
	csv_writer.writerow(["Anushka",19])
	csv_writer.writerow(["Suarabh",19])