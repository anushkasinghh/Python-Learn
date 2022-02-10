from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>First HTML Page</title>
</head>
<body>
	<div id="first">
		<h3 data-example="yes">hi</h3>
		<p>more text.</p>
	</div>
	<ol>
		<li class="special">This list item is speacial.</li>
		<li class="special">This list item is also speacial.</li>
		<li>This list item is  not speacial.</li>
	</ol>
	<div>bye</div>
</body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")
# 1. find an element with an id of foo
# using find:
soup.find(id='foo')
# using css
soup.select('#foo')[0]
# css always returns a list

# 2. find all elements with a class of bar
# carefull class is a reserved keyword in python
soup.find_all(class_='bar')
soup.select(".bar")

# 3. find all elements with data
# attribute of baz
# using the general attrs kwarg

soup.find_all('attrs-baz':True)
soup.select(['data-baz'])