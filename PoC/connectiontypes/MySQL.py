#Simple implementation of MySQL connection
#Peewee is a nice ORM
from ConnectionManager import ConnectionManager
import peewee
from peewee import *


class MySQL(ConnectionManager):
	#When we create a new MySQL instance we want to tell our connectionmanager to set up mysql for us
	def __init__(self):
		super().__init__("SQL")
		self.db = MySQLDatabase(self.dbname, host=self.host, port=self.port, user=self.username, passwd=self.password) 
	
	#Do the obvious
	def connect(self):
		self.db.connect();
		