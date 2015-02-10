import requests

request = requests.get('http://pcs.qub.ac.uk/')

with open("output.txt", "wt") as out_file:
	out_file.write(request.text);
