try:
    import sys
    from os import getuid
    from pwd import getpwuid

    import pymysql
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    
    from shared_modules.server_manager import ServerManager
    from shared_modules.sql_statements import valueInDatabase
    from shared_modules.sql_statements import setPaidToTrue
    from shared_modules.sql_statements import submitTicket
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

class MysqlManager(ServerManager):
    def __init__(self):
        super(MysqlManager, self).__init__()
        
        self.cur = None

    def connect(self, databaseSettings):
        conn = pymysql.connect(**databaseSettings)
        
        self.cur = conn.cursor()
    
    def valueInDatabase(self, field, value):
        sql = valueInDatabase.format(table="tickets",
                                     field="hash",
                                     value=value)
        self.cur.execute(sql)
        
        if self.cur.fetchone():
            return True
        else:
            return False
        
    def setPaidTrue(self, field, value):
        sql = setPaidToTrue.format(table="tickets",
                                   field="hash",
                                   value=value)
        
        return self.cur.execute(sql)
            
    def submitTicket(self, ticket):
        sql = submitTicket.format(number=ticket["number"],
                                  date=ticket["date"],
                                  time=ticket["time"],
                                  name=ticket["firstName"],
                                  house=ticket["houseNumber"],
                                  street=ticket["street"],
                                  town=ticket["town"],
                                  postcode=ticket["postcode"],
                                  reg=ticket["customerReg"],
                                  hashId=ticket["hashId"])
        
        if self.cur.execute(sql):
            print("update complete")
        else:
            print("update failed")
        