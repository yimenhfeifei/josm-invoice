try:
    import sys
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

submitTicket = "insert into tickets values ({number}, '{date}', '{time}', '{name}', '{house}', '{street}', '{town}', '{postcode}', '{reg}', '{hashId}', false)"

setPaidToTrue = "update {table} set paid = true where {field} = '{value}'"
valueInDatabase = "select hash from {table} where {field} = '{value}'"


insertMaterialsRecord = ("INSERT INTO materials (material, price, ferrous)"
                         "VALUES (:material, :price, :ferrous)")

selectPrices = ("SELECT material, price from materials where ferrous = :ferrousBool")

# Creation statements.
createMaterialsTable = ("CREATE TABLE materials ("
                        "material VARCHAR(40) PRIMARY KEY UNIQUE NOT NULL,"
                        "price FLOAT(16,2) NOT NULL,"
                        "ferrous BOOL)")
