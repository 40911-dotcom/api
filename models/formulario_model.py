import sqlite3 
from database.db import get_db_connection  

class FormularioModel:
    
    @staticmethod
    def create_formulario(user_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection()  
        try:
            conn.execute('''INSERT INTO formularios (user_id, nome, email, data_nascimento, cpf, genero)
                             VALUES (?, ?, ?, ?, ?, ?)''', 
                         (user_id, nome, email, data_nascimento, cpf, genero))
            conn.commit()  
            return True  
        except sqlite3.IntegrityError:
            return None  
        finally:
            conn.close()  

    @staticmethod
    def get_formularios(user_id):
        conn = get_db_connection()
        formularios = conn.execute(
            'SELECT * FROM formulario WHERE user_id = ?', (user_id,)
        ).fetchall()
        conn.close()
        return formularios

    @staticmethod
    def get_formulario_by_id(user_id, formulario_id):
        conn = get_db_connection()
        formulario = conn.execute(
            'SELECT * FROM formulario WHERE id = ? AND user = ?',
            (formulario_id, user_id)
        ).fetchall()
        conn.close()
        return formulario

    @staticmethod
    def update_formulario(user_id, formulario_id, nome, email, data_nascimento, cpf, genero):
        conn = get_db_connection
        try:
            resultado = conn.execute(
                '''UPDATE formularios
                    SET nome = ?, email = ?, data_nascimento = ?, cpf = ?, genero = ?
                    WHERE id = ? AND user_id = ?''',
                    (nome, email, data_nascimento, cpf, genero, formulario_id, user_id)
            )
            conn.commit()
            return resultado.rowcount
        finally:
            conn.close()

    @staticmethod
    def delete_formulario(user_id, formulario_id):
        conn = get_db_connection()
        try:
            resultado = conn.execute(
                'DELETE FROM  formularios WHERE id = ? AND user_id = ?',
                (formulario_id, user_id)
            )
            conn.commit()
            return resultado.rowcount 
        finally:
            conn.close()


