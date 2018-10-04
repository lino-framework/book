# -*- coding: UTF-8 -*-
logger.info("Loading 1 objects to table cal_guestrole...")
# fields: id, name
loader.save(create_cal_guestrole(1,['Attendee', 'Attendee', 'Attendee']))

loader.flush_deferred_objects()
