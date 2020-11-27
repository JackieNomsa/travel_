import pymysql

mydb = pymysql.connect(
    host='localhost',
    user='root',
    passwd='12345',
    database='south_africa',)

mycursor = mydb.cursor()

# mycursor.execute('ALTER TABLE gauteng DROP COLUMN picture')

# for i in mycursor:
#     print(i)




