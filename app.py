# to open/create a new html file in the write mode
f = open('app/udacity.html', encoding="utf-8")

# the html code which will go in the file GFG.html
html_template = """<html>
<head>
<title>Udacity Capstone</title>
</head>
<body>
<h2>Thanks Udacity Team</h2>
  
<p>This is a capstone project.</p>
  
</body>
</html>
"""

# writing the code into the file
f.write(html_template)

# close the file
f.close()