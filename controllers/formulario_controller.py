from models.formulario_model import FormularioModel 
from database import get_db_connection

class FormularioController:

    @staticmethod
    def create_formulario(user_id, data):
        nome = data.get('nome')  
        email = data.get('email') 
        data_nascimento = data.get('data_nascimento') 
        cpf = data.get('cpf')  
        genero = data.get('genero')  

        if not nome or not email or not data_nascimento or not cpf or not genero:
            return {"error": "Todos os campos são obrigatórios"}, 400  

        formulario = FormularioModel.create_formulario(user_id, nome, email, data_nascimento, cpf, genero)
        if formulario:
            return {"message": "Formulário criado com sucesso"}, 201
        return {"error": "Erro ao criar formulário"}, 500 


    @staticmethod
    def get_formularios(user_id):
        formularios = FormularioModel.get_formularios(user_id)
        return {"formularios": [dict(f) for f in formularios]}, 200


    @staticmethod
    def get_form_by_id(user_id, formulario_id):
        formulario = FormularioModel.get_formulario_by_id(user_id, formulario_id)
        if not formulario:
            return {"error": "Formulario não encontrado!"}, 400
        return {"formulario": dict(formulario)}, 200

    @staticmethod
    def update_formulario(user_id, formulario_id, data):
        nome = data.get('nome')  
        email = data.get('email') 
        data_nascimento = data.get('data_nascimento') 
        cpf = data.get('cpf')  
        genero = data.get('genero')

        if not nome or not email or not data_nascimento or not cpf or not genero: 
            return {"erro": "Todos os campos são obrigatórios"}, 400

        linhas = FormularioModel.update_formulario(user_id, formulario_id, nome, email, data_nascimento, cpf, genero)
        if linhas == 0:
            return {"erro": "Formulário não encontrado"}, 404
        return {"message": "Formulário atualizado com sucesso"}, 200

    @staticmethod
    def delete_formulario(user_id, formulario_id):
        linhas = FormularioModel.delete_formulario(user_id, formulario_id)
        if linhas == 0:
            return{"erro": "Formulário não encontrado!"}, 404
        return{"message": "Formulário encontrado com sucesso!"}, 200


