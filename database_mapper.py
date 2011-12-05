#!/usr/bin/python3
try:
    import traceback
    import sys
    
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.orm import sessionmaker

except ImportError as err:
    eType, eValue, eTb = sys.exc_info()
    fileName, lineNum, funcName, text = traceback.extract_tb(eTb)[-1]
    print("{0} -> {1}".format(fileName, err))
    raise SystemExit(err)

base = declarative_base()

class Database(object):
    
    def __init__(self, fileName, driver):
        self.engine = create_engine("{}:///{}".format(driver, fileName),
                                    echo=False)
        base.metadata.create_all(self.engine)
        self.sessionMaker = sessionmaker(bind=self.engine)
        self.session = self.sessionMaker()
        self.purchaseCustomers = []
        self.salesCustomers = []
        
    def addPurchaseCustomer(self, name, address, vatReg):
        self.purchaseCustomers.append(PurchaseCustomer(name,
                                                       address,
                                                       vatReg))
        
        self.session.add(self.purchaseCustomers[-1])

    def addSalesCustomer(self, name, address, vatReg):
        self.salesCustomers.append(SalesCustomer(name,
                                                 address,
                                                 vatReg))
        
        self.session.add(self.salesCustomers[-1])

    def persist(self):
        self.session.commit()
        
    def getPurchaseCustomersDict(self):
        records = {}
        for customer in self.session.query(PurchaseCustomer).all():
            records[customer.name] = {"address": customer.address,
                                      "vatReg": customer.vatReg}
        
        return records
    
    def getSalesCustomersDict(self):
        records = {}
        for customer in self.session.query(SalesCustomer).all():
            records[customer.name] = {"address": customer.address,
                                      "vatReg": customer.vatReg}
            
        return records


class PurchaseCustomer(base):
    
    __tablename__ = "purchase_customers"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    vatReg = Column(String)
    
    def __init__(self, name, address, vatReg):
        self.name = name
        self.address = address
        self.vatReg = vatReg
        
    def __repr__(self):
        return "<PurchaseCustomer ({}, {}, {}, {})>".format(self.id,
                                                            self.name,
                                                            self.address,
                                                            self.vatReg)


class SalesCustomer(base):
    
    __tablename__ = "sales_customers"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    vatReg = Column(String)    
    
    def __init__(self, name, address, vatReg):
        self.name = name
        self.address = address
        self.vatReg = vatReg
        
    def __repr__(self):
        return "<SalesCustomer ({}, {}, {}, {})>".format(self.id,
                                                         self.name,
                                                         self.address,
                                                         self.vatReg)
