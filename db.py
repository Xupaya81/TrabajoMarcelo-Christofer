import mysql.connector
from mysql.connector import errorcode

def generar_conexion():
    config={
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'trabajo_Marcelo-Christofer'
    }
    try:
        conexion = mysql.connector.connect(**config)
        if conexion and conexion.is_connected():
            cursor = conexion.cursor()
            cursor.execute()
            cursor.execute(cursor)
            if cursor != None:
                for registro in cursor:
                    print(registro)
                    
                    # for (first_name, last_name, hire_date) in cursor:
                    #     print("{}, {} was hired on {:%d %b %Y}".format(
                    #         last_name, first_name, hire_date))

                cursor.close()
            else:
                print("Su búsqueda no arrojó resultados...")
            conexion.close()
        else:
            print("Could not connect")
    
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Acceso denegado para el usuario o la contraseña")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Su base de datos NO existe")
        else:
            print(error)
    else:
        conexion.close()