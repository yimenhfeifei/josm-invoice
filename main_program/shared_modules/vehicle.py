try:
    import sys
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class Vehicle(object):
    def __init__(self, vehicle):
        self.vehicleType = vehicle["type"]
        self.make = vehicle["make"]
        self.model = vehicle["model"]
        self.colour = vehicle["colour"]
        self.registration = vehicle["registration"]
        self.vin = vehicle["vin"]
        self.catalyticConverterBoolean = vehicle["catBool"]
        self.catalyticConverterValue = vehicle["catValue"]
