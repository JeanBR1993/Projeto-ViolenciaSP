from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Delegacia(models.Model):

    nome = models.CharField(max_length=50)
    endereço = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Crime(models.Model):
    
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Mes(models.Model):

    #Está "Marco" primeiro porque as tabelas excel estão sem ç.
    MESES = (
        ("Janeiro","Janeiro"),
        ("Feveireiro","Feveireiro"),
        ("Marco", "Marco"),
        ("Abril","Abril"),
        ("Maio","Maio"),
        ("Junho","Junho"),
        ("Julho","Julho"),
        ("Agosto","Agosto"),
        ("Setembro","Setembro"),
        ("Outubro","Outubro"),
        ("Novembro","Novembro"),
        ("Dezembro","Dezembro")
    )


    nome = models.CharField(
        choices = MESES,
        max_length=20
    )

    def __str__(self):
        return self.nome



class DadosBoletim(models.Model):

    ano = models.IntegerField(
        validators=[
            MinValueValidator(2001),
            MaxValueValidator(2100)
        ]
    )

    mes = models.ForeignKey(Mes, on_delete=models.PROTECT)
    crime = models.ForeignKey(Crime, on_delete=models.PROTECT)
    delegacia = models.ForeignKey(Delegacia, on_delete=models.PROTECT)

    nCrimes = models.PositiveIntegerField()

    def __str__(self):
        return str(self.delegacia) + " - " + str(self.crime) + " - " + str(self.mes) + "/" +str(self.ano)

