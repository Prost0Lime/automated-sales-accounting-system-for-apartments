from django.contrib import admin

# Register your models here.
# Register the Admin classes for Book using the decorator
from core.models import Client, DogovorProd, KategKvart, KnOplat, Kvart, ObjZastroi, ProdKv, Sotrudn, VidJil, Zayavka


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["kod_client", "pasp", "fio_sotr", "phone", "status"]


@admin.register(DogovorProd)
class DogovorProdAdmin(admin.ModelAdmin):
    list_display = ["id_dog", "num_dog", "date_sost", "date_prod", "sum_dog", "opl", "id_zaya", "kod_sotrudn"]

@admin.register(KategKvart)
class KategKvartAdmin(admin.ModelAdmin):
    pass

@admin.register(KnOplat)
class KnOplatAdmin(admin.ModelAdmin):
    pass

@admin.register(Kvart)
class KvartAdmin(admin.ModelAdmin):
    pass

@admin.register(ObjZastroi)
class ObjZastroiAdmin(admin.ModelAdmin):
    pass

@admin.register(ProdKv)
class ProdKvAdmin(admin.ModelAdmin):
    pass

@admin.register(Sotrudn)
class SotrudnAdmin(admin.ModelAdmin):
    pass

@admin.register(VidJil)
class VidJilAdmin(admin.ModelAdmin):
    pass

@admin.register(Zayavka)
class ZayavkaAdmin(admin.ModelAdmin):
    pass
