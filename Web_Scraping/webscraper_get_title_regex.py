import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode('utf-8')

pattern = "<title.*?>.*?</title.*?>"  # regex pattern; *? non-greedily matches all text 
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)  # Removes HTML tags
print(title)
