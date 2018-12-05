# -*- coding: UTF-8 -*-
logger.info("Loading 1 objects to table cal_calendar...")
# fields: id, name, description, color
loader.save(create_cal_calendar(1,['General', 'Allgemein', 'G\xe9n\xe9ral'],u'',1))

loader.flush_deferred_objects()
