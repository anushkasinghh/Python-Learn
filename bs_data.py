from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" class='special'>
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
attr = soup.find("div")["id"]
print(attr)
# for el in soup.select(".special"):
# 	print(el)
# 	print(el.get_text())
# 	print(el.name)
# 	print(el.attrs)
	