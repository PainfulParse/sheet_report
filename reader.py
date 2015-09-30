import csv
import chart
from datetime import datetime

class Machine:

	def __init__(self, name):
		self.name            = name
		self.date_storage    = {}
		self.divisor_storage = {}

	def store_date(self, date, yld):
		#print yld
		if date == '09/10/2015' and self.name == 'Salvagnini laser' and self.date_storage.get(date):
				print('Adding Yield %f to %f' % (yld, self.date_storage[date]))
				#print self.divisor_storage[date]

		if self.date_storage.get(date):
			self.date_storage[date]    = self.date_storage[date] + yld
			self.divisor_storage[date] = self.divisor_storage[date] + 1
		else:
			self.date_storage[date]    = yld
			self.divisor_storage[date] = 1

	def readData(self):
		for key in sorted(self.date_storage):
			print('V1 Average Percentage for %s is %f' % (key, self.date_storage[key]))

	def avgPercentage(self):
		for i in sorted(self.date_storage):
			#print('Divisor for %s is %s' % (self.date_storage[i], self.divisor_storage[i]))
			self.date_storage[i] = round(100 * ((self.date_storage[i] / 2) / self.divisor_storage[i]), 1)

v1 = Machine('Amada Vipros 1 - Cell #1')
v2 = Machine('Amada Vipros 2 - Cell #1')
v3 = Machine('Amada Vipros 3 - Cell #2')
v5 = Machine('Amada Vipros 5 - Cell #3')
l1 = Machine('Salvagnini laser')
p1 = Machine('Amada Pulsar Laser  - Cell #1')

def readFile():
	global v1,v2,v3,v5,l1,p1

	with open('data.txt') as csvfile:
		reader = csv.DictReader(csvfile)
		#Iterate thru csv file by each row
		for row in reader:
			when    = row['Date Completed']
			machine = row['Work Center']
			rectYld = float(row['Requested Rect. Yield'])

			if rectYld >= 100.00:
				rectYld = 1.00
			else:
				rectYld = rectYld / 100.00

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
					if v1.date_storage.get(when):
						v1.date_storage[when] =  v1.date_storage[when] + rectYld
						v1.store_date(when, rectYld)
					else:
						v1.store_date(when, rectYld)
				elif machine == v2.name:
					if v2.date_storage.get(when):
						v2.date_storage[when] =  v2.date_storage[when] + rectYld
						v2.store_date(when, rectYld)
					else:
						v2.store_date(when, rectYld)
				elif machine == v3.name:
					if v3.date_storage.get(when):
						v3.date_storage[when] =  v3.date_storage[when] + rectYld
						v3.store_date(when, rectYld)
					else:
						v3.store_date(when, rectYld)
				elif machine == v5.name:
					if v5.date_storage.get(when):
						v5.date_storage[when] =  v5.date_storage[when] + rectYld
						v5.store_date(when, rectYld)
					else:
						v5.store_date(when, rectYld)
				elif machine == l1.name:
					if l1.date_storage.get(when):
						l1.date_storage[when] =  l1.date_storage[when] + rectYld
						l1.store_date(when, rectYld)
					else:
						l1.store_date(when, rectYld)
				elif machine == p1.name:
					if p1.date_storage.get(when):
						p1.date_storage[when] =  p1.date_storage[when] + rectYld
						p1.store_date(when, rectYld)
					else:
						p1.store_date(when, rectYld)

#Check the date to see if it is a production day (Monday - Friday)
def dateCheck(d):
	d = datetime.strptime(d, '%m/%d/%Y').date()
	i = 1

	while i < 12:	
		if d.month == i:
			if d.isoweekday() in range(1, 6):
				return True
			else:
				return False
		i += 1

readFile()

v1.avgPercentage()
v2.avgPercentage()
v3.avgPercentage()
v5.avgPercentage()
l1.avgPercentage()
p1.avgPercentage()

chart.addLine(v1.date_storage, v1.name[6:14])
chart.addLine(v2.date_storage, v2.name[6:14])
chart.addLine(v3.date_storage, v3.name[6:14])
chart.addLine(v5.date_storage, v5.name[6:14])
chart.addLine(l1.date_storage, l1.name[0:10])
chart.addLine(p1.date_storage, p1.name[6:12])
chart.render()


