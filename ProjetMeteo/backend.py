import pymysql.cursors

def selectreleve():
    # Connexion a la base de données
    con = pymysql.connect(host='localhost', user="root", password="root", database='bloc2', port=8889)
    cur = con.cursor()
    mareq = "SELECT * FROM Capteur JOIN Releve ON Capteur.ID_C = Releve.ID_C WHERE Capteur.ID_C "
    cur.execute(mareq)
    result = cur.fetchall()
    return result

def select():
    con = pymysql.connect(host='localhost', user="root", password="root", database='bloc2', port=8889)
    cur = con.cursor()
    mareq = "SELECT * FROM `Capteur` "
    cur.execute(mareq)
    result = cur.fetchall()
    return result


# def selectcapteur():
#     con = pymysql.connect(host='localhost', user="root", password="root", database='bloc2', port=8889)
#     cur = con.cursor()
#     mareq = "SELECT ID_C from `Capteur` "
#     cur.execute(mareq)
#     result = cur.fetchall()
#
#     for capteur in result:
#         id_c = capteur[0]
#     return id_c


