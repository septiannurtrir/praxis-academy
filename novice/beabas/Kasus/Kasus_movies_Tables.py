import mysql.connector

cnx = mysql.connector.connect(user='septiannurtrir', password='sandaljebatds07', database='Kasus')
cursor = cnx.cursor()

query = ("SELECT Table2.movies_Rented, Table1.full_Names FROM Table2 INNER JOIN Table1 ON Table2.membership_ID = Table1.membership_ID WHERE Table2.membership_ID = 1 ")
cursor.execute(query)

for (membership_ID, movies_Rented) in cursor:
    print("{} rented by {}".format(membership_ID,movies_Rented))

cursor.close()
cnx.close()


'''Result
Pirates of the Caribbean rented by Janet Jones
Clash of the Titans rented by Janet Jones
'''