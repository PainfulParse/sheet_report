import pygal

line_chart = pygal.HorizontalBar(range=(0,100))

def addLine(data, machine):
	line_chart.title = '9/10/2015 Plant 1 Average Sheet Utilization'

	for key in data:
		if key[0:5] == '09/10':
			line_chart.add(machine, data[key])

def render(filename):
	line_chart.render_to_file(filename + '_bar.svg')
