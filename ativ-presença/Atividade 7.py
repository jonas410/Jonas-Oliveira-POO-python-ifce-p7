class aluno:
    def __init__(self, nome, telefone, matricula, listaula):
        self.nome = nome
        self.telefone = telefone
        self.matricula = matricula
        self.listaula = listaula

    def set_planodeaula(self, planodeaula):
        self.planodeaula = planodeaula

    def __int__(self, planodeaula):
        self.planodeaula = planodeaula

class horario:
    def set_horario(self, dia):
        self.dia = dia

    def set_hora(self, hora):
        self.hora = hora
    def __init__(self, dia, hora) :
        self.dia = dia
        self.hora = hora

class professor:
    def __init__(self, nome, especializacao, telefone, listaula):
        self.nome = nome
        self.especializacao = especializacao
        self.telefone = telefone
        self.listaula = listaula

class aula:
    def get_horario(self):
        return self.horario
    def get_professor(self):
        return self.professor
    def get_aluno(self):
        return self.aluno
