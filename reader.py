import csv
import chart
from datetime import datetime

class Machine:

	def __init__(self, name):
		self.name = name
		self.total = 0
		self.date_storage = {}

	def increment(self, quantity):
		self.total += quantity

	def store_date(self, date, amount):
		self.date_storage[date] = amount

	def readData(self):
		for key in self.date_storage:
			i = 0

	def mergeDups(self):
		for key in self.date_storage:
			print self.name + ' - ' + key



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
			divisor = 0
			when    = row['Date Completed']
			machine = row['Work Center']
			rectYld = float(row['Requested Rect. Yield'])

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
					divisor += 1
					v1.store_date(
						when,
						rectYld
					)
				elif machine == v2.name:
					divisor += 1
					v2.store_date(
						when,
						rectYld
					)
				elif machine == v3.name:
					divisor += 1
					v3.store_date(
						when,
						rectYld
					)
				elif machine == v5.name:
					divisor += 1
					v5.store_date(
						when,
						rectYld
					)
				elif machine == l1.name:
					divisor += 1
					l1.store_date(
						when,
						rectYld
					)
				elif machine == p1.name:
					divisor += 1
					p1.store_date(
						when,
						rectYld
					)

		#print('%s Daily Average Percent: %f' % (p1.name, round(p1.total/divCounter,1)))


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
v1.mergeDups()
v2.mergeDups()
v3.mergeDups()
v5.mergeDups()
l1.mergeDups()
p1.mergeDups()

