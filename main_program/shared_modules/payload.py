try:
    import sys
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class Payload(object):
    def __init__(self, payload, vehicle=None):
        self.weight = payload["weight"]
        self.material = payload["material"]
        self.value = payload["value"]
        self.vehicle = vehicle
