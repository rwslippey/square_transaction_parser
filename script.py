import csv

## Variables  EDIT these to suit your needs
incomingFile = "square_example.csv" ## your file from square
outFile = "square_ready.csv" ## your outgoing file... note ALWAYS KEEP A BACKUP OF YOUR ORIGINAL FILE

## Income information
incomeDescription = "Square Income Record to post to Square Holding Account" # The description you'd like to see in your square account register for the sale
salesAccount = "Income:Photographic Service Income" # Your income account in GNUCash or other financial program Note this is layed out for GNUCash

## Transfer information
transferDescription ="Square transfer to bank account" # The decription for your square transfers to your bank
bankAccount = "Assets:Current Assets:yourbank" # Your bank account setup in GNUCash

## Square 
squareHoldingAccount = "Assets:Current Assets:Square Holding Account" # Your square holding account in GNUCash
squareExpenseAccount = "Expenses:Credit Card Processing:Square" # Your Square expense account in GNUCash
squaredescription = "Square Processing Fees" # your square processing fee description



with open(incomingFile,'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	with open(outFile, 'w', newline='') as new_file:

		fieldnames = ['Date', 'Gross Sales', 'Fees', 'Net Total', 'Description', 'Transfer Account']


		csv_writer = csv.writer(new_file)

		csv_writer.writerow(["Date", "Gross Sales", "Fees", "Net Total", "Description", "Account"])

		for row in csv_reader:
			csv_writer.writerow([row['Date'], row['Gross Sales'], '', '', incomeDescription, salesAccount])
			csv_writer.writerow([row['Date'], '', '', row['Net Total'], transferDescription, bankAccount])
			csv_writer.writerow([row['Date'], '', row['Fees'],'', squaredescription, squareExpenseAccount])






		# csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

		# csv_writer.writeheader()

		# for line in newdata:
		# 	writefeilds = ['Date', 'Gross Sales', 'Fees', 'Net Total']
		# # 	del line['Time']
		# # 	del line['Time Zone']
		# # 	del line['Discounts']
		# # 	del line['Net Sales']
		# # 	del line['Gift Card Sales']
		# # 	del line['Tax']
		# # 	del line['Tip']
		# # 	del line['Partial Refunds']
		# # 	del line['Total Collected']
		# # 	del line['Source']
		# # 	del line['Card']
		# # 	del line['Card Entry Methods']
		# # 	del line['Cash']
		# # 	del line['Square Gift Card']
		# # 	del line['Installment']
		# # 	del line['Other Tender']
		# # 	del line['Other Tender Type']
		# # 	del line['Other Tender Note']
		# # 	del line['Transaction ID']
		# # 	del line['Payment ID']
		# # 	del line['Card Brand']
		# # 	del line['PAN Suffix']
		# # 	del line['Device Name']
		# # 	del line['Staff Name']
		# # 	del line['Staff ID']
		# # 	del line['Details']
		# # 	del line['Description']
		# # 	del line['Event Type']
		# # 	del line['Location']
		# # 	del line['Dining Option']
		# # 	del line['Customer ID']
		# # 	del line['Customer Name']
		# # 	del line['Customer Reference ID']
		# # 	del line['Device Nickname']
		# # 	del line['Deposit ID']
		# # 	del line['Deposit Date']
		# # 	del line['Deposit Details']
		# # 	del line['Fee Percentage Rate']
		# # 	del line['Fee Fixed Rate']
		# # 	del line['Refund Reason']
		# 	csv_writer.writerow(line)