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
    nomer_telephona =  models.CharField(max_length=15, unique=True)
    rabochiy_nomer_telephona =  models.CharField(max_length=15, null=True)
    rabochiy_emale = models.CharField(max_length=255, null=True) 
    emale = models.CharField(max_length=255, unique=True)
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

class Putevka(models.Model):
    turoperator = models.ForeignKey(Turoperator, on_delete=models.CASCADE)
    otel = models.ForeignKey(Otel, on_delete=models.CASCADE)
    data_vremya_otpravlenia = models.DateTimeField()
    data_vremya_vozvrashenia = models.DateTimeField()
    stoimost = models.IntegerField()
    data_vremya_zaselenia = models.DateTimeField()
    data_vremya_viselenia = models.DateTimeField()

class Zakaz(models.Model):
    putevka = models.ForeignKey(Putevka, on_delete=models.CASCADE)
    data_sozdania = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    dop_info = models.TextField()

class ZakazPolzovatel(models.Model):
    zakaz = models.ForeignKey(Zakaz, on_delete=models.CASCADE)
    polzovatel = models.ForeignKey(Polzovatel, on_delete=models.CASCADE)
    scan_dogovora = models.TextField()
    nomer_bileta_tuda = models.CharField(max_length=100)
    nomer_bileta_obratno = models.CharField(max_length=100)