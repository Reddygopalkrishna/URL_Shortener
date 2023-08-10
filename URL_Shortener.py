# url Shortener

import pyshorteners

url=input('Enter the link here :')
shortener=pyshorteners.Shortener()
result=shortener.tinyurl.short(url)
print("Shorten link :",result)

