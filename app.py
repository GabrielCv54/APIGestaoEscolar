from flask import Flask, jsonify, request

app = Flask(__name__)

alunos = [
    {
        'id': 1,
        'nome': 'João',
        'idade': 18,
        'turma_id': 101,
        'data_nascimento': '2007-03-15',
        'nota_primeiro_semestre': 7.5,
        'nota_segundo_semestre': 8.0,
        'media_final': 7.75
    },
    {
        'id': 2,
        'nome': 'Maria',
        'idade': 17,
        'turma_id': 102, 
        'nota_primeiro_semestre': 8.0,
        'nota_segundo_semestre': 7.5,
        'media_final': 7.75
    },
    {
        'id': 3,
        'nome': 'José',
        'idade': 19,
        'turma_id': 103,
        'nota_primeiro_semestre': 6.0,
        'nota_segundo_semestre': 5.5,
        'media_final': 5.75
    },
    {
        'id': 4,
        'nome': 'Ana',
        'idade': 18,
        'turma_id': 104,
        'nota_primeiro_semestre': 9.0,
        'nota_segundo_semestre': 8.5,
        'media_final': 8.75
    }
]

professores = [
    {
        'id': 1,
        'nome': 'Diego',
        'idade': 46,
        'materia': 'Geografia',
        'observacoes': 'Tende a usar métodos interativos e debates em sala de aula.'
    },
    {
        'id': 2,
        'nome': 'Marcelo',
        'idade': 62,
        'materia': 'Física',
        'observacoes': 'Profissional com 10 anos de experiência no ensino de Física'
    },
    {
        'id': 3,
        'nome': 'Luiza',
        'idade': 55,
        'materia': 'Português',
        'observacoes': 'Excelente em gerenciar turmas e motivar os alunos.'
    },
    {
        'id': 4,
        'nome': 'Vanessa',
        'idade': 32,
        'materia': 'Matemática',
        'observacoes': 'Excelente em gerenciar turmas e motivar os alunos.'
    }
]

turmas = [
    {
        'id': 101,
        'descricao': 'Turma de Geografia - 1º Ano',
        'professor_id': 1,  
        'ativo': True
    },
    {
        'id': 102,
        'descricao': 'Turma de Matemática - 2º Ano',
        'professor_id': 4,  
        'ativo': True
    },
    {
        'id': 103,
        'descricao': 'Turma de Física - 3º Ano',
        'professor_id': 2,  
        'ativo': False 
    },
    {
        'id': 104,
        'descricao': 'Turma de Português - 1º Ano',
        'professor_id': 3, 
        'ativo': True
    }
]


# Consulta todos os alunos
@app.route('/alunos', methods=['GET'])
def getAlunos():
    return jsonify(alunos)

# Consulta aluno por id
@app.route('/alunos/<int:idAluno>', methods=['GET'])
def getAluno(idAluno):
    for aluno in alunos:
        if aluno.get('id') == idAluno:
            return jsonify(aluno)
    return jsonify('Aluno não encontrado')

# Adiciona um novo aluno
@app.route('/alunos', methods=['POST'])
def createAluno():
    dados = request.get_json()
    alunos.append(dados)
    return jsonify(dados)

# Atualiza o aluno por id
@app.route('/alunos/<int:idAluno>', methods=['PUT'])
def updateAluno(idAluno):
    dados = request.get_json()
    for aluno in alunos:
        if aluno['id'] == idAluno:
            aluno['nome'] = dados.get('nome', aluno['nome'])
            aluno['idade'] = dados.get('idade', aluno['idade'])
            aluno['nota_primeiro_semestre'] = dados.get('nota_primeiro_semestre', aluno['nota_primeiro_semestre'])
            aluno['nota_segundo_semestre'] = dados.get('nota_segundo_semestre', aluno['nota_segundo_semestre'])
            aluno['media_final'] = dados.get('media_final', aluno['media_final'])
            return jsonify(aluno)
    return jsonify('Aluno não encontrado')

# Deleta o aluno por id
@app.route('/alunos/<int:idAluno>', methods=['DELETE'])
def deleteAluno(idAluno):
    for aluno in alunos:
        if aluno['id'] == idAluno:
            alunos.remove(aluno)  
            return jsonify('Aluno deletado com sucesso')
    return jsonify('Aluno não encontrado')

#deleta todos os alunos
@app.route('/alunos/delete_all', methods=['DELETE'])
def delete_Todos_Alunos():
    alunos.clear()  
    return jsonify('Todos os alunos foram deletados')


# Selecionar todos os professores
@app.route('/api/professores', methods=['GET'])
def getTodosProfessores():
    return jsonify(professores)

# Selecionar um professor pelo id
@app.route('/api/professores/<int:id>', methods=['GET'])
def getProfessor(id):
    for professor in professores:
        if professor.get('id') == id:
            return jsonify(professor)
    return jsonify('Professor não encontrado')

# Adicionar um novo professor
@app.route('/api/professores', methods=['POST'])
def add_professor():
    novo_professor = request.get_json()
    professores.append(novo_professor)
    return jsonify(novo_professor)

# Atualizar um professor
@app.route('/api/professores/<int:id>', methods=['PUT'])
def update_professor(id):
    atualizado = request.get_json()
    for professor in professores:
        if professor.get('id') == id:
            professor.update(atualizado)  
            return jsonify(professor)
    return jsonify('Professor não encontrado')

# Deletar um professor
@app.route('/api/professores/<int:id>', methods=['DELETE'])
def delete_professor(id):
    for professor in professores:
        if professor.get('id') == id:
            professores.remove(professor) 
            return jsonify('Professor deletado com sucesso')
    return jsonify('Professor não encontrado')

#deleta todos os professores
@app.route('/api/professores/delete_all', methods=['DELETE'])
def delete_Todos_Professores():
    professores.clear() 
    return jsonify('Todos os professores foram deletados')

# Consultar todas as turmas
@app.route('/turmas', methods=['GET'])
def getTurmas():
    return jsonify(turmas)

# Consultar turma por ID
@app.route('/turmas/<int:idTurma>', methods=['GET'])
def getTurma(idTurma):
    for turma in turmas:
        if turma['id'] == idTurma:
            return jsonify(turma)
    return jsonify('Turma não encontrada')

# Adicionar uma nova turma
@app.route('/turmas', methods=['POST'])
def createTurma():
    dados = request.get_json()
    turmas.append(dados)
    return jsonify(dados)

# Atualizar uma turma por ID
@app.route('/turmas/<int:idTurma>', methods=['PUT'])
def updateTurma(idTurma):
    dados = request.get_json()
    for turma in turmas:
        if turma['id'] == idTurma:
            turma['descricao'] = dados.get('descricao', turma['descricao'])
            turma['professor_id'] = dados.get('professor_id', turma['professor_id'])
            turma['ativo'] = dados.get('ativo', turma['ativo'])
            return jsonify(turma)
    return jsonify('Turma não encontrada')

# Deletar uma turma por ID
@app.route('/turmas/<int:idTurma>', methods=['DELETE'])
def deleteTurma(idTurma):
    for turma in turmas:
        if turma['id'] == idTurma:
            turmas.remove(turma)  
            return jsonify('Turma deletada com sucesso')
    return jsonify('Turma não encontrada')

#deletar todas as turmas
@app.route('/turmas/delete_all', methods=['DELETE'])
def delete_Todas_turmas():
    turmas.clear()
    return jsonify('Todas as turmas foram deletadas')


if __name__ == '__main__':
    app.run(debug=True)