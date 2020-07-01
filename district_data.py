import json
from Data.district_download import downloadData

def district(state):
    try:
        districtData = data[state]['districtData']
    except Exception as E:
        print('Invalid data')
        getState()
    
    print('\n\nDistricts in',state+':\n')  
    print('District'.ljust(20,' ')+'Active'.ljust(10,' ')+'Confirmed'.ljust(10,' ')+'Deceased'.ljust(10,' ')+'Recovered'.ljust(10,' '))
    print()
    
    for district in districtData:
        districts = districtData[district]
        
        print('{:<20}{:<10}{:<10}{:<10}{:<10}'.format(district,districts['active'],districts['confirmed'],districts['deceased'],districts['recovered']))
        print()
    

def getState():
    print('States in India:\n')
    for states in data:
        print(' '*5+states)
    print('\n')
    state = input('Select state : ')
    district(state)

if __name__ == '__main__':
    try:
        downloadData()
    except Exception as E:
        print(E)
    file = open('Data/district_download.json')
    data = json.load(file)
    getState()
