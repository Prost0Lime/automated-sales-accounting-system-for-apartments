# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Client(models.Model):
    kod_client = models.IntegerField(primary_key=True,  verbose_name= "Код клиента")
    pasp = models.CharField(max_length=40, verbose_name= "Паспорт")
    fio_sotr = models.CharField(max_length=70, verbose_name= "ФИО")
    phone = models.CharField(max_length=50, verbose_name= "Телефон")
    status = models.CharField(max_length=20, verbose_name= "Статус")

    def __str__(self):
        return "<Client {kod_client}>".format(kod_client=self.kod_client)

    class Meta:
        managed = False
        db_table = 'client'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class DogovorProd(models.Model):
    id_dog = models.AutoField(primary_key=True, verbose_name= "ИД договора")
    num_dog = models.IntegerField(verbose_name= "Номер договора")
    date_sost = models.DateField(verbose_name= "Дата составления")
    date_prod = models.DateField(verbose_name= "Дата продажи")
    sum_dog = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, verbose_name= "Сумма по договору")
    opl = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True, verbose_name= "Оплачено по договору")
    id_zaya = models.ForeignKey('Zayavka', models.CASCADE, db_column='id_zaya', verbose_name= "ИД заявки")
    kod_sotrudn = models.ForeignKey('Sotrudn', models.CASCADE, db_column='kod_sotrudn', verbose_name= "Код сотрудника")

    class Meta:
        managed = False
        db_table = 'dogovor_prod'
        verbose_name = 'Договор продажи'
        verbose_name_plural = 'Договоры продаж'

class KategKvart(models.Model):
    kod_kategorii = models.IntegerField(primary_key=True)
    naim_kat = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'kateg_kvart'


class KnOplat(models.Model):
    id_oplt = models.AutoField(primary_key=True)
    date_opl = models.DateField()
    sum_opl = models.IntegerField(blank=True, null=True)
    id_dog = models.ForeignKey(DogovorProd, models.DO_NOTHING, db_column='id_dog')

    class Meta:
        managed = False
        db_table = 'kn_oplat'


class Kvart(models.Model):
    id_kv = models.AutoField(primary_key=True)
    num_etag = models.IntegerField()
    num_kv = models.CharField(max_length=50)
    kol_vo_kom = models.IntegerField(blank=True, null=True)
    area = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    stoim = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    num_obj = models.ForeignKey('ObjZastroi', models.DO_NOTHING, db_column='num_obj')
    kod_kategorii = models.ForeignKey(KategKvart, models.DO_NOTHING, db_column='kod_kategorii')

    class Meta:
        managed = False
        db_table = 'kvart'


class ObjZastroi(models.Model):
    num_obj = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=70)
    num_zd = models.CharField(max_length=20)
    kol_vo_et = models.IntegerField()
    kod_vida = models.ForeignKey('VidJil', models.DO_NOTHING, db_column='kod_vida')

    class Meta:
        managed = False
        db_table = 'obj_zastroi'


class ProdKv(models.Model):
    id_prod = models.AutoField(primary_key=True)
    id_dog = models.ForeignKey(DogovorProd, models.DO_NOTHING, db_column='id_dog')
    id_kv = models.ForeignKey(Kvart, models.DO_NOTHING, db_column='id_kv')
    stoim = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prod_kv'


class Sotrudn(models.Model):
    kod_sotrudn = models.IntegerField(primary_key=True)
    fio = models.CharField(max_length=90)
    dolz = models.CharField(max_length=70)

    class Meta:
        managed = False
        db_table = 'sotrudn'


class VidJil(models.Model):
    kod_vida = models.IntegerField(primary_key=True)
    naim_jil = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'vid_jil'


class Zayavka(models.Model):
    id_zaya = models.AutoField(primary_key=True)
    data_zaya = models.DateField()
    opisanie = models.CharField(max_length=20)
    kod_client = models.ForeignKey(Client, models.DO_NOTHING, db_column='kod_client')
    kod_sotrudn = models.ForeignKey(Sotrudn, models.DO_NOTHING, db_column='kod_sotrudn')

    class Meta:
        managed = False
        db_table = 'zayavka'
