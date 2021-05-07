from django.contrib import admin

# Register your models here.
# Register the Admin classes for Book using the decorator

from core.models import Client, DogovorProd, KategKvart, KnOplat, Kvart, ObjZastroi, ProdKv, Sotrudn, VidJil, Zayavka


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["kod_client", "pasp", "fio_client", "phone", "status"]
    list_filter = ["status"]
    search_fields = ["pasp", "fio_client", "phone"]
    ordering = ["kod_client"]


class KnOplatInline(admin.TabularInline):
    model = KnOplat
    extra = 0


@admin.register(DogovorProd)
class DogovorProdAdmin(admin.ModelAdmin):
    list_display = ["id_dog", "num_dog", "date_sost", "date_prod", "sum_dog", "opl", "id_zaya", "kod_sotrudn"]
    search_fields = ["num_dog", "date_sost", "id_zaya", "date_prod"]
    list_filter = ["kod_sotrudn"]
    ordering = ["id_dog"]
    inlines = [KnOplatInline]


@admin.register(KategKvart)
class KategKvartAdmin(admin.ModelAdmin):
    list_display = ["kod_kategorii", "naim_kat"]
    search_fields = ["naim_kat"]
    ordering = ["kod_kategorii"]


@admin.register(KnOplat)
class KnOplatAdmin(admin.ModelAdmin):
    list_display = ["id_oplt", "date_opl", "sum_opl", "id_dog"]
    search_fields = ["date_opl", "id_dog"]
    ordering = ["id_oplt"]


@admin.register(Kvart)
class KvartAdmin(admin.ModelAdmin):
    list_display = ["id_kv", "num_etag", "num_kv", "kol_vo_kom", "area", "stoim", "num_obj", "kod_kategorii",
                    "image_img"]
    readonly_fields = ('image_img',)
    list_filter = ["num_etag", "kol_vo_kom"]
    ordering = ["id_kv"]


@admin.register(ObjZastroi)
class ObjZastroiAdmin(admin.ModelAdmin):
    list_display = ["num_obj", "street", "num_zd", "kol_vo_et", "kod_vida", "trans_dos", "soc_infr", "rekreaciya",
                    "parkov"]
    list_filter = ["street"]
    ordering = ["num_obj"]


@admin.register(ProdKv)
class ProdKvAdmin(admin.ModelAdmin):
    list_display = ["id_prod", "id_dog"]
    ordering = ["id_prod"]


@admin.register(Sotrudn)
class SotrudnAdmin(admin.ModelAdmin):
    list_display = ["kod_sotrudn", "fio", "dolz"]
    list_filter = ["dolz"]
    search_fields = ["fio"]
    ordering = ["kod_sotrudn"]


@admin.register(VidJil)
class VidJilAdmin(admin.ModelAdmin):
    list_display = ["kod_vida", "naim_jil"]
    search_fields = ["naim_jil"]
    ordering = ["kod_vida"]


@admin.register(Zayavka)
class ZayavkaAdmin(admin.ModelAdmin):
    list_display = ["id_zaya", "num_zaya", "data_zaya", "id_kv", "kod_client", "kod_sotrudn"]
    search_fields = ["data_zaya"]
    ordering = ["id_zaya"]