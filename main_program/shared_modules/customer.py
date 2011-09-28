try:
    import sys
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class Customer(object):
    def __init__(self, customer):
        self.firstName = customer["firstName"]
        self.lastName = customer["lastName"]
        self.houseNumber = customer["houseNumber"]
        self.street = customer["street"]
        self.town = customer["town"]
        self.postcode = customer["postcode"]
        self.customerRegistration = customer["customerReg"]
