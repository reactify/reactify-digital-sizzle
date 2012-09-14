import urllib2

#import https://trac.v2.nl/attachment/wiki/pyOSC/pyOSC-0.3.5b-5294.tar.gz
import OSC

# http://pypi.python.org/pypi/simplejson/
import simplejson

port = 8080

# the url for the data api, return as json, NOT jsonp
url = "http://developer.echonest.com/api/v4/song/search?api_var2=N6E4NIOVYMTHNDM8J&format=json&artist=All%20Good%20Funk%20Alliance&title=Super%20Jam&bucket=audio_summary"


# go fetch all the data as json, DO NOT TOUCH THIS
req = urllib2.Request(url, None, {'user-agent':'syncstream/vimeo'})
opener = urllib2.build_opener()
f = opener.open(req)
data = simplejson.load(f)

# for debugging
print data

# THIS IS WHAT YOU WANT TO EDIT FOR WHICHEVER API
# parse the data to retreive whatever you want
results = data['response']['songs']

var1 = results[0]['audio_summary']['tempo']
var2 = results[0]['audio_summary']['key']
var3 = results[0]['audio_summary']['mode']

print 'var1:',var1
print 'var2:',var2
print 'var3:',var3

client = OSC.OSCClient()
msg = OSC.OSCMessage()
msg.setAddress("/var1")
msg.append(var1)
client.sendto(msg, ('localhost', port))

client = OSC.OSCClient()
msg = OSC.OSCMessage()
msg.setAddress("/var2")
msg.append(var2)
client.sendto(msg, ('localhost', port))

client = OSC.OSCClient()
msg = OSC.OSCMessage()
msg.setAddress("/var3")
msg.append(var3)
client.sendto(msg, ('localhost', port))