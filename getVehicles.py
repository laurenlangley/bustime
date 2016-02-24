#!/usr/bin/env python

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json
#from apiclient.discovery import build

#service = build('api_name', 'api_version', ...)

#api_key = AIzaSyBSeJkxFLXt9Qc912_b4c6gCLrChUrVMMI
#gmaps = GoogleMaps(api_key)


# By default, function searches for all MARTA routes.
def getBuses(route=''):
    # Base URL for MARTA API
    base = 'http://developer.itsmarta.com/BRDRestService/BRDRestService.svc/'

    # If user does not input a value for route number, use 'GetAllBus' API call
    if route == '':
        query = 'GetAllBus'
    # Else, use 'GetBusByRoute' API call with user-defined route number
    else:
        query = 'GetBusByRoute/' + str(route)

    response = urllib2.urlopen(base + query, timeout=30)
    str_response = response.read()
    buses = json.loads(str_response.decode('utf-8'))

    # Prints entirety of json response
    #print(buses)
    with open('data.json', 'w') as jsonfile:
        json.dump(buses, jsonfile)

    output = ''

    # For each bus in response, print a few pieces of data.
    for bus in buses:
        output = 'ROUTE:' + bus['ROUTE'] + ' LAT:' + bus['LATITUDE'] + ' LON:' + bus['LONGITUDE'] + ' TIMEPOINT:' + bus['TIMEPOINT'] + ' ADHER:' + bus['ADHERENCE'] + ' VEHICLE:' + bus['VEHICLE'] + ' at:' + bus['MSGTIME'] + '\n'
        print(output)

        #destination = gmaps.latlng_to_address(bus['LATITUDE'], bus['LONGITUDE'])
        #print(destination)

    #checkTripIds(buses)

# Determines how many of the buses have TripIDs
def checkTripIds(buses):
    count = 0
    total = len(buses)
    for bus in buses:
        tripId = bus['TRIPID']
        # print("Current Trip ID: " + tripId)

        if (tripId == ''):
            count += 1
    print(str(count) + " of " + str(total) + " do not have Trip IDs\n")
