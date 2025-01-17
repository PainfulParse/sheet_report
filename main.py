import pygal
import json
from pygal.style import CleanStyle, LightColorizedStyle
import reader
import read_demand
from flask import Flask, Response , render_template, request
from datetime import date, timedelta, datetime

app = Flask(__name__ , static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
	return render_template('about.html')

@app.route('/forms/')
def forms():
	return render_template('forms.html')

@app.route('/reports/')
def reports():
	return render_template('reports.html')

@app.route('/reports/paint/', methods=['POST'])
def paint_report():
	dateStr = request.form.get('date', type=str)
	report  = request.form.get('report', type=str)
	date    = datetime.strptime(dateStr, '%Y-%m-%d').strftime('%m/%d/%Y')

	return read_demand.readFile(date, report)

@app.route('/reports/non_paint/', methods=['POST'])
def non_paint_report():
	dateStr = request.form.get('date', type=str)
	report  = request.form.get('report', type=str)
	date    = datetime.strptime(dateStr, '%Y-%m-%d').strftime('%m/%d/%Y')

	return read_demand.readFile(date, report)

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

@app.route('/charts/')
def display():
	return render_template('charts.html')

@app.route('/build/', methods=['POST'])
def avgChart():
	days        = []
	v1          = []
	v2          = []
	v3          = []
	v5          = []
	l1          = []
	p1          = []
	t1          = []
	t2          = []
	sg1         = []
	sg2         = []
	sg3         = []
	sg4         = []
	sg5         = []
	dateFormat  = '%Y-%m-%d'
	beginStr    = request.form.get('begin', type=str)
	endStr      = request.form.get('end', type=str)
	chartType   = request.form.get('chartType', type=str)
	machines    = request.form.get('mach', type=str)
	mach        = json.loads(machines)
	begin       = datetime.strptime(beginStr, dateFormat)
	end         = datetime.strptime(endStr, dateFormat)
	delta       = end - begin

	#Loop thru days and add them to days list
	for i in range(delta.days + 1):
		if i != 0:
			days.append(str(begin + timedelta(days=i))[5:10].replace('-', '/'))

	#Setup style of chart
	if chartType == 'Bar':
		user_chart = pygal.Bar(style=LightColorizedStyle)
	elif chartType == 'Line':
		user_chart = pygal.Line(style=CleanStyle)
	elif chartType == 'Stacked':
		user_chart = pygal.StackedLine(fill=True)

	#Setup labels on x axis and the title of the chart
	user_chart.x_labels = days
	user_chart.title = days[0] + ' - ' + days[-1] + ' Plant 1 Daily Sheet Utilization by Machine'

	#Loop thru machines list and assign correct day and machine to be plotted on chart
	for i in mach:
		#Add data to chart by machine
		if i == 'v1':
			user_chart.add('Vipros 1', v1)
		elif i == 'v2':
			user_chart.add('Vipros 2', v2)
		elif i == 'v3':
			user_chart.add('Vipros 3', v3)
		elif i == 'v5':
			user_chart.add('Vipros 5', v5)
		elif i == 'l1':
			user_chart.add('Salvagnini', l1)
		elif i == 'p1':
			user_chart.add('Pulsar', p1)
		elif i == 't1':
			user_chart.add('FMS 1', t1)
		elif i == 't2':
			user_chart.add('FMS 2', t2)
		elif i == 'sg1':
			user_chart.add('SG 1', sg1)
		elif i == 'sg2':
			user_chart.add('SG 2', sg2)
		elif i == 'sg3':
			user_chart.add('SG 3', sg3)
		elif i == 'sg4':
			user_chart.add('SG 4', sg4)
		elif i == 'sg5':
			user_chart.add('SG 5', sg5)

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
				elif i == 't1':
					t1.append(data[key])
				elif i == 't2':
					t2.append(data[key])
				elif i == 'sg1':
					sg1.append(data[key])
				elif i == 'sg2':
					sg2.append(data[key])
				elif i == 'sg3':
					sg3.append(data[key])
				elif i == 'sg4':
					sg4.append(data[key])
				elif i == 'sg5':
					sg5.append(data[key])

	reader.cleanUp()
	days = None
	v1   = None
	v2   = None
	v3   = None
	v5   = None
	l1   = None
	p1   = None
	t1   = None
	t2   = None
	sg1  = None
	sg2  = None
	sg3  = None
	sg4  = None
	sg5  = None

	chart = user_chart.render(is_unicode=True)
	return chart

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run('localhost',5000)

