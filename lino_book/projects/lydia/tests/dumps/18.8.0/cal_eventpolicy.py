# -*- coding: UTF-8 -*-
logger.info("Loading 6 objects to table cal_eventpolicy...")
# fields: id, start_date, start_time, end_date, end_time, name, every_unit, every, monday, tuesday, wednesday, thursday, friday, saturday, sunday, max_events, event_type
loader.save(create_cal_eventpolicy(1,date(2015,5,23),time(9,0,0),None,None,['Every month', 'Monatlich', 'Every month'],u'M',1,True,True,True,True,True,False,False,None,2))
loader.save(create_cal_eventpolicy(2,date(2015,5,23),time(9,0,0),None,None,['Every 2 months', 'Alle 2 Monate', 'Every 2 months'],u'M',2,True,True,True,True,True,False,False,None,2))
loader.save(create_cal_eventpolicy(3,date(2015,5,23),None,None,None,['Every 3 months', 'Alle 3 Monate', 'Every 3 months'],u'M',3,True,True,True,True,True,False,False,None,2))
loader.save(create_cal_eventpolicy(4,date(2015,5,23),time(9,0,0),None,None,['Every 2 weeks', 'Alle 2 Wochen', 'Every 2 weeks'],u'W',2,True,True,True,True,True,False,False,None,2))
loader.save(create_cal_eventpolicy(5,date(2015,5,23),time(9,0,0),None,None,['Once after 10 days', 'Einmal nach 10 Tagen', 'Once after 10 days'],u'D',10,True,True,True,True,True,False,False,1,2))
loader.save(create_cal_eventpolicy(6,date(2015,5,23),None,None,None,['Other', 'Sonstige', 'Autre'],u'M',1,False,False,False,False,False,False,False,None,None))

loader.flush_deferred_objects()
