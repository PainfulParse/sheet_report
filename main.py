import pygal
from pygal.style import CleanStyle
import reader
from flask import Flask, Response , render_template, request
from datetime import date, timedelta, datetime

app = Flask(__name__ , static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/line/')
def serve():
	user_chart = pygal.Line()
	user_chart.title = 'Browser usage evolution (in %)'
	user_chart.x_labels = map(str, range(2002, 2013))
	user_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
	user_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
	user_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
	user_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
	return Response(response=user_chart.render(), content_type='image/svg+xml')

@app.route('/user_chart/')
def display():
	return """
	<html>
    	<body>
        	<h1>hello pygal</h1>
        	<figure>
        		<embed type="image/svg+xml" src="/line/" />
        	</figure>
    	</body>
	</html>'
	"""

@app.route('/chart/', methods=['POST'])
def avgChart():
	days        = []
	v1          = []
	v2          = []
	v3          = []
	v5          = []
	l1          = []
	p1          = []
	machines    = ['v1','v2', 'v3','v5','l1','p1']
	dateFormat  = '%Y-%m-%d'
	beginStr    = request.form.get('begin', type=str)
	endStr      = request.form.get('end', type=str)
	freq   = request.form.get('freq', type=str)
	begin       = datetime.strptime(beginStr, dateFormat)
	end         = datetime.strptime(endStr, dateFormat)
	delta       = end - begin
	
	#Loop thru days and add them to days list
	for i in range(delta.days + 1):
		days.append(str(begin + timedelta(days=i))[5:10].replace('-', '/'))

	if freq == 'Daily':
		user_chart = pygal.Bar(style=CleanStyle)
	elif freq == 'Weekly':
		user_chart = pygal.Line(style=CleanStyle)
	elif freq == 'Monthly':
		user_chart = pygal.StackedLine(fill=True)

	#Setup style, labels on x axis and the title of the chart
	#user_chart = pygal.Line(style=CleanStyle)
	user_chart.x_labels = days
	user_chart.title = days[0] + ' - ' + days[-1] + ' Plant 1 Daily Sheet Utilization by Machine'

	#Loop thru machines list and assign correct day and machine to be plotted on chart
	for i in machines:
		data = reader.readData(i)
		for key in data:
			if key[0:5] in days:
				if i == 'v1':
					v1.append(data[key])
				elif i == 'v2':
					v2.append(data[key])
				elif i == 'v3':
					v3.append(data[key])
				elif i == 'v5':
					v5.append(data[key])
				elif i == 'l1':
					l1.append(data[key])
				elif i == 'p1':
					p1.append(data[key])

	#Add data to chart by machine
	user_chart.add('Vipros 1', v1)
	user_chart.add('Vipros 2', v2)
	user_chart.add('Vipros 3', v3)
	user_chart.add('Vipros 5', v5)
	user_chart.add('Salvagnini', l1)
	user_chart.add('Pulsar', p1)

	reader.cleanUp()
	days = None
	v1   = None
	v2   = None
	v3   = None
	v5   = None
	l1   = None
	p1   = None

	chart = user_chart.render(is_unicode=True)
	chart_file = user_chart.render_to_file('chart.svg')
	return chart

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run('localhost',5000)

