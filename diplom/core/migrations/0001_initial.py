# Generated by Django 3.1.5 on 2021-01-30 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('kod_client', models.IntegerField(primary_key=True, serialize=False)),
                ('pasp', models.CharField(max_length=40)),
                ('fio_sotr', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'client',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DogovorProd',
            fields=[
                ('id_dog', models.AutoField(primary_key=True, serialize=False)),
                ('num_dog', models.IntegerField()),
                ('date_sost', models.DateField()),
                ('date_prod', models.DateField()),
                ('sum_dog', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('opl', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ],
            options={
                'db_table': 'dogovor_prod',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KategKvart',
            fields=[
                ('kod_kategorii', models.IntegerField(primary_key=True, serialize=False)),
                ('naim_kat', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'kateg_kvart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KnOplat',
            fields=[
                ('id_oplt', models.AutoField(primary_key=True, serialize=False)),
                ('date_opl', models.DateField()),
                ('sum_opl', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'kn_oplat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kvart',
            fields=[
                ('id_kv', models.AutoField(primary_key=True, serialize=False)),
                ('num_etag', models.IntegerField()),
                ('num_kv', models.CharField(max_length=50)),
                ('kol_vo_kom', models.IntegerField(blank=True, null=True)),
                ('area', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('stoim', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ],
            options={
                'db_table': 'kvart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ObjZastroi',
            fields=[
                ('num_obj', models.IntegerField(primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=70)),
                ('num_zd', models.CharField(max_length=20)),
                ('kol_vo_et', models.IntegerField()),
            ],
            options={
                'db_table': 'obj_zastroi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProdKv',
            fields=[
                ('id_prod', models.AutoField(primary_key=True, serialize=False)),
                ('stoim', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
            options={
                'db_table': 'prod_kv',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sotrudn',
            fields=[
                ('kod_sotrudn', models.IntegerField(primary_key=True, serialize=False)),
                ('fio', models.CharField(max_length=90)),
                ('dolz', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'sotrudn',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VidJil',
            fields=[
                ('kod_vida', models.IntegerField(primary_key=True, serialize=False)),
                ('naim_jil', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'vid_jil',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Zayavka',
            fields=[
                ('id_zaya', models.AutoField(primary_key=True, serialize=False)),
                ('data_zaya', models.DateField()),
                ('opisanie', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'zayavka',
                'managed': False,
            },
        ),
    ]
