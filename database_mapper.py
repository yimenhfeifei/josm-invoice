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
    
    def __init__(self, fileName):
        self.engine = create_engine("sqlite:///{}".format(fileName),
                                    echo=False)
        base.metadata.create_all(self.engine)
        self.sessionMaker = sessionmaker(bind=self.engine)
        self.session = self.sessionMaker()
        self.programStrings = []
        self.purchaseCustomers = []
        self.salesCustomers = []
        
    def addProgramString(self, name, text, fontName, fontSize, fontFlags):
        self.programStrings.append(ProgramString(name,
                                                 text,
                                                 fontName,
                                                 fontSize,
                                                 fontFlags))
        
        self.session.add(self.programStrings[-1])
        
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
   

class ProgramString(base):
    
    __tablename__ = "program_strings"
    name = Column(String, primary_key=True)
    text = Column(String)
    fontName = Column(String)
    fontSize = Column(Integer)
    fontFlags = Column(Integer)
    
    def __init__(self, name, text, fontName, fontSize, fontFlags):
        self.name = name
        self.text = text
        self.fontName = fontName
        self.fontSize = fontSize
        self.fontFlags = fontFlags

    def __repr__(self):
        return "<ProgramString ({}, {}, {}, {}, {})>".format(self.name,
                                                             self.text,
                                                             self.fontName,
                                                             self.fontSize,
                                                             self.fontFlags)


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


d = Database("testing_db.db")
#d.addSalesCustomer("Fanny", "Whore House", "69")
#d.addProgramString("compkany", "John Orchard & Company", "Helvetica", 12, 75)
#d.persist()
print(d.session.query(PurchaseCustomer).all())
print(d.session.query(SalesCustomer).all())
print(d.session.query(ProgramString).all())