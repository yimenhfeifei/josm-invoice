try:
    import sys
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class Vehicle(object):
    def __init__(self, vehicle):
        self.make = vehicle["make"]
        self.model = vehicle["model"]
        self.colour = vehicle["colour"]
        self.registration = vehicle["reg"]
        self.vin = vehicle["vin"]
        self.Id = vehicle["id"]

    def getVehicle(self):
        return {"make": self.make,
                "model": self.model,
                "colour": self.colour,
                "reg": self.registration,
                "vin": self.vin,
                "id": self.Id}