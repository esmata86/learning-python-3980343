# LinkedIn Learning Python course by Joe Marini
# Example file for retrieving data from the internet
#
import urllib.request

web_url = urllib.request.urlopen("https://www.example.com")
print(web_url.getcode())

data = web_url.read()
print(data)