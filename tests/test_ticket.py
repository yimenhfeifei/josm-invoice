try:
    import unittest
    import sys
    
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class TestTicketHash(unittest.TestCase):
    
    def setUp(self):
        t1 = Ticket()
        t2 = Ticket()
        
        t1.setNumber("12000")
        t1.setDate("13/10/2011")
        t1.setTime("13:34")
        
        t1.customer.setFirstName("John")
        t1.customer.setLastName("Orchard")
        t1.customer.setHouseNumber("678")
        t1.customer.setStreet("Way")
        t1.customer.setTown("Truro")
        t1.customer.setPostcode("Tr678J")
        t1.customer.setRegistration("YT78JNK")
        
        t1.payload.addPayload()
    
    def testSetData(self):
        """"""
        pass

    def tearDown(self):
        pass
