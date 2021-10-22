import urllib.request
import urllib.parse
import urllib.error
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter a URL to scrape: ')
html = urllib.request.urlopen(url, context=ctx).read()

# Find links by regex
links = re.findall(b'href="(http[s]?://.*?)"', html)

# Print links found
for link in links:
    print(link.decode())
