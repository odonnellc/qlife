#This is a proof of concept and does not reflect the final product

import requests
from connectiontypes.MySQL import MySQL

#Grab the library seating
request = requests.get('http://pcs.qub.ac.uk/')
database = MySQL()

#Output it to a file
with open("output.txt", "wt") as out_file:
	out_file.write(request.text);
	
#Test a connection
database.connect()