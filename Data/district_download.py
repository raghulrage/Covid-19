import json
import urllib.request as request

def downloadData():
    with request.urlopen('https://api.covid19india.org/state_district_wise.json') as response:
        data = json.loads(response.read())

    with open('district_download.json','w') as file:
        json.dump(data,file)
