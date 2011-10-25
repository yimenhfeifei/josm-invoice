try:
    import sys
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

submitTicket = "insert into tickets values ({number}, '{date}', '{time}', '{name}', '{house}', '{street}', '{town}', '{postcode}', '{reg}', '{hashId}', false)"

setPaidToTrue = "update {table} set paid = true where {field} = '{value}'"
valueInDatabase = "select hash from {table} where {field} = '{value}'"


# Modification statements
insertMaterialsRecord = ("INSERT INTO materials (material, price, ferrousFlag)"
                         "VALUES (:material, :price, :ferrousFlag)")


replaceMaterialsRecord = ("REPLACE INTO materials (material, price, ferrousFlag)"
                          "VALUES (:material, :price, :ferrousFlag)")

# View statements
selectPrices = ("SELECT material, price from materials where ferrousFlag = :ferrousFlag")

# Creation statements.
createMaterialsTable = ("CREATE TABLE if not exists materials ("
                        "material VARCHAR(40) PRIMARY KEY UNIQUE NOT NULL,"
                        "price FLOAT(16,2) NOT NULL,"
                        "ferrousFlag VARCHAR(20))")
