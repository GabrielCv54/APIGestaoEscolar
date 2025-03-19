import requests
import unittest

class TestStringMethods(unittest.TestCase):


    def test_000_alunos_retorna_lista(self):
        #pega a url /alunos, com o verbo get
        r = requests.get('http://localhost:5002/alunos')

        #o status code foi pagina nao encontrada?
        if r.status_code == 404:
            self.fail("voce nao definiu a pagina /alunos no seu server")

        try:
            obj_retornado = r.json()
            #r.json() é o jeito da biblioteca requests
            #de pegar o arquivo que veio e transformar
            #em lista ou dicionario.
            #Vou dar erro se isso nao for possivel
        except:
            self.fail("queria um json mas voce retornou outra coisa")

        #no caso, tem que ser uma lista
        self.assertEqual(type(obj_retornado),type([]))

    def test_002_aluno_por_id(self):
        #cria um aluno 'mario', com id 20
        r = requests.post('http://localhost:5002/alunos',json={'nome':'mario','id':20})

        #consulta a url /alunos/20, pra ver se o aluno está lá
        resposta = requests.get('http://localhost:5002/alunos/20')
        dict_retornado = resposta.json() #pego o dicionario retornado
        self.assertEqual(type(dict_retornado),dict)
        self.assertIn('nome',dict_retornado)#o dicionario dict_retornado, que veio do servidor, 
        #tem que ter a chave nome
        self.assertEqual(dict_retornado['nome'],'mario') # no dic, o nome tem que ser o 
                                                   # que eu mandei
                                                   # tem que ser mario


    #adiciona um aluno, mas depois reseta o servidor
    #e o aluno deve desaparecer