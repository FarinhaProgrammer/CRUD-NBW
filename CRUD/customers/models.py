from django.db import models

class Customer(models.Model):
    """
    Modelo de empresa/cliente, com suas respectivas informações.
    A chave primária (primary key) é adicionada automaticamente pelo Django, e se chama "id".
    O padrão para nulo é falso.
    """

    CHOICES = (
        ('AC', 'Acre',),
        ('AL', 'Alagoas',),
        ('AP', 'Amapá',),
        ('AM', 'Amazonas',),
        ('BH', 'Bahia',),
        ('CE', 'Ceará',),
        ('ES', 'Espírito Santo',),
        ('GO', 'Goiás',),
        ('MA', 'Maranhão',),
        ('MT', 'Mato Grosso',),
        ('MS', 'Mato Grosso do Sul',),
        ('MG', 'Minas Gerais',),
        ('PA', 'Pará',),
        ('PB', 'Paraíba',),
        ('PR', 'Paraná',),
        ('PE', 'Pernambuco',),
        ('PI', 'Piauí',),
        ('RJ', 'Rio de Janeiro',),
        ('RN', 'Rio Grande do Norte',),
        ('RS', 'Rio Grande do Sul',),
        ('RO', 'Rondônia',),
        ('RR', 'Roraima',),
        ('SC', 'Santa Catarina',),
        ('SP', 'São Paulo',),
        ('SE', 'Sergipe',),
        ('TO', 'Tocantins',),
        ('DF', 'Distrito Federal',),)

    name                    = models.CharField(max_length=250, verbose_name="Nome")
    operation               = models.CharField(max_length=70, null=True, blank=True, verbose_name="Operação")
    cnpj                    = models.CharField(max_length=14, verbose_name="CNPJ")
    employees               = models.IntegerField(null=True, blank=True, verbose_name="Funcionários")
    billing                 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Faturamento")
    phone                   = models.CharField(max_length=20, null=True, blank=True, verbose_name="Telefone")
    mobile                  = models.CharField(max_length=20, verbose_name="Celular")
    adress                  = models.CharField(max_length=250, null=True, blank=True, verbose_name="Endereço")
    district                = models.CharField(max_length=100, null=True, blank=True, verbose_name="Bairro")
    city                    = models.CharField(max_length=100, null=True, blank=True, verbose_name="Cidade")
    state                   = models.CharField(max_length=2, choices=CHOICES, null=True, blank=True)
    zip_code                = models.CharField(max_length=8, null=True, blank=True, verbose_name="Código Postal")

    def __str__(self):
        return self.name