import urllib
url = 'https://www.google.com'
response = urllib.urlopen(url)
data = response.read()
print data