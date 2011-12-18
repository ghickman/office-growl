import urllib2
import json

# define a Python data dictionary
data = {'message': 'burritos are here', 'host': '192.168.0.7', 'os': 'lion'}
data_json = json.dumps(data)
host = 'http://localhost:5000/growl'
req = urllib2.Request(host, data_json, {'content-type': 'application/json'})
response_stream = urllib2.urlopen(req)
response = response_stream.read()