# -*- coding: UTF-8 -*-
logger.info("Loading 2 objects to table cal_guestrole...")
# fields: id, ref, name, is_teacher
loader.save(create_cal_guestrole(1,None,['Attendee', 'Teilnehmer', 'Attendee'],False))
loader.save(create_cal_guestrole(2,None,['Colleague', 'Colleague', 'Colleague'],True))

loader.flush_deferred_objects()
