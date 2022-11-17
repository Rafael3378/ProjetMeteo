import pymysql.cursors # j'importe la librairie pymysql pour avoir acces a ma base de donnees

def selectreleve(): # je cree une fonction qui selectionnera les releve de chaque capteur
    # Connexion a la base de données
    con = pymysql.connect(host='localhost', user="root", password="root", database='bloc2', port=8889)
    cur = con.cursor()
    # je stock ma requete sql dans une variable
    mareq = "SELECT * FROM Capteur JOIN Releve ON Capteur.ID_C = Releve.ID_C WHERE Capteur.ID_C "
    # j'execute ma requete
    cur.execute(mareq)
    # je stock mon resultat dans la variable result
    result = cur.fetchall()
    # je retourne la variable result
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


