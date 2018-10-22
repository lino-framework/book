# -*- coding: UTF-8 -*-
logger.info("Loading 2 objects to table cal_guestrole...")
# fields: id, ref, name
loader.save(create_cal_guestrole(1,None,['Attendee', 'Teilnehmer', 'Attendee']))
loader.save(create_cal_guestrole(2,None,['Colleague', 'Colleague', 'Colleague']))

loader.flush_deferred_objects()
