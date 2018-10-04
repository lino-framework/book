# -*- coding: UTF-8 -*-
logger.info("Loading 6 objects to table ledger_fiscalyear...")
# fields: id, ref, start_date, end_date, state
loader.save(create_ledger_fiscalyear(1,u'2015',date(2015,1,1),date(2015,12,31),'10'))
loader.save(create_ledger_fiscalyear(2,u'2016',date(2016,1,1),date(2016,12,31),'10'))
loader.save(create_ledger_fiscalyear(3,u'2017',date(2017,1,1),date(2017,12,31),'10'))
loader.save(create_ledger_fiscalyear(4,u'2018',date(2018,1,1),date(2018,12,31),'10'))
loader.save(create_ledger_fiscalyear(5,u'2019',date(2019,1,1),date(2019,12,31),'10'))
loader.save(create_ledger_fiscalyear(6,u'2020',date(2020,1,1),date(2020,12,31),'10'))

loader.flush_deferred_objects()
