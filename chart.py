import pygal

line_chart = pygal.HorizontalBar()
line_chart.title = 'September Pulsar 1 Daily Utilization'


def addLine(data):
	line_chart.add(date, data)

def render():
	line_chart.render_to_file('bar.svg')