# coding: utf-8

SEXO_CHOICES 		= (('M','Masculino'),('F','Feminino'))

EVASAO   = (
    ('D','Desviou'),
    ('V','VIAJOU'),
)
CATEGORIA_CHOICES   = (
	('N0','Novo Convertido'),
	('N1','Cursando-N1'),
    ('N2','Cursando-N2'),
    ('N3','Cursando-N3'),
    ('N4','Cursando-Trainee'),
    ('N5','Trainee Formado'),
	('LC','Lider de Célula'),
	('LG','Lider de Geração'),
	('PR','Pastores'),

)
ESCOLARIDADE = (
    ('ANF','Não Alfabetizado'),
    ('EFI','Ensino fundamental incompleto'),
    ('EFC','Ensino fundamental completo'),
    ('EMI','Ensino médio incompleto'),
    ('EMC','Ensino médio completo'),
    ('ESC','Superior completo'),
    ('PGC','Pós-Graduação'),
    ('MES','Mestrado'),
    ('DOT','Doutorado'),
)
UF = (
    ('', 'Estado'),
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MT', 'Mato Grosso'),
    ('MA', 'Maranhão'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RS', 'Rio Grande do Sul'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins'),
)

DIAS = (
    ('DM','Domingo'),
    ('SF','Segunda-feira '),
    ('TF','Terça-feira '),
    ('QF','Quarta-feira  '),
    ('QT','Quinta feira '),
    ('SF','sexta-feira'),
    ('SB','Sabado'),
)

#Fix Me corriger os labels pra 2 caracteres
CELULA_CHOICES      = (('H','Homens'),('M','Mulheres'),('J','Jovens'),('C','Moças'))