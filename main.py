import pygal
from pygal.style import LightSolarizedStyle
import reader
import chart
from flask import Flask, Response , render_template, request, jsonify
from datetime import date, timedelta, datetime

app = Flask(__name__ , static_url_path='')

@app.route('/')
def index():
    """ render svg figures on html """
    return render_template('index.html')

@app.route('/chart/')
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
	beginStr    = request.args.get('begin', 0, type=str)
	endStr      = request.args.get('end', 0, type=str)
	begin       = datetime.strptime(beginStr, dateFormat)
	end         = datetime.strptime(endStr, dateFormat)
	delta       = end - begin
	
	#Loop thru days and add them to days list
	for i in range(delta.days + 1):
		days.append(str(begin + timedelta(days=i))[5:10].replace('-', '/'))

	line_chart = pygal.Bar(style=LightSolarizedStyle)
	line_chart.x_labels = (days[0], days[1], days[2], days[3], days[4])
	line_chart.title = days[0] + ' - ' + days[-2] + ' Plant 1 Daily Sheet Utilization by Machine'

	for i in machines:
		data = reader.readData(i)
		for key in data:
			if key[0:5] == days[0] or key[0:5] == days[1] or key[0:5] == days[2] or key[0:5] == days[3] or key[0:5] == days[4]:
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

	line_chart.add('Vipros 1', v1)
	line_chart.add('Vipros 2', v2)
	line_chart.add('Vipros 3', v3)
	line_chart.add('Vipros 5', v5)
	line_chart.add('Salvagnini', l1)
	line_chart.add('Pulsar', p1)

	return Response(response=line_chart.render(), content_type='image/svg+xml')

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run('localhost',5000)

