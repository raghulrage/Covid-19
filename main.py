import json


def states(data):
    print('\n\nStates in India:\n\n')
    
    for states in data.keys():
        print(' '*10,states)
    print()
    
    while True:
        state = input('Select State: ')
        
        if state == 'E':
            break
        else:
            if state in data.keys():
                districts(state)
                break
            else:
                print('Invalid Data!! Enter Again')

def districts(state):
    print('\n\nDistricts in {}:\n\n'.format(state))
    states = data[state]
    for districts in states.keys():
        
        print(' '*10,districts)
    print()
    while True:
        district = input('Select Disrtict: ')
        if district == 'E':
            break
        else:
            if district in states.keys():
                display(states[district])
                break
            else:
                print('Invalid Data!! Enter Again')

def display(district):
    print('\n\n')
    print('Date         |'+' Active Case |'+' Confirmed Case |'+' Deceased Case |'+' Recovered Case')
    print('\n')
    for data in district[::-1]:
        print(data['date']+'   | '+str(data['active']).center(12,' ')+'| '+str(data['confirmed']).center(15,' ')+'| '+str(data['deceased']).center(14,' ')+'| '+ str(data['recovered']).center(14,' '))



'''with request.urlopen('https://api.covid19india.org/districts_daily.json') as response:
    data = json.loads(response.read())
    data = data['districtsDaily']'''


file = open('Data/daily_data.json',)
data = json.load(file)
data  = data['districtsDaily']
states(data)

