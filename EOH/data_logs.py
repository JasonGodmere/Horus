
from EOH.models import Performance

# third-party
import pandas
import time


'''
Data for any given EOH node stores data
by month (default) in csv files associated with a
row in the EOH set of data log tables.

Accessing those files should be done with
this intermediary tool for any read/append
task that accesses the csv files in question.
Using this module should not require much if 
any understanding of the EOH model structure.

The idea is to make this as simple as possible
while maximizing efficiency and minimizing
overhead/latency.
'''


### Module Configuration Settings ###
# changing these with a live db may cause problems

NEW_ENTRY_FREQ = 30 # days
LOG_FREQ = 60 # seconds



### Extends Performance Model ###

def read(node_id);#, model='Performance'):
	'''
	return all available csv data from database
	for given node id
	'''
	entries = Performance.objects.filter(node=node_id)

	# recursive function for accessing logs that may
	# exist accross multiple db entries
	def pull(node_id, start, end):
		
		




def append(node_id, ):
	pass