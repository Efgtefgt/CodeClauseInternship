# pip install pyshorteners
import pyshorteners

url = input('Enter the URL :')

def shorternedURL(url):
    s=pyshorteners.Shortener()
    print('shorterned url :'+s.tinyurl.short(url))

shorternedURL(url)
