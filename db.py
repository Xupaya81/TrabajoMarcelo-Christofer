import mysql.connector
from mysql.connector import errorcode

def generar_conexion():
    """
    Genera una conexión a la base de datos MySQL.

    Returns:
        mysql.connector.connection.MySQLConnection: Objeto de conexión a la base de datos, 
                                                    o None si la conexión falla.
    """
    config = {
        'user': 'root',
        'password': '',
        'host': 'localhost',
        'database': 'gestion_empleados'  # Nombre de la base de datos
    }
    try:
        conexion = mysql.connector.connect(**config)
        if conexion.is_connected():
            print("Conexión a la base de datos establecida correctamente.")
            return conexion
        else:
            print("No se pudo conectar a la base de datos.")
            return None
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Acceso denegado para el usuario o la contraseña.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no existe.")
        else:
            print(f"Error de conexión: {err}")
        return None