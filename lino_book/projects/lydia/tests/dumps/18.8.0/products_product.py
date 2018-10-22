# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects to table products_product...")
# fields: id, name, description, cat, delivery_unit, vat_class, number_of_events, min_asset, sales_account, sales_price
loader.save(create_products_product(1,['Group therapy', 'Gruppentherapie', 'Group therapy'],['None', '', ''],1,'20',None,None,1,None,'30.00'))
loader.save(create_products_product(2,['Individual therapy', 'Einzeltherapie', 'Individual therapy'],['None', '', ''],1,'20',None,None,1,27,'60.00'))
loader.save(create_products_product(3,['Other', 'Sonstige', 'Autre'],['None', '', ''],None,'20',None,None,1,None,'35.00'))

loader.flush_deferred_objects()
