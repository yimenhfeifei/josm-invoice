try:
    import unittest
    import sys
    
    from shared_modules.ticket import Ticket
    from shared_modules.customer import Customer
    from shared_modules.payload import Payload
    from shared_modules.vehicle import Vehicle
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class TestTicketHash(unittest.TestCase):
    
    def setUp(self):
        self.customer = {"firstName": "John",
         "lastName": "Orchard",
         "houseNumber": "54",
         "street": "Bark",
         "town": "Truro",
         "postcode": "Tr679h",
         "customerReg": "HU8JJUG"}
        
        self.vehicle = {"make": "BMW",
                        "model": "Fast One",
                        "colour": "Black",
                        "reg": "GDHy487",
                        "vin": "8742942952528795",
                        "id": "Checked"}
        
        self.payload = {"weight": "1650",
                        "material": "Car",
                        "value": "155.00"}
        
        self.ticket = {"number": "12000",
                       "hashID": "",
                       "date": "24/08/2011",
                       "time": "13:56",
                       "ticketValue": "155.00"}
        
        self.ticket2 = {"number": "12000",
                        "hashID": "",
                        "date": "24/08/2011",
                        "time": "13:57",
                        "ticketValue": "155.00"}
        
        self.CustomerObject = Customer(self.customer)
        self.payloadObject = Payload(self.payload, Vehicle(self.vehicle))
    
    def testCollision(self):
        """Two identical tickets must produce hash collision."""
        self.t1 = Ticket(self.ticket, self.CustomerObject, self.payloadObject)
        
        self.t2 = Ticket(self.ticket, self.CustomerObject, self.payloadObject)
        
        self.assertEqual(self.t1.hashId, self.t2.hashId)

    def testNoCollision(self):
        """Two different tickets must not produce hash collision."""
        self.t1 = Ticket(self.ticket2, self.CustomerObject, self.payloadObject)
        
        self.t2 = Ticket(self.ticket, self.CustomerObject, self.payloadObject)
        
        self.assertNotEqual(self.t1.hashId, self.t2.hashId)
    
    def tearDown(self):
        self.t1 = None
        self.t2 = None

if __name__ == "__main__":
    unittest.main()
