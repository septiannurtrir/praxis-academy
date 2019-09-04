import mysql.connector

cnx = mysql.connector.connect(user='septiannurtrir', password='sandaljebatds07',
                              host='127.0.0.1',
                              database='siswa') #jejeDB dibuat manual, tapi ngga dilihatin di dokumentasi ini
cnx.close()