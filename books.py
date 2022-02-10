import re
titles = [
	"Significant Others (1987)",
	"Tales of the City (1978)",
	"The Days of Anna Madrigal (2014)",
	"Mary Anne in Autumn (2010)",
	"Further tales of the city (1980)",
	"Babycakes (1984)",
	"More tales of the City (1980)",
	"Sure of You (1980)",
	"Michael Tolliver Lives (2007)"]

pattern = re.compile(r'(?P<book_name>^[\w ]+) \((?P<year>\d{4})\)')

sorted_books = []
for book in titles:
	# match = pattern.search(book)
	# sorted_books.append(f"{match.group('year')} - {match.group('book_name')}") 
	# sorted_books.append(pattern.sub("\g<2> - \g<1>", book))
	sorted_books.append(pattern.sub("\g<year> - \g<book_name>", book))

print(sorted_books)