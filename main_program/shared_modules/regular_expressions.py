try:
    import sys
    import re
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

regexObjects = {"Name": re.compile(r"^[a-z]{1,20}$", re.I),
                
                "HouseNumber": re.compile(r"^[0-9]{1,5}$"),
                
                "Street": re.compile(r"^[a-z]{1,20}(\s[a-z]{1,20})?$", re.I),
                
                "Town": re.compile(r"^[a-z]{1,20}(\s[a-z]{1,20})?$", re.I),
                
                "Postcode": re.compile(r"^[a-z]{1,2}[0-9]{1,2}\s?[0-9][a-z][a-z]$",
                                       re.I),
                
                "VehicleRegistration": re.compile(r"^[a-z][a-z0-9]{2,7}$",
                                                  re.I),
                
                "optionalWeight": re.compile(r"^(|[0-9]{1,5}\.(5|0)0*)$"),
                
                "NetWeight": re.compile(r"^[0-9]{1,5}\.(5|0)0*$")}