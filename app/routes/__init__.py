from flask import Blueprint, jsonify, request

bp_api = Blueprint("api", "api", url_prefix="/")
bp_auth = Blueprint("auth", "auth", url_prefix="/auth")

from . import cliente, clinica, consulta, horario, auth


#                STATUS CODE REFERENCE

#           Repostas de sucesso
## 200 OK Estas requisição foi bem sucedida.
## 201 CREATED indica que a requisição foi bem sucedida e que um novo recurso foi criado

#           Repostas de erro do cliente
## 400 BAD REQUEST Essa resposta significa que o servidor não entendeu a requisição pois está com uma sintaxe inválida.
## 404 NOT FOUND O servidor não encontra o recurso solicitado
## 422 UNPROCESSABLE ENTITY indica que o servidor entende o tipo de conteúdo da entidade da requisição, e a sintaxe da requisição esta correta, mas não foi possível processar as instruções presentes.

#           Respostas de erro do Servidor
## 500 INTERNAL SERVER ERROR O servidor encontrou uma situação com a qual não sabe lidar.


"""
                JSON RESPONSE FORMAT
 success:
 {"status": "success", data: {} | None}

 fail e error:
 {"status": "fail" | "error", "message": "problem message", "data": {"detail": {"key": "required" | "not found" | "invalid" | "unusable"}, "payload": {"request data"}}}

 ! Formato de resposta de error e fail é o mesmo para todos métodos

 POST JSON DATA RESPONSE

 {"status": "success", "data": {"consulta": {"new_consulta_data"}}}

 GET JSON DATA RESPONSE

 {"status": "success", "data": {"consultas": [{"consulta data"}, {"consulta data"}] | "consulta": {"new_consulta_data"}}}

 PUT JSON DATA RESPONSE

 {"status": "success", "data": {"consulta": {"updated_consulta_data"}}}

 DELETE JSON DATA RESPONSE

 {"status": "success", "data": None}

"""
