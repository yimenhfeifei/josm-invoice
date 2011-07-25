try:
    import sys
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class Customer(object):
    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        self.houseNumber = ""
        self.street = ""
        self.town = ""
        self.postcode = ""
        self.vehicleRegistration = ""
    
    def setFirstName(self, firstName):
        self.firstName = firstName
        
    def setLastName(self, lastName):
        self.lastName = lastName
        
    def setHouseNumber(self, houseNumber):
        self.houseNumber = houseNumber
        
    def setStreet(self, street):
        self.street = street
        
    def setTown(self, town):
        self.town = town
        
    def setPostcode(self, postcode):
        self.postcode = postcode
        
    def setVehicleRegistration(self, registration):
        self.vehicleRegistration = registration
