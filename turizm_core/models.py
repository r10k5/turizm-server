from django.db import models
from django.contrib.auth.models import AbstractUser

class Address(models.Model):
    strana = models.CharField(max_length=100)
    gorod = models.CharField(max_length=255)

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
        return f"Загранпаспорт №{self.nomer} от {self.data_vidachi.day}.{self.data_vidachi.month}.{self.data_vidachi.year}"

    @property
    def kem_kogda_vydan(self):
        kogda = f"{self.data_vidachi.day}.{self.data_vidachi.month}.{self.data_vidachi.year}"
        return f"{kogda} {self.organ_vidachi}"
    
    @property
    def data_okonchania_formated(self):
        return f"{self.data_okonchania.day}.{self.data_okonchania.month}.{self.data_okonchania.year}"

class Pasport(models.Model):
    familia = models.CharField(max_length=100)
    imya = models.CharField(max_length=100)
    otchestvo = models.CharField(max_length=100)
    data_rojdenia = models.DateField()
    seria = models.IntegerField()
    nomer = models.IntegerField()
    data_vidachi = models.DateField()
    organ_vidachi = models.CharField(max_length=255)
    scan_pasporta = models.ImageField(upload_to="pasports")

    def __str__(self):
        return f"{self.fio} {self.seria_nomer}"

    @property
    def fio(self):
        return f"{self.imya} {self.familia} {self.otchestvo}"
    
    @property
    def data_rojdenia_formated(self):
        return f"{self.data_rojdenia.day}.{self.data_rojdenia.month}.{self.data_rojdenia.year}"
    
    @property
    def seria_nomer(self):
        return f"{self.seria} {self.nomer}"
    
    @property
    def kem_kogda_vydan(self):
        kogda = f"{self.data_vidachi.day}.{self.data_vidachi.month}.{self.data_vidachi.year}"
        return f"{kogda} {self.organ_vidachi}"

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
    dannie_autorizatsii = models.ForeignKey(DannieAutorizatsii, on_delete=models.CASCADE)
    pasport = models.ForeignKey(Pasport, null=True, on_delete=models.SET_NULL, default=None)
    zagranpasport = models.ForeignKey(Zagranpasport, null=True, on_delete=models.SET_NULL, default=None)
    data_registatsii = models.DateField(auto_now_add=True)

    def __str__(self):
        fio = f" ({self.pasport.fio})" if self.pasport else ""
        return f"Пользователь {self.dannie_autorizatsii.username}{fio}"

class Putevka(models.Model):
    turoperator = models.ForeignKey(Turoperator, on_delete=models.CASCADE)
    otel = models.ForeignKey(Otel, on_delete=models.CASCADE)
    data_vremya_otpravlenia = models.DateTimeField()
    data_vremya_vozvrashenia = models.DateTimeField()
    stoimost = models.IntegerField()
    data_vremya_zaselenia = models.DateTimeField()
    data_vremya_viselenia = models.DateTimeField()

    def __str__(self):
        data_s = f"{self.data_vremya_otpravlenia.day}.{self.data_vremya_otpravlenia.month}.{self.data_vremya_otpravlenia.year}"
        data_do = f"{self.data_vremya_vozvrashenia.day}.{self.data_vremya_vozvrashenia.month}.{self.data_vremya_vozvrashenia.year}"
        return f"Путёвка с {data_s} до {data_do} ({self.turoperator})"

    @property
    def daty_reisov(self):
        data_s = f"{self.data_vremya_otpravlenia.day}.{self.data_vremya_otpravlenia.month}.{self.data_vremya_otpravlenia.year}"
        vremya_s = f"{self.data_vremya_otpravlenia.hour} ч. {self.data_vremya_otpravlenia.minute} мин."
        data_do = f"{self.data_vremya_vozvrashenia.day}.{self.data_vremya_vozvrashenia.month}.{self.data_vremya_vozvrashenia.year}"
        vremya_do = f"{self.data_vremya_vozvrashenia.hour} ч. {self.data_vremya_vozvrashenia.minute} мин."

        return f"Отправление: {data_s} {vremya_s} Возвращение: {data_do} {vremya_do}"
    
    @property
    def otel_period(self):
        data_s = f"{self.data_vremya_zaselenia.day}.{self.data_vremya_zaselenia.month}.{self.data_vremya_zaselenia.year}"
        vremya_s = f"{self.data_vremya_zaselenia.hour} ч. {self.data_vremya_zaselenia.minute} мин."
        data_do = f"{self.data_vremya_viselenia.day}.{self.data_vremya_viselenia.month}.{self.data_vremya_viselenia.year}"
        vremya_do = f"{self.data_vremya_viselenia.hour} ч. {self.data_vremya_viselenia.minute} мин."

        return f"Заселение: {data_s} {vremya_s} Выселение: {data_do} {vremya_do}"

STATUSY_ZAKAZA = [
    "В обработке менеджером",
    "Ожидает документы",
    "Ожидает подтверждения туроператора",
    "Ожидает оплаты",
    "Подтверждён",
    "Услуга оказана",
    "Отменён"
]

class Zakaz(models.Model):
    putevka = models.ForeignKey(Putevka, on_delete=models.CASCADE)
    data_sozdania = models.DateField(auto_now_add=True)
    status = models.IntegerField()
    dop_info = models.TextField(default="")

    def __str__(self):
        return f"Заказ №{self.id} от {self.data_sozdania_formated}"

    @property
    def data_sozdania_formated(self):
        return f"{self.data_sozdania.day}.{self.data_sozdania.month}.{self.data_sozdania.year}"
    
    @property
    def status_formated(self):
        if self.status > len(STATUSY_ZAKAZA) - 1:
            return "Неизвестно"
        
        return STATUSY_ZAKAZA[self.status]

class ZakazPolzovatel(models.Model):
    zakaz = models.ForeignKey(Zakaz, on_delete=models.CASCADE)
    polzovatel = models.ForeignKey(Polzovatel, on_delete=models.CASCADE)
    scan_dogovora = models.ImageField(upload_to="dogovors")
    nomer_bileta_tuda = models.CharField(max_length=100)
    nomer_bileta_obratno = models.CharField(max_length=100)

    def __str__(self):
        if self.polzovatel.pasport:
            imya_polzovatelya = self.polzovatel.pasport.fio
        else:
            imya_polzovatelya = self.polzovatel.dannie_autorizatsii.username
        return f"{self.zakaz} пользователя {imya_polzovatelya}"