SELECT setval('kn_oplat_id_oplt_seq', (SELECT MAX(id_oplt) FROM kn_oplat));
SELECT setval('dogovor_prod_id_dog_seq', (SELECT MAX(id_dog) FROM dogovor_prod));
SELECT setval('zayavka_id_zaya_seq', (SELECT MAX(id_zaya) FROM zayavka));
SELECT setval('kvart_id_kv_seq', (SELECT MAX(id_kv) FROM kvart));
SELECT setval('prod_kv_id_prod_seq', (SELECT MAX(id_prod) FROM prod_kv));