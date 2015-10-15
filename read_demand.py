import csv

shim        = 'F700153'
allOps      = 'All Operations Completed'

def readFile(date,report):
	required  = 0
	completed = 0
	msg       = ''

	if report == 'Non Paint':
		msg = 'Total Remaining Non-Paint Parts: '
	elif report == 'Paint':
		msg = 'Total Remaining Paint Parts: '
	else:
		print ('Error - report is %s' % report)

	with open('all_demand.txt', 'rU') as csvfile:
		reader = csv.DictReader(csvfile)
		#Iterate thru csv file by each row
		for row in reader:
			prod_bucket    = row['Production Bucket']
			quan_complete  = row['Quantity Completed']
			required_quan  = row['Required Quantity']
			completed_thru = row['Quantity Completed Thru']
			item_number    = row['Item Number']
			due_date       = row['Due Date']

			#Bypass Non Fab Buckets
			if (prod_bucket == 'Ends Dept' or
				prod_bucket == 'Ends Dept Paint' or 
				prod_bucket == 'Radius Bucket' or
				prod_bucket == 'Kan - Ban' or
				prod_bucket == 'Urgent Parts' or
				prod_bucket == 'Welding' or
				prod_bucket == 'Welding Paint' or
				prod_bucket == 'Shelf Spotweld' or
				prod_bucket == 'Non-Shelf Spotweld' or
				prod_bucket == 'Foam Dept' or
				prod_bucket == 'DC' or
				prod_bucket == 'DC Paint' or
				prod_bucket == 'Pegboards Paint' or
				prod_bucket == 'Pegboards' or
				prod_bucket == 'TNK Bucket' or
				prod_bucket == 'Fab for Engineering' or
				prod_bucket == 'Electrical Cell' or
				prod_bucket == 'Filler Punch'):
				continue

			#Check if parts are pending and the part is not a shim
			if completed_thru != allOps and item_number[0:7] != shim:
				if due_date == date:
					if 'Paint' in prod_bucket and report == 'Paint':
						required  += int(required_quan)
						completed += int(quan_complete)
					elif not 'Paint' in prod_bucket and report == 'Non Paint':
						required  += int(required_quan)
						completed += int(quan_complete)

	return (msg + '%i' % (required - completed))


