# -*- coding: UTF-8 -*-
logger.info("Loading 4 objects to table cal_priority...")
# fields: id, name, ref
loader.save(create_cal_priority(1,['very urgent', 'sehr dringend', 'tr\xe8s urgent'],u'1'))
loader.save(create_cal_priority(2,['urgent', 'dringend', 'urgent'],u'3'))
loader.save(create_cal_priority(3,['normal', 'normal', 'normal'],u'5'))
loader.save(create_cal_priority(4,['not urgent', 'nicht dringend', 'pas urgent'],u'9'))

loader.flush_deferred_objects()
