import pygal
import reader
import chart
from flask import Flask, Response , render_template

app = Flask(__name__ , static_url_path='')

@app.route('/')
def index():
    """ render svg figures on html """
    return render_template('index.html')

@app.route('/linechart/')
def avgChart():
	i = 0
	line_chart = pygal.HorizontalBar(range=(0,100))
	line_chart.title = '9/10/2015 Plant 1 Average Sheet Utilization'

	machines = [
		'Vipros 1',
		'Vipros 2', 
		'Vipros 3',
		'Vipros 5',
		'Salvagnini',
		'Pulsar 1'
	]

	for i in machines:
		data = reader.readData(i)
		print data
		for key in data:
			if key[0:5] == '09/10':
				line_chart.add(i, data[key])

	return Response(response=line_chart.render(), content_type='image/svg+xml')

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run('localhost',5000)

