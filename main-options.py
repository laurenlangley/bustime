import getopt, sys
from getVehicles import getBuses

def main():
    handleOptions()
    initBus()

def initBus():
    # Input function to obtain route number from user
    route = input('\n\n*******Get Buses*******\n\nPlease enter a route number (leave blank for all routes):\n\n')

    # Call getBuses function with user-defined route number
    getBuses(route)

def handleOptions():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "btho:v", ["bus", "help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-b", "--bus"):
            initBus()
            sys.exit()
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"

def usage():
    print("\n\n--help\n\nThis is how you use it.\n\n")

if __name__ == '__main__':
    main()