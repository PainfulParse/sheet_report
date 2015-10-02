import csv
import chart
from datetime import datetime

class Machine:
	def __init__(self, name):
		self.name            = name
		self.dates           = {}
		self.divisors        = {}

	#Add Date to Dict for storage
	def addDate(self, date, yld):
		if self.dates.get(date):
			self.dates[date]    += yld
			self.divisors[date] += 1
		else:
			self.dates[date]    = yld
			self.divisors[date] = 1

	#Average Percentage of data supplied
	def avgPercentage(self):
		for i in sorted(self.dates):
			self.dates[i] = round(100 * (self.dates[i] / self.divisors[i]), 1)

v1 = Machine('Amada Vipros 1 - Cell #1')
v2 = Machine('Amada Vipros 2 - Cell #1')
v3 = Machine('Amada Vipros 3 - Cell #2')
v5 = Machine('Amada Vipros 5 - Cell #3')
l1 = Machine('Salvagnini laser')
p1 = Machine('Amada Pulsar Laser  - Cell #1')

def readFile():
	global v1,v2,v3,v5,l1,p1

	with open('data.TXT') as csvfile:
		reader = csv.DictReader(csvfile)
		#Iterate thru csv file by each row
		for row in reader:
			when    = row['Date Completed']
			machine = row['Work Center']
			rectYld = float(row['Requested Rect. Yield']) / 100

			#Check if production day and format to mm/dd/YYYY format
			if dateCheck(when):
				#Convert to DD format
				if when[3:4] == '/':
					when = when[:2] + '0' + when[2:] 
				#Convert to MM format
				if when[1:2] == '/':
					when = when[:0] + '0' + when[0:]

				#Add data to machine object for storage
				if machine == v1.name:
						v1.addDate(when, rectYld)
				elif machine == v2.name:
						v2.addDate(when, rectYld)
				elif machine == v3.name:
						v3.addDate(when, rectYld)
				elif machine == v5.name:
						v5.addDate(when, rectYld)
				elif machine == l1.name:
						l1.addDate(when, rectYld)
				elif machine == p1.name:
						p1.addDate(when, rectYld)
		reader = None


#Check the date to see if it is a production day (Monday - Friday)
def dateCheck(d):
	'''d = datetime.strptime(d, '%m/%d/%Y').date()
	i = 1

	while i < 12:	
		if d.month == i:
			if d.isoweekday() in range(1, 6):
				return True
			else:
				return False
		i += 1'''

	return True

def readData(mach):
	readFile()

	if mach == 'v1':
		v1.avgPercentage()
		return v1.dates
	elif mach == 'v2':
		v2.avgPercentage()
		return v2.dates
	elif mach == 'v3':
		v3.avgPercentage()
		return v3.dates
	elif mach == 'v5':
		v5.avgPercentage()
		return v5.dates
	elif mach == 'l1':
		l1.avgPercentage()
		return l1.dates
	elif mach == 'p1':
		p1.avgPercentage()
		return p1.dates
	else:
		print 'No Machine Name was passed to Reader'

#Erase references to global variables for garbage collection
def cleanUp():
	v1.dates    = {}
	v2.dates    = {}
	v3.dates    = {}
	v5.dates    = {}
	l1.dates    = {}
	p1.dates    = {}
	v1.divisors = {}
	v2.divisors = {}
	v3.divisors = {}
	v5.divisors = {}
	l1.divisors = {}
	p1.divisors = {}