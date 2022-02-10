# https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.rithmschool.com/blog"
response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article")

with open("blog_data.csv", "w", newline="") as file:
	csv_writer = writer(file)
	csv_writer.writerow(["Title", "Date", "Link"])
	for article in articles:
		title = article.find("a").get_text()
		date = article.find("small").get_text()
		href = article.find("a")["href"]
		csv_writer.writerow([title, date, href])
