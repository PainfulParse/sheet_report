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
		#If a date already exists then add to it
		if self.dates.get(date):
			self.dates[date]    += yld
			self.divisors[date] += 1
		#create new date if one does not exist
		else:
			self.dates[date]    = yld
			self.divisors[date] = 1

	#Average Percentage of data supplied
	def avgPercentage(self):
		for i in sorted(self.dates):
			self.dates[i] = round(100 * (self.dates[i] / self.divisors[i]), 1)

#Create Machine Objects
l1  = Machine('Salvagnini laser')
p1  = Machine('Amada Pulsar Laser  - Cell #1')
sg1 = Machine('FINNSG1')
sg2 = Machine('FINNSG2')
sg3 = Machine('FINNSG3')
sg4 = Machine('FINNSG4')
sg5 = Machine('FINNSG5')
t1  = Machine('Amada FMS #1')
t2  = Machine('Amada FMS #2')
v1  = Machine('Amada Vipros 1 - Cell #1')
v2  = Machine('Amada Vipros 2 - Cell #1')
v3  = Machine('Amada Vipros 3 - Cell #2')
v5  = Machine('Amada Vipros 5 - Cell #3')

def readFile():
	global v1,v2,v3,v5,l1,p1,t1,t2,sg1,sg2,sg3,sg4,sg5

	with open('new_data.TXT') as csvfile:
		reader = csv.DictReader(csvfile)
		#Iterate thru csv file by each row
		for row in reader:
			when    = row['Date Completed']
			machine = row['Work Center']
			rectYld = float(row['Requested Rect. Yield']) / 100

			#Convert to DD format
			if when[3:4] == '/':
				when = when[:2] + '0' + when[2:] 
			#Convert to MM format
			if when[1:2] == '/':
				when = when[:0] + '0' + when[0:]

			#Add data to machine object for storage
			if machine == l1.name:
					l1.addDate(when, rectYld)
			elif machine == p1.name:
					p1.addDate(when, rectYld)
			elif machine == sg1.name:
					sg1.addDate(when, rectYld)
			elif machine == sg2.name:
					sg2.addDate(when, rectYld)
			elif machine == sg3.name:
					sg3.addDate(when, rectYld)
			elif machine == sg4.name:
					sg4.addDate(when, rectYld)
			elif machine == sg5.name:
					sg5.addDate(when, rectYld)
			elif machine == t1.name:
					t1.addDate(when, rectYld)
			elif machine == t2.name:
					t2.addDate(when, rectYld)
			elif machine == v1.name:
					v1.addDate(when, rectYld)
			elif machine == v2.name:
					v2.addDate(when, rectYld)
			elif machine == v3.name:
					v3.addDate(when, rectYld)
			elif machine == v5.name:
					v5.addDate(when, rectYld)

		reader = None

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
	elif mach == 't1':
		t1.avgPercentage()
		return t1.dates
	elif mach == 't2':
		t2.avgPercentage()
		return t2.dates
	elif mach == 'sg1':
		sg1.avgPercentage()
		return sg1.dates
	elif mach == 'sg2':
		sg2.avgPercentage()
		return sg2.dates
	elif mach == 'sg3':
		sg3.avgPercentage()
		return sg3.dates
	elif mach == 'sg4':
		sg4.avgPercentage()
		return sg4.dates
	elif mach == 'sg5':
		sg5.avgPercentage()
		return sg5.dates
	else:
		print 'No Machine Name was passed to Reader'

#Erase references to global variables for garbage collection
def cleanUp():
	v1.dates      = {}
	v2.dates      = {}
	v3.dates      = {}
	v5.dates      = {}
	l1.dates      = {}
	p1.dates      = {}
	t1.dates      = {}
	t2.dates      = {}
	sg1.dates     = {}
	sg2.dates     = {}
	sg3.dates     = {}
	sg4.dates     = {}
	sg5.dates     = {}
	v1.divisors   = {}
	v2.divisors   = {}
	v3.divisors   = {}
	v5.divisors   = {}
	l1.divisors   = {}
	p1.divisors   = {}
	t1.divisors   = {}
	t2.divisors   = {}
	sg1.divisors  = {}
	sg2.divisors  = {}
	sg3.divisors  = {}
	sg4.divisors  = {}
	sg5.divisors  = {}