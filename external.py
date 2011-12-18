import urllib2
import json

# define a Python data dictionary
data = {'message': '', 'host': '', 'os': '', 'password': ''}
data_json = json.dumps(data)
host = 'http://localhost:5000/'
req = urllib2.Request(host, data_json, {'content-type': 'application/json'})
response_stream = urllib2.urlopen(req)
response = response_stream.read()