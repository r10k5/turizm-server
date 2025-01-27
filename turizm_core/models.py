from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Address(models.Model):
    strana = models.CharField(max_length=100)
    gorod = models.CharField(max_length=255)

    class Meta:
        unique_together = ('strana', 'gorod')

    def __str__(self):
        return f"{self.strana}, {self.gorod}"

class Role(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    opisanie = models.TextField()

    def __str__(self):
        return f"{self.id} ({self.opisanie:.50})"

class Zagranpasport(models.Model):
    nomer = models.IntegerField()
    data_vidachi = models.DateField()
    organ_vidachi = models.CharField(max_length=255)
    data_okonchania = models.DateField()
    scan_zagranpasporta = models.ImageField(upload_to="zagranpasports")

    def __str__(self):
        return f"Загранпаспорт №{self.nomer} от {self.data_vidachi.strftime('%d.%m.%Y')}"

    @property
    def kem_kogda_vydan(self):
        return f"{self.data_vidachi.strftime('%d.%m.%Y')} {self.organ_vidachi}"
    
    @property
    def data_okonchania_formated(self):
        return self.data_okonchania.strftime('%d.%m.%Y')

class Pasport(models.Model):
    data_rojdenia = models.DateField()
    seria = models.IntegerField()
    nomer = models.IntegerField()
    data_vidachi = models.DateField()
    organ_vidachi = models.CharField(max_length=255)
    scan_pasporta = models.ImageField(upload_to="pasports")

    def __str__(self):
        return f"Паспорт {self.seria_nomer}"
    
    @property
    def data_rojdenia_formated(self):
        return self.data_rojdenia.strftime('%d.%m.%Y')
    
    @property
    def seria_nomer(self):
        return f"{self.seria} {self.nomer}"
    
    @property
    def kem_kogda_vydan(self):
        return f"{self.data_vidachi.strftime('%d.%m.%Y')} {self.organ_vidachi}"

class Otel(models.Model):
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    nazvanie = models.CharField(max_length=100)
    opisanie = models.TextField()
    kolichestvo_zvezd = models.IntegerField()
    osobennosti = models.TextField()
    photo = models.ImageField(upload_to="otels")

    def __str__(self):
        return f"{self.nazvanie}"

class DannieAutorizatsii(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    nomer_telephona =  models.CharField(max_length=15, unique=True)
    rabochiy_nomer_telephona = models.CharField(max_length=15, null=True, default=None)
    rabochiy_emale = models.CharField(max_length=255, null=True, default=None)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.username} ({self.role.id})"

class Turoperator(models.Model):
    dannie_autorizatsii = models.ForeignKey(DannieAutorizatsii, on_delete=models.CASCADE)
    inn = models.CharField(max_length=20)
    kpp = models.CharField(max_length=20)
    nazvanie_companii = models.CharField(max_length=255)

    def __str__(self):
        return f"Туроператор {self.dannie_autorizatsii.username} ({self.nazvanie_companii})"

class Polzovatel(models.Model):
    familia = models.CharField(max_length=100)
    imya = models.CharField(max_length=100)
    otchestvo = models.CharField(max_length=100)
    dannie_autorizatsii = models.ForeignKey(DannieAutorizatsii, on_delete=models.SET_NULL, null=True, default=None)
    pasport = models.ForeignKey(Pasport, null=True, on_delete=models.SET_NULL, default=None)
    zagranpasport = models.ForeignKey(Zagranpasport, null=True, on_delete=models.SET_NULL, default=None)
    data_registatsii = models.DateField(auto_now_add=True)


    @property
    def fio(self):
        return f"{self.imya} {self.familia} {self.otchestvo}"

    def __str__(self):
        return f"Пользователь {self.fio}"

class Putevka(models.Model):
    turoperator = models.ForeignKey(Turoperator, on_delete=models.CASCADE)
    otel = models.ForeignKey(Otel, on_delete=models.CASCADE)
    data_vremya_otpravlenia = models.DateTimeField()
    data_vremya_vozvrashenia = models.DateTimeField()
    stoimost = models.IntegerField()
    data_vremya_zaselenia = models.DateTimeField()
    data_vremya_viselenia = models.DateTimeField()

    def __str__(self):
        return f"Путёвка с {self.data_vremya_otpravlenia.strftime('%d.%m.%Y')} до {self.data_vremya_vozvrashenia.strftime('%d.%m.%Y')} ({self.turoperator})"

    @property
    def data_otpravlenia_formated(self):
        return self.data_vremya_otpravlenia.strftime('%d.%m.%Y %H:%M')

    @property
    def data_vozvrashenia_formated(self):
        return self.data_vremya_vozvrashenia.strftime('%d.%m.%Y %H:%M')

    @property
    def data_zaselenia_formated(self):
        return self.data_vremya_zaselenia.strftime('%d.%m.%Y %H:%M')

    @property
    def data_viselenia_formated(self):
        return self.data_vremya_viselenia.strftime('%d.%m.%Y %H:%M')
    
    @property
    def stoimost_formated(self):
        return f"{self.stoimost:,} ₽".replace(",", " ")

STATUSY_ZAKAZA = {
    0: "В обработке менеджером",
    1: "Ожидает документы", 
    2: "Ожидает подтверждения туроператора",
    3: "Ожидает оплаты",
    4: "Подтверждён",
    5: "Услуга оказана",
    6: "Отменён"
}

class Zakaz(models.Model):
    putevka = models.ForeignKey(Putevka, on_delete=models.CASCADE)
    data_sozdania = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    dop_info = models.TextField(default="")
    manager = models.ForeignKey(Polzovatel, on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return f"Заказ №{self.id} от {self.data_sozdania_formated}"

    @property
    def data_sozdania_formated(self):
        return self.data_sozdania.strftime('%d.%m.%Y')
    
    @property
    def status_formated(self):
        if self.status in STATUSY_ZAKAZA:
            return STATUSY_ZAKAZA[self.status]
        else:
            return "Неизвестно"

class ZakazPolzovatel(models.Model):
    zakaz = models.ForeignKey(Zakaz, on_delete=models.CASCADE)
    polzovatel = models.ForeignKey(Polzovatel, on_delete=models.CASCADE)
    scan_dogovora = models.ImageField(upload_to="dogovors")
    nomer_bileta_tuda = models.CharField(max_length=100)
    nomer_bileta_obratno = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.zakaz} пользователя {self.polzovatel.fio}"