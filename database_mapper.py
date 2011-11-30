#!/usr/bin/python3
try:
    import traceback
    import sys
    
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String

except ImportError as err:
    eType, eValue, eTb = sys.exc_info()
    fileName, lineNum, funcName, text = traceback.extract_tb(eTb)[-1]
    print("{0} -> {1}".format(fileName, err))
    raise SystemExit(err)

base = declarative_base()

class ProgramStrings(base):
    
    def __init__(self):
        pass


class PurchaseCustomer(base):
    
    __tablename__ = "purchase_customers"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    vatReg = Column(String)
    
    def __init__(self):
        pass


class SalesCustomer(base):
    
    __tablename__ = "sales_customers"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    vatReg = Column(String)    
    
    def __init__(self):
        pass