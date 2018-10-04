# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects to table properties_proptype...")
# fields: id, name, choicelist, default_value, limit_to_choices, multiple_choices
loader.save(create_properties_proptype(1,['Present or not', 'Vorhanden oder nicht', 'Pr\xe9sent ou pas'],u'',u'',False,False))
loader.save(create_properties_proptype(2,['Rating', 'Bewertung', 'Appr\xe9ciation(?)'],u'properties.HowWell',u'2',False,False))
loader.save(create_properties_proptype(3,['Division', 'Abteilung', 'Division'],u'',u'',False,False))

loader.flush_deferred_objects()
