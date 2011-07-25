try:
    import sys
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class Vehicle(object):
    def __init__(self):
        self.vehicleType = ""
        self.make = ""
        self.model = ""
        self.colour = ""
        self.registration = ""
        self.vin = ""
        self.catalyticConverterBoolean = ""
        self.catalyticConverterValue = ""
        self.ID = ""
        
    def setVehicleType(self, vehicle):
        self.vehicleType = vehicle
        
    def setMake(self, make):
        self.make = make
        
    def setModel(self, model):
        self.model = model
        
    def setColour(self, colour):
        self.colour = colour
        
    def setRegistration(self, registration):
        self.registration = registration
        
    def setVin(self, vin):
        self.vin = vin
        
    def setCatalyticConverterBoolean(self, catBool):
        self.catalyticConverterBoolean = catBool
        
    def setCatlyticConverterValue(self, catValue):
        self.catalyticConverterValue = catValue