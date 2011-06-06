try:
    import sys
    
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

regexObjects = {"Name": QRegExp(r"^[a-z]{1,20}$",
                                Qt.CaseInsensitive),
                "HouseNumber": QRegExp(r"^[0-9]{1,5}$"),
                "Street": QRegExp(r"^[a-z]{1,20}\s[a-z]{1,20}$",
                                  Qt.CaseInsensitive),
                "Town": QRegExp(r"^[a-z]{1,20}\s[a-z]{1,20}$",
                                Qt.CaseInsensitive),
                "Postcode": QRegExp(r"^[a-z]{1,2}[0-9]{1,2}[0-9][a-z][a-z]$",
                                    Qt.CaseInsensitive),
                "VehicleRegistration": QRegExp(r"^[a-z][a-z0-9]{1,7}$",
                                               Qt.CaseInsensitive)}