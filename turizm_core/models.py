from django.db import models

class Address(models.Model):
    strana = models.CharField(max_length=100)
    gorod = models.CharField(max_length=255)

class Role(models.Model):
    opisanie = models.TextField()

class Zagranpasport(models.Model):
    nomer = models.IntegerField()
    data_vidachi = models.DateField()
    organ_vidachi = models.CharField(max_length=255)
    data_okonchania = models.DateField()
    scan_zagranpasporta = models.CharField(max_length=255)

class Pasport(models.Model):
    familia = models.CharField(max_length=100)
    imya = models.CharField(max_length=100)
    otchestvo = models.CharField(max_length=100)
    data_rojdenia = models.DateField()
    seria = models.IntegerField()
    nomer = models.IntegerField()
    data_vidachi = models.DateField()
    organ_vidachi = models.CharField(max_length=255)
    scan_pasporta = models.CharField(max_length=255)

class Otel(models.Model):
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    nazvanie = models.CharField(max_length=100)
    opisanie = models.TextField()
    kolichestvo_zvezd = models.IntegerField()
    osobennosti = models.TextField()
    photo = models.CharField(max_length=255)

class DannieAutorizatsii(models.Model):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    nomer_telephona =  models.CharField(max_length=15)
    rabochiy_nomer_telephona =  models.CharField(max_length=15, null=True)
    rabochiy_emale = models.CharField(max_length=255, null=True) 
    emale = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Turoperator(models.Model):
    dannie_autorizatsii = models.ForeignKey(DannieAutorizatsii, on_delete=models.CASCADE)
    inn = models.CharField(max_length=20)
    kpp = models.CharField(max_length=20)
    nazvanie_companii = models.CharField(max_length=255)

class Polzovatel(models.Model):
    dannie_autorizatsii = models.ForeignKey(DannieAutorizatsii, on_delete=models.CASCADE)
    pasport = models.ForeignKey(Pasport, null=True, on_delete=models.SET_NULL)
    zagranpasport = models.ForeignKey(Zagranpasport, null=True, on_delete=models.SET_NULL)
    data_registatsii = models.DateField(auto_now_add=True)
