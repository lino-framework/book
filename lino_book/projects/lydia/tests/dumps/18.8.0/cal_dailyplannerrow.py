# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects to table cal_dailyplannerrow...")
# fields: id, seqno, designation, start_time, end_time
loader.save(create_cal_dailyplannerrow(1,1,['AM', 'Vormittags', 'Avant-midi'],None,time(12,0,0)))
loader.save(create_cal_dailyplannerrow(2,2,['PM', 'Nachmittags', 'Apr\xe8s-midi'],time(12,0,0),None))
loader.save(create_cal_dailyplannerrow(3,3,['All day', 'Ganztags', 'Journ\xe9e enti\xe8re'],None,None))

loader.flush_deferred_objects()
