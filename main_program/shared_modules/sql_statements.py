try:
    import sys
    
except ImportError as err:
    print("Couldn't load module: {0}".format(err))
    raise SystemExit(err)

submitTicket = "insert into tickets values ({number}, '{date}', '{time}', '{name}', '{house}', '{street}', '{town}', '{postcode}', '{reg}', '{hashId}', false)"

setPaidToTrue = "update {table} set paid = true where {field} = '{value}'"
valueInDatabase = "select hash from {table} where {field} = '{value}'"