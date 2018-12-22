# -*- coding: UTF-8 -*-
logger.info("Loading 8 objects to table countries_country...")
# fields: name, isocode, short_code, iso3
loader.save(create_countries_country(['Belgium', 'Belgien', 'Belgique'],u'BE',u'',u''))
loader.save(create_countries_country(['Congo (Democratic Republic)', 'Kongo (Demokratische Republik)', 'Congo (R\xe9publique democratique)'],u'CD',u'',u''))
loader.save(create_countries_country(['Germany', 'Deutschland', 'Allemagne'],u'DE',u'',u''))
loader.save(create_countries_country(['Estonia', 'Estland', 'Estonie'],u'EE',u'',u''))
loader.save(create_countries_country(['France', 'Frankreich', 'France'],u'FR',u'',u''))
loader.save(create_countries_country(['Maroc', 'Marokko', 'Maroc'],u'MA',u'',u''))
loader.save(create_countries_country(['Netherlands', 'Niederlande', 'Pays-Bas'],u'NL',u'',u''))
loader.save(create_countries_country(['Russia', 'Russland', 'Russie'],u'RU',u'',u''))

loader.flush_deferred_objects()
