# -*- coding: UTF-8 -*-
logger.info("Loading 1 objects to table products_productcat...")
# fields: id, name, description
loader.save(create_products_productcat(1,['Payment by presence', 'Payment by presence', 'Payment by presence'],u''))

loader.flush_deferred_objects()
