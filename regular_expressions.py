try:
    import sys
    import re
   
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

regexObjects = {"name": re.compile(r"^[a-z]{1,20}$", re.I),
                
                "houseNumber": re.compile(r"^[0-9]{1,5}$"),
                
                "street": re.compile(r"^[a-z]{1,20}(\s[a-z]{1,20})?$", re.I),
                
                "town": re.compile(r"^[a-z]{1,20}(\s[a-z]{1,20})?$", re.I),
                
                "postcode": re.compile(r"^[a-z]{1,2}[0-9]{1,2}\s?[0-9][a-z]{2}$",
                                       re.I),
                
                "vehicleRegistration": re.compile(r"^[a-z][a-z0-9]{2,7}$", re.I),
                
                "weight": re.compile(r"^(\d{1,8}(\.\d{1,2})?|\.\d{1,3})$"),
                
                "value": re.compile(r"^\d{1,8}(\.\d{1,3})?$"),
                
                "integer": re.compile(r"^\d+$"),
                
                "model": re.compile(r"^(|[a-z0-9\s]{1,30})$", re.I),
                
                "description": re.compile(r"^(\w+\s?)+(\([a-z][a-z0-9]{2,7}\))?$", re.I),
                
                "vin": re.compile(r"^(|[a-z0-9]{1,17})$", re.I),
                
                "spanTagContents": re.compile(r"([^>]*)(?=</span>)"),
                
                "post2001Reg": re.compile(r"^[a-hj-pr-y]{2}[0-9]{2}\s?[a-z]{3}$",
                                          re.I),
                
                "qMaterial": QRegExpValidator(QRegExp(r"^(.+(\s)?)+$"), None),
                
                "qPrice": QRegExpValidator(QRegExp(r"^\d{1,5}(\.\d{1,2})?$"), None),
                
                "qValue": QRegExpValidator(QRegExp(r"^\d{1,8}(\.\d{1,3})?$"), None)}
