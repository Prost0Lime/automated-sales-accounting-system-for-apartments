select
o.Num_obj,
o.street,
o.num_zd,
o.Kol_vo_et,
v.Naim_jil
from obj_zastroi o
join vid_jil v on v.Kod_vida=o.Kod_vida