from django.db import models

class RolUic (models.Model):
    rol = models.CharField(max_length=70)

class Estudiante (models.Model):
    name = models.CharField(max_length=80)
    card_indentification = models.IntegerField()
    date_of_bird = models.DateField(auto_now=False, auto_now_add=False)
    email = models.CharField(max_length=100)
    cellphone = models.IntegerField()
    gender = models.CharField(max_length=60)
    civil_status = models.CharField(max_length=60)
    ethnicity = models.CharField(max_length=60)
    country  = models.CharField(max_length=60)
    career = models.CharField(max_length=60)
    tipo = models.ForeignKey(RolUic, on_delete=models.PROTECT)
    
# class Persona (models.Model):
#     nombre = models.CharField(max_lenght=80)
#     cedula = models.IntegerField()
#     fecha_nacimieno = models.DateField(auto_now=False, auto_now_add=False)
#     email = models.CharField(max_length=100)
#     cellphone = models.IntegerField()
#     gender = models.CharField(max_length=60)
#     civil_status = models.CharField(max_lenght=60)
#     ethnicity = models.CharField(max_lenght=60)
#     country  = models.CharField(max_length=60) 