#Import the following modules
#It is assumed that the file is in CSV format
import csv
import sys
import os
import re
import json
from bs4 import BeautifulSoup
import requests
from elasticsearch import Elasticsearch
#path to the file containing data
currentDirectory = os.path.dirname(os.path.realpath(__file__))
#defined a class with the function that can be called upon when required
class ElasticSearchImporter(object):
    def importToDb(self, fileName, indexDbName, indexType="default"):
		csv.field_size_limit(sys.maxsize)
		es = Elasticsearch()
		list = []
		headers = []
        # setting index as 0 initially
		index = 0

		f = open(dataFilePath+fileName, 'rb')
		reader = csv.reader(f)
# ittirate through each row to get the data
		try:
			for row in reader:
				try:
					if(index == 0):
						headers = row
					else:
						obj = {}
						for i, val in enumerate(row):
							obj[headers[i]] = val
						# put document into elastic search
						# Elastic Search 6.0 + doesn't support multiple types in one index.
						es.index(index=indexDbName, doc_type=indexType, body=obj)

				except Exception as e:
					print(index)
					print(e)

				index = index + 1
		except:
			print ('error')

		if not f.closed:
			f.close()
#call the function with the file name
importer = ElasticSearchImporter()
importer.importToDb("begineer_assignment01.csv", "product_listing", indexType="default")
