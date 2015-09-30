import pygal

line_chart = pygal.HorizontalBar()

def addLine(data, machine):
	line_chart.title = '9/10/2015 Plant 1 Average Sheet Utilization'

	for key in data:
		if key[0:5] == '09/10':
			line_chart.add(machine, data[key])

def render():
	line_chart.render_to_file('bar.svg')