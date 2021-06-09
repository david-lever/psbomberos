from django.db import models

# Create your models here.

#COMPAÑIA DE BOMBERO
class Compania(models.Model):
    idCompania = models.IntegerField(primary_key=True, verbose_name='ID Compañia')
    nomComp = models.CharField(max_length=35, verbose_name='Nombre Compañía')

    def __str__(self):
        return self.nomComp


#CARGO DE BOMBERO
class Cargo(models.Model):
    idCargo = models.CharField(max_length=3,primary_key=True, verbose_name='ID Cargo')
    nomCargo = models.CharField(max_length=30, verbose_name='Nombre Cargo')
    def __str__(self):
        return self.nomCargo


#COMUNA
class Comuna(models.Model):
    idComuna = models.CharField(max_length=3,primary_key=True, verbose_name='ID Comuna')
    nomCom = models.CharField(max_length=20, verbose_name='Nombre Comuna')

    def __str__(self):
        return self.nomCom


#PERONAL - BOMBEROS
class Personal(models.Model):
    rut = models.IntegerField(primary_key=True, verbose_name='Rut')
    dv = models.CharField(max_length=1, verbose_name='Dígito verificador')
    pnombre = models.CharField(max_length=25, verbose_name='Primer nombre')
    snombre = models.CharField(null=True, blank=True, max_length=25, verbose_name='Segundo nombre')
    appaterno = models.CharField(max_length=25, verbose_name='Apellido paterno')
    apmaterno = models.CharField(max_length=25, verbose_name='Apellido materno')
    fono = models.IntegerField(verbose_name='Teléfono')
    fecha_ing = models.DateField(verbose_name='Fecha Ingreso')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    compania = models.ForeignKey(Compania, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)

    def __str__(self):
        return self.pnombre + " " + self.snombre + " " + self.appaterno + " " + self.apmaterno
