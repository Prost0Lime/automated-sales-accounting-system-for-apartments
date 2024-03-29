# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from dbview.models import DbView
from django.db.models.signals import post_delete, post_save
from django.utils.safestring import mark_safe


class Client(models.Model):
    kod_client = models.AutoField(primary_key=True, verbose_name="Код клиента")
    pasp = models.CharField(max_length=40, verbose_name="Паспорт")
    fio_client = models.CharField(max_length=70, verbose_name="ФИО")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    status = models.CharField(max_length=20, verbose_name="Статус")

    def __str__(self):
        return "{kod_client}".format(kod_client=self.kod_client)

    class Meta:
        managed = False
        db_table = 'client'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class DogovorProd(models.Model):
    readonly_fields = ("sum_dog",)
    id_dog = models.AutoField(primary_key=True, verbose_name="ИД договора")
    num_dog = models.IntegerField(verbose_name="Номер договора")
    date_sost = models.DateField(verbose_name="Дата составления")
    date_prod = models.DateField(verbose_name="Дата продажи")
    sum_dog = models.DecimalField(max_digits=9, decimal_places=2, default=0, blank=True,
                                  verbose_name="Сумма по договору")
    opl = models.DecimalField(max_digits=9, decimal_places=2, default=0, blank=True,
                              verbose_name="Оплачено по договору")
    id_zaya = models.ForeignKey('Zayavka', models.CASCADE, db_column='id_zaya', verbose_name="ИД заявки",
                                related_name='dogovors')
    kod_sotrudn = models.ForeignKey('Sotrudn', models.CASCADE,
                                    db_column='kod_sotrudn', verbose_name="Код сотрудника",
                                    related_name='dogovors')

    def __str__(self):
        return "{id_dog}".format(id_dog=self.id_dog)

    class Meta:
        managed = False
        db_table = 'dogovor_prod'
        verbose_name = 'Договор продажи'
        verbose_name_plural = 'Договоры продаж'


class KategKvart(models.Model):
    kod_kategorii = models.IntegerField(primary_key=True, verbose_name="Код категории")
    naim_kat = models.CharField(max_length=50, verbose_name="Наименование")

    def __str__(self):
        return "{kod_kategorii}".format(kod_kategorii=self.kod_kategorii)

    class Meta:
        managed = False
        db_table = 'kateg_kvart'
        verbose_name = 'Категория квартир'
        verbose_name_plural = 'Категории квартир'


class KnOplat(models.Model):
    id_oplt = models.AutoField(primary_key=True, verbose_name="ИД оплаты")
    date_opl = models.DateField(verbose_name="Дата оплаты")
    sum_opl = models.IntegerField(blank=True, null=True, verbose_name="Сумма оплаты")
    id_dog = models.ForeignKey(DogovorProd, models.CASCADE, db_column='id_dog', verbose_name="ИД договора",
                               related_name='oplaty')

    def __str__(self):
        return "{id_oplt}".format(id_oplt=self.id_oplt)

    class Meta:
        managed = False
        db_table = 'kn_oplat'
        verbose_name = 'Книга оплат'
        verbose_name_plural = 'Книга оплат'


# # Вычисляемые поля
# def calculate_sum_dogs(sender, instance: KnOplat, **kwargs):
#     dog = instance.id_dog
#     dog.opl = sum(instance.id_dog.oplaty.values_list('sum_opl', flat=True))
#     dog.save()
#
#
# post_save.connect(calculate_sum_dogs, sender=KnOplat)
# post_delete.connect(calculate_sum_dogs, sender=KnOplat)


class Kvart(models.Model):
    id_kv = models.AutoField(primary_key=True, verbose_name="ИД квартиры")
    num_etag = models.IntegerField(verbose_name="Номер этажа")
    num_kv = models.CharField(max_length=50, verbose_name="Номер квартиры")
    kol_vo_kom = models.IntegerField(blank=True, null=True, verbose_name="Кол-во комнат")
    area = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, verbose_name="Площадь")
    stoim = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, verbose_name="Стоимость")
    image = models.ImageField(blank=True, null=True, upload_to="images/", verbose_name='Изображение')
    num_obj = models.ForeignKey('ObjZastroi', models.CASCADE, db_column='num_obj', verbose_name="Номер объекта")
    kod_kategorii = models.ForeignKey(KategKvart, models.CASCADE, db_column='kod_kategorii',
                                      verbose_name="Код категории")

    # Вывод в админ панель изображения
    def image_img(self):
        if self.image:
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Изображение'
    image_img.allow_tags = True

    def __str__(self):
        return "{id_kv}".format(id_kv=self.id_kv)

    class Meta:
        managed = False
        db_table = 'kvart'
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'


class ObjZastroi(models.Model):
    num_obj = models.IntegerField(primary_key=True, verbose_name="Номер объекта")
    street = models.CharField(max_length=70, verbose_name="Улица")
    num_zd = models.CharField(max_length=20, verbose_name="Номер здания")
    kol_vo_et = models.IntegerField(verbose_name="Кол-во этажей")
    kod_vida = models.ForeignKey('VidJil', models.CASCADE, db_column='kod_vida', verbose_name="Код вида")
    trans_dos = models.CharField(max_length=100, verbose_name="Транспортная доступность")
    soc_infr = models.CharField(max_length=100, verbose_name="Социальная инфраструктура")
    rekreaciya = models.CharField(max_length=100, verbose_name="Рекреация")
    parkov = models.CharField(max_length=50, verbose_name="Парковочные места")

    def __str__(self):
        return "{num_obj}".format(num_obj=self.num_obj)

    class Meta:
        managed = False
        db_table = 'obj_zastroi'
        verbose_name = 'Объек застройки'
        verbose_name_plural = 'Объекты застройки'


class ProdKv(models.Model):
    id_prod = models.AutoField(primary_key=True, verbose_name="ИД продажи")
    id_dog = models.ForeignKey(DogovorProd, models.CASCADE, db_column='id_dog', verbose_name="ИД договора")

    def __str__(self):
        return "{id_prod}".format(id_prod=self.id_prod)

    class Meta:
        managed = False
        db_table = 'prod_kv'
        verbose_name = 'Проданная квартира'
        verbose_name_plural = 'Проданные квартиры'


class Sotrudn(models.Model):
    kod_sotrudn = models.IntegerField(primary_key=True, verbose_name="Код сотрудника")
    fio = models.CharField(max_length=90, verbose_name="ФИО")
    dolz = models.CharField(max_length=70, verbose_name="Должность")

    def __str__(self):
        return "{kod_sotrudn}".format(kod_sotrudn=self.kod_sotrudn)

    class Meta:
        managed = False
        db_table = 'sotrudn'
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class VidJil(models.Model):
    kod_vida = models.IntegerField(primary_key=True, verbose_name="Код вида")
    naim_jil = models.CharField(max_length=50, verbose_name="Наименование жилья")

    def __str__(self):
        return "{kod_vida}".format(kod_vida=self.kod_vida)

    class Meta:
        managed = False
        db_table = 'vid_jil'
        verbose_name = 'Вид жилья'
        verbose_name_plural = 'Виды жилья'


class Zayavka(models.Model):
    id_zaya = models.AutoField(primary_key=True, verbose_name="ИД заявки")
    data_zaya = models.DateField(verbose_name="Дата заполнения")
    id_kv = models.ForeignKey(Kvart, models.CASCADE, db_column='id_kv', verbose_name="ИД квартиры")
    kod_client = models.ForeignKey(Client, models.CASCADE, db_column='kod_client', verbose_name="Код клиента")
    kod_sotrudn = models.ForeignKey(Sotrudn, models.CASCADE, blank=True, null=True, db_column='kod_sotrudn',
                                    verbose_name="Код сотрудника")

    def __str__(self):
        return "{id_zaya}".format(id_zaya=self.id_zaya)

    class Meta:
        managed = False
        db_table = 'zayavka'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class KvartV(models.Model):
    id_kv = models.AutoField(primary_key=True)
    num_etag = models.IntegerField()
    num_kv = models.CharField(max_length=50)
    kol_vo_kom = models.IntegerField()
    area = models.DecimalField(max_digits=9, decimal_places=2)
    stoim = models.DecimalField(max_digits=9, decimal_places=2)
    image = models.ImageField(blank=True, null=True)
    num_obj = models.IntegerField()
    street = models.CharField(max_length=70)
    num_zd = models.CharField(max_length=20)
    kol_vo_et = models.IntegerField()
    trans_dos = models.CharField(max_length=100)
    soc_infr = models.CharField(max_length=100)
    rekreaciya = models.CharField(max_length=100)
    parkov = models.CharField(max_length=50)
    kod_kategorii = models.IntegerField()
    naim_kat = models.CharField(max_length=50)
    naim_jil = models.CharField(max_length=50)

    def __str__(self):
        return "{id_kv}".format(id_kv=self.id_kv)

    class Meta:
        managed = False
        db_table = "kvart_v"


class ZayavkaV(models.Model):
    id_zaya = models.AutoField(primary_key=True)
    data_zaya = models.DateField()
    street = models.CharField(max_length=50)
    num_zd = models.CharField(max_length=20)
    num_kv = models.IntegerField()
    stoim = models.DecimalField(max_digits=9, decimal_places=2)
    kod_client = models.IntegerField()
    fio_client = models.CharField(max_length=70)
    pasp = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)

    def __str__(self):
        return "{id_zaya}".format(id_kv=self.id_zaya)

    class Meta:
        managed = False
        db_table = "zayavka_v"
