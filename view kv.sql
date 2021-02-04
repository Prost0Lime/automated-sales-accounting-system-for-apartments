select
k.Id_kv,
k.Num_etag,
k.Num_kv,
k.Area,
k.Stoim,
k.Num_obj,
kat.Naim_kat
from kvart k
join kateg_kvart kat on k.Kod_kategorii=kat.Kod_kategorii