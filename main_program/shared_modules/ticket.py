try:
    import sys
    import hashlib
    
    from shared_modules.payload import Payload
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class Ticket(object):
    def __init__(self, ticket, customer, payload):
        self.number = ticket["number"]
        self.hashId = ""
        self.date = ticket["date"]
        self.time = ticket["time"]
        self.totalValue = ticket["totalValue"]        
        
        self.customer = customer
        self.payloads = []
       
        if isinstance(payload, Payload):
            self.payloads.append(payload)
        else:
            self.payloads = payload
            
        self.generateHashId()
    
    def generateHashId(self):
        hasher = hashlib.md5()
        
        hasher.update(bytes(self.number, "UTF-8"))
        hasher.update(bytes(self.date, "UTF-8"))
        hasher.update(bytes(self.time, "UTF-8"))
        hasher.update(bytes(self.totalValue, "UTF-8"))
        
        hasher.update(bytes(self.customer.firstName, "UTF-8"))
        hasher.update(bytes(self.customer.lastName, "UTF-8"))
        hasher.update(bytes(self.customer.houseNumber, "UTF-8"))
        hasher.update(bytes(self.customer.street, "UTF-8"))
        hasher.update(bytes(self.customer.town, "UTF-8"))
        hasher.update(bytes(self.customer.postcode, "UTF-8"))
        hasher.update(bytes(self.customer.vehicleRegistration, "UTF-8"))
        
        for payload in self.payloads:
            hasher.update(bytes(payload.weight, "UTF-8"))
            hasher.update(bytes(payload.material, "UTF-8"))
            hasher.update(bytes(payload.value, "UTF-8"))
            if payload.vehicle:
                hasher.update(bytes(payload.vehicle.vehicleType, "UTF-8"))
                hasher.update(bytes(payload.vehicle.make, "UTF-8"))
                hasher.update(bytes(payload.vehicle.model, "UTF-8"))
                hasher.update(bytes(payload.vehicle.colour, "UTF-8"))
                hasher.update(bytes(payload.vehicle.registration, "UTF-8"))
                hasher.update(bytes(payload.vehicle.vin, "UTF-8"))
                hasher.update(bytes(payload.vehicle.catalyticBoolean, "UTF-8"))
                hasher.update(bytes(payload.vehicle.catalyticValue, "UTF-8"))
                
        self.hashId = hasher.hexdigest()

    def addPayload(self, payload):
        self.payloads.append(payload)
