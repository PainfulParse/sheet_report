import pygal
from pygal.style import CleanStyle
import reader
from flask import Flask, Response , render_template, request, send_file
from datetime import date, timedelta, datetime

app = Flask(__name__ , static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

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
	begin       = datetime.strptime(beginStr, dateFormat)
	end         = datetime.strptime(endStr, dateFormat)
	delta       = end - begin
	
	#Loop thru days and add them to days list
	for i in range(delta.days + 1):
		days.append(str(begin + timedelta(days=i))[5:10].replace('-', '/'))

	#Setup style, labels on x axis and the title of the chart
	line_chart = pygal.Line(style=CleanStyle)
	line_chart.x_labels = days
	line_chart.title = days[0] + ' - ' + days[-1] + ' Plant 1 Daily Sheet Utilization by Machine'

	#Loop thru machines list and assign correct day and machine to be plotted on chart
	for i in machines:
		data = reader.readData(i)
		for key in data:
			if key[0:5] in days:
				if i == 'v1':
					v1.append(data[key])
					print(data[key])
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
	line_chart.add('Vipros 1', v1)
	line_chart.add('Vipros 2', v2)
	line_chart.add('Vipros 3', v3)
	line_chart.add('Vipros 5', v5)
	line_chart.add('Salvagnini', l1)
	line_chart.add('Pulsar', p1)

	reader.cleanUp()
	days = None
	v1   = None
	v2   = None
	v3   = None
	v5   = None
	l1   = None
	p1   = None

	print('Rendering File')
	chart = line_chart.render(is_unicode=True)
	line_chart.render_to_file('chart.svg')

	return chart

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run('localhost',5000)

