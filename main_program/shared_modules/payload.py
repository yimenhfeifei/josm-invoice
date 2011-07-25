try:
    import sys
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class Payload(object):
    def __init__(self):
        self.payloads = []
        self.vehicles = []
