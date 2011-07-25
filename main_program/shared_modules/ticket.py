try:
    import sys
    
    from customer import Customer
    from payload import Payload
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class Ticket(onject):
    def __init__(self, ticket):
        self.number = ticket["number"]
        self.hashId = ""
        self.date = ticket["date"]
        self.time = ticket["time"]
        
        self.customer = ticket["customer"]
        self.payloads = []
    
    def setHashId(self, hashId):
        self.hashId = hashId
    
    def generateHashId(self):
        pass

    def addPayload(self, payload):
        self.payloads.append(payload)
