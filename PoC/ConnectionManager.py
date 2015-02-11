#ConnectionManager takes the heavy lifting out of configuration management
import configparser


class ConnectionManager:
	
	
	
	#Grab connection type from config
	#Also python is weird and likes to automatically send instances but not automatically receive them, so we need to specify self here
	def __init__(self, connectionType):
		
		#Variable location - this probably shouldn't go here
		configLocation = "./conf/dbinfo.ini"
	
		#Read in config from location
		self.Config = configparser.ConfigParser()
		self.Config.read(configLocation)
		
		#Set local variables
		#This is very MySQL at the minute and should be revisited
		self.dbname = self.Config[connectionType]['DBName']
		self.host = self.Config[connectionType]['Host']
		self.username = self.Config[connectionType]['Username']
		self.password = self.Config[connectionType]['Password']
		self.port = self.Config[connectionType]['Port']
		
	