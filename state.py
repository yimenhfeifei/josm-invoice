#!/usr/bin/python3
try:
    import traceback
    import sys

except ImportError as err:
    eType, eValue, eTb = sys.exc_info()
    fileName, lineNum, funcName, text = traceback.extract_tb(eTb)[-1]
    print("{0} -> {1}".format(fileName, err))
    raise SystemExit(err)
                
class State(object):
    def __init__(self):
        self.variables = []
        
    def addVariable(self, variable, value):
        self.variables.append((variable, value))

    def enable(self):
        for k, v in self.variables:
            if hasattr(k, "__call__"):
                k(v)
            else:
                k = v
