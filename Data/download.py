import json
import urllib.request as request
with request.urlopen('https://api.covid19india.org/districts_daily.json') as response:
    data = json.loads(response.read())
with open('daily_data.json', 'w') as outfile:
    json.dump(data, outfile)
