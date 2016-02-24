import json
from getVehicles import getBuses
import time

def main():

    route = ""

    # Input function to obtain route number from user
    #route = getInput("route")

    # Call getBuses function with user-defined route number
    # getBuses(route)

    while True:
        getBuses(route)
        time.sleep(60)

def usage():
    print("\n--help\nThis is how you use it.\n")


def getInput(mode):
    vehicle = "Buses"
    #if (mode == "route"):
    #    vehicle = "Buses"
    #else:
    #    vehicle = "Trains"
    message = '\n\n*******Get' + vehicle + '*******\nPlease enter a route number\n(leave blank for all routes)\n(type \'?\' for a list of ' + mode + 's)\n'

    userInput = input(message)

    if (userInput == "?"):
        showJSON(mode)
        userInput = getInput(mode)

    return userInput


def showJSON(mode):
    json_data = open('json')

    data = json.load(json_data)
    print("\nList of " + mode + "s:\n")
    for i in data[mode]:
        print(i)
    json_data.close()


if __name__ == '__main__':
    main()
