import psycopg2

conn = psycopg2.connect(
    database = "dd75re8gpemlhh",
    user = "dgasqbsxpyknsj",
    password = "b291aec1072c11c216a18636825ae58778688c3d57ee779cd951ddbb9299e6ce",
    host = "ec2-18-210-51-239.compute-1.amazonaws.com",
    port = "5432"
)

cur = conn.cursor()

cur.execute("SELECT * FROM transfermktAPI_transfer")

conn.commit()

print("QUERY EXECUTED")

conn.close()