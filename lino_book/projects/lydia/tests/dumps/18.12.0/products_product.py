# -*- coding: UTF-8 -*-
logger.info("Loading 4 objects to table products_product...")
# fields: id, name, description, cat, delivery_unit, product_type, vat_class, tariff, sales_account, sales_price
loader.save(create_products_product(1,['Group therapy', 'Gruppentherapie', 'Group therapy'],['None', '', ''],1,'20',u'100',None,None,27,'30.00'))
loader.save(create_products_product(2,['Individual therapy', 'Einzeltherapie', 'Individual therapy'],['None', '', ''],1,'20',u'100',None,None,27,'60.00'))
loader.save(create_products_product(3,['Other', 'Sonstige', 'Autre'],['None', '', ''],None,'20',u'100',None,None,None,'35.00'))
loader.save(create_products_product(4,['Cash daybook Daniel', 'Kassenbuch Daniel', 'Cash daybook Daniel'],['None', '', ''],2,'20',u'200',None,None,None,None))

loader.flush_deferred_objects()
