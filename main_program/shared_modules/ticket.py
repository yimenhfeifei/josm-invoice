try:
    import sys
    import hashlib
    
    from shared_modules.payload import Payload
    from shared_modules.byte_count_hasher import ByteCountHasher
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
            
        self.size = 0
        self.generateHashId()
        
    def getTicket(self):
        ticket = {"number": self.number,
                  "hashId": self.hashId,
                  "date": self.date,
                  "time": self.time,
                  "totalValue": self.totalValue,
                  "firstName": self.customer.firstName,
                  "lastName": self.customer.lastName,
                  "houseNumber": self.customer.houseNumber,
                  "street": self.customer.street,
                  "town": self.customer.town,
                  "postcode": self.customer.postcode,
                  "registration": self.customer.vehicleRegistration}
        ticket.update(self.getPayload())
        return ticket

    def getPayload(self):
        collectedPayloads = {}
        for number, payload in enumerate(self.payloads):
            currentPayload = {}
            currentPayload["weight"] = payload.weight
            currentPayload["material"] = payload.material
            currentPayload["value"] = payload.value
            
            if payload.vehicle:
                currentPayload["vehicle"] = payload.vehicle.getVehicle()
                
            collectedPayloads["payload {}".format(number)] = currentPayload
        
        return collectedPayloads
    
    def hashAll(self, hashable, hasher):
        for field, value in hashable.items():
            if isinstance(value, dict):
                self.hashAll(value, hasher)
                continue
            hasher.update(value)
        
    def hashPayloads(self, hasher):
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
                hasher.update(bytes(payload.vehicle.catalyticCheckbox, "UTF-8"))
                hasher.update(bytes(payload.vehicle.catalyticValue, "UTF-8"))
                hasher.update(bytes(payload.vehicle.Id, "UTF-8"))
    
    def generateHashId(self):
        hasher = ByteCountHasher("md5")
        
        self.hashAll(self.getTicket(), hasher)
                
        self.hashId = hasher.hexdigest()
        
        self.size = len(bytes(self.hashId, "UTF-8")) + hasher.getNumBytesHashed()
