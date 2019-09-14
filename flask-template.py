import os, sys

app_data = "from flask import Flask, request, redirect, render_template, url_for\n" \
	"import os, sys\n" \
	"\n" \
	"app = Flask(__name__)\n" \
	"\n" \
	"@app.route('/')\n" \
	"def main():\n" \
	"	return render_template('main.html')\n" \
	"\n" \
	"if __name__ == '__main__':\n" \
	"	app.run(port=80)\n" 

css_data = "/* elements */\n" \
	"\n" \
	"/* /elements */\n" \
	"/* header */\n" \
	"\n" \
	"/* /header */\n" \
	"/* site */\n" \
	"\n" \
	"/* /site */\n" \
	"/* footer */\n" \
	"\n" \
	"/* /footer */\n" \

html_data = "<!DOCTYPE html>\n" \
	"<html>\n" \
	"<head>\n" \
	"	<title>My site</title>\n" \
	"	<link rel=\"stylesheet\" type=\"text/css\" href=\"{{ url_for('static', filename='css/global.css') }}\">\n" \
	"</head>\n" \
	"<body>\n" \
	"	Body content\n" \
	"</body>\n" \
	"</html>\n" \


# creating main folders for stable working 
os.mkdir('templates')
os.mkdir('static')
os.mkdir('static/css')

with open('app.py', 'w') as app:
	app.writelines(app_data)
with open('static/css/global.css', 'w') as css:
	css.writelines(css_data)
with open('templates/main.html', 'w') as html:
	html.writelines(html_data)