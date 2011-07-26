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
        self.catalyticBoolean = vehicle["catBool"]
        self.catalyticValue = vehicle["catValue"]

    def getVehicle(self):
        return {"type": self.vehicleType,
                "make": self.make,
                "model": self.model,
                "colour": self.colour,
                "registration": self.registration,
                "vin": self.vin,
                "catBool": self.catalyticBoolean,
                "catValue": self.catalyticValue}