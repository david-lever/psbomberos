from django.db import models

# Create your models here.


class Personal(models.Model):
    rut = models.IntegerField(primary_key=True, unique=True, verbose_name='Rut')
    dv = models.CharField(max_length=1, verbose_name='Dígito verificador')
    pnombre = models.CharField(max_length=25, verbose_name='Primer nombre')
    snombre = models.CharField(null=True, blank=True, max_length=25, verbose_name='Segundo nombre')
    appaterno = models.CharField(max_length=25, verbose_name='Apellido paterno')
    apmaterno = models.CharField(max_length=25, verbose_name='Apellido materno')
    fono = models.IntegerField(verbose_name='Teléfono')
    email = models.EmailField(verbose_name='Email')
    fecha_ing = models.DateField(verbose_name='Fecha Ingreso')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    compania = models.ForeignKey(Compania, on_delete=models.CASCADE)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)


def __str__(self):
    rut_per = self.rut+"-"+self.dv
    return rut_per


class Cargo(models.Model):
    nom_cargo = models.CharField(max_length=30, verbose_name='Nombre Cargo')


def __str__(self):
    return self.nom_cargo


class Compania(models.Model):
    nom_comp = models.CharField(max_length=35, verbose_name='Nombre Compañía')


def __str__(self):
    return self.nom_comp


class Comuna(models.Model):
    nom_com = models.CharField(max_length=20, verbose_name='Nombre Comuna')
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)


def __str__(self):
    return self.nom_com


class Provincia(models.Model):
    nom_prov = models.CharField(max_length=20, verbose_name='Nombre Provincia')
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


def __str__(self):
    return self.nom_prov


class Region(models.Model):
    nom_reg = models.CharField(max_length=20, verbose_name='Nombre Región')


def __str__(self):
    return self.nom_reg

