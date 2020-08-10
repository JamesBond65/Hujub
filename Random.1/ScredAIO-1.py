from urllib.requests import build_opener, HTTPCookieProcessor, HTTPHandler
import requests
import http.cookiejar as cookielib

#Create a CookieJar object to hold the cookies
cj = cookielib.CookieJar()
#Create an opener to open pages using the http protocol and to process cookies.
opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())

#create a request object to be used to get the page.
req = request.get("https://temp-mail.org/fr/")
f = opener.open(req)

#see the first few lines of the page
html = f.read()
print (html[:50])

#Check out the cookies
print( "the cookies are: ")
for cookie in cj:
    print (cookie)