# -*- coding: UTF-8 -*-
logger.info("Loading 2 objects to table sales_papertype...")
# fields: id, name, template
loader.save(create_sales_papertype(1,['Letter paper', 'Briefbogen', 'Type de papier'],u'DefaultLetter.odt'))
loader.save(create_sales_papertype(2,['Blank paper', 'Blanko-Papier', 'Papier vierge'],u'DefaultBlank.odt'))

loader.flush_deferred_objects()
