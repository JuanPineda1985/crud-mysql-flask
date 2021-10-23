# importar el archivo de la conexión a la BD
from configdb import get_connection

def add_user(name,email,telefono,passwd):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("INSERT INTO user (name, email, telefono, passwd) VALUES (%s,%s,%s,%s)",(name,email,telefono,passwd))
    cnn.commit()
    cnn.close()

def update_user(name,email,telefono,passwd,id):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("UPDATE user SET name = %s, email = %s, telefono = %s, passwd = %s WHERE id = %s",(name,email,telefono,passwd,id))
    cnn.commit()
    cnn.close()

def delete_user(id):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("DELETE FROM user WHERE id = %s",(id))
    cnn.commit()
    cnn.close()

def get_users():
    cnn = get_connection()
    users = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, email, telefono FROM user")
        users = cursor.fetchall()
    cnn.close()
    return users

def get_user_id(id):
    cnn = get_connection()
    user = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, email, telefono FROM user WHERE id = %s",(id))
        user = cursor.fetchone()
    cnn.close
    return user
