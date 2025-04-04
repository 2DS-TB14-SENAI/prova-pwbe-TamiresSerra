from django.db import models

CATEGORIAS = [
    ('CL', 'Clínico Geral'),
    ('CD', 'Cardiologista'),
    ('NE', 'Neurologista'),
    ('OR', 'Ortopedista'),
]

STATUS_CONSULTA = [
    ('AG', 'Agendado'),
    ('DM', 'Desmarcado'),
    ('DI', 'Disponível'),
    ('ND', 'Não disponível'),
    ('RE', 'Realizado'),
    ('CA', 'Cancelado'),
]

class Medicos(models.Model):
    nome = models.CharField(max_length=150)
    especialidade = models.CharField(max_length=2, choices=CATEGORIAS)
    crm = models.CharField(max_length=100, unique=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.get_especialidade_display()})"

class Consulta(models.Model):  
    paciente = models.CharField(max_length=150)
    data = models.DateTimeField()  
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)  
    status = models.CharField(max_length=2, choices=STATUS_CONSULTA)  

    def __str__(self):
        return f"Consulta de {self.paciente} com {self.medico.nome} em {self.data.strftime('%d/%m/%Y %H:%M')}"
