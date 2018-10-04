# -*- coding: UTF-8 -*-
logger.info("Loading 2 objects to table properties_propchoice...")
# fields: id, type, value, text
loader.save(create_properties_propchoice(1,3,u'1',['Furniture', 'M\xf6bel', 'Meubles']))
loader.save(create_properties_propchoice(2,3,u'2',['Web hosting', 'Hosting', 'Hosting']))

loader.flush_deferred_objects()
