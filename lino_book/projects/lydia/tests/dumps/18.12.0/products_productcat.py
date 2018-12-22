# -*- coding: UTF-8 -*-
logger.info("Loading 2 objects to table products_productcat...")
# fields: id, name, description
loader.save(create_products_productcat(1,['Fees', 'Geb\xfchren', 'Fees'],u''))
loader.save(create_products_productcat(2,['Cash daybooks', 'Kassenb\xfccher', 'Cash daybooks'],u''))

loader.flush_deferred_objects()
