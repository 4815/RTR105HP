from numpy import random

html_fails = open("htmlf.html", "w")
html_fails.write("<html>")

colors = ['#003366', '#666', 'rgb(125,200, 0)', 'rgba(0, 250, 0, 0.5)' , 'tomato', 'salmon', 'hotpink', 'olive', 'lime', 'khaki', 'saddlebrown', 'maroon', 'navy', 'gold', 'teal']


html_fails.write("<html>")
for i in range(1,11):

	a = ("<font style=\"color: " + random.choice(colors) + "\"> %d %d</font>") %(i,i*i)
	html_fails.write(a)
	html_fails.write("<br>")
html_fails.write("</html>")



html_fails.close()
