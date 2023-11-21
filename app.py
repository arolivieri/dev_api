from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)

desenvolvedores = [
    {'id': '0',
     'nome': 'Artur',
     'habilidades': ['SQL', 'SAS']
     },
     {'id': '1',
         'nome': 'Olivieri',
      'habilidades': ['Flask', 'PBI']
      }
    ]

# devolve um desenvolvedor pelo Id, tb altera e deleta
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'desenvlovedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'erro desconhecido, procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'registro excluído'})
    
# lista todos os desenvolvedores e inclui novos desenvolvedores
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)
    

if __name__ == '__main__':
    app.run(debug=True)
