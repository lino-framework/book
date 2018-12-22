# -*- coding: UTF-8 -*-
logger.info("Loading 6 objects to table ledger_accountingperiod...")
# fields: id, ref, start_date, end_date, state, year, remark
loader.save(create_ledger_accountingperiod(1,u'2015-01',date(2015,1,1),date(2015,1,31),'10',1,u''))
loader.save(create_ledger_accountingperiod(2,u'2015-02',date(2015,2,1),date(2015,2,28),'10',1,u''))
loader.save(create_ledger_accountingperiod(3,u'2015-03',date(2015,3,1),date(2015,3,31),'10',1,u''))
loader.save(create_ledger_accountingperiod(4,u'2015-04',date(2015,4,1),date(2015,4,30),'10',1,u''))
loader.save(create_ledger_accountingperiod(5,u'2015-05',date(2015,5,1),date(2015,5,31),'10',1,u''))
loader.save(create_ledger_accountingperiod(6,u'2015-12',date(2015,12,1),date(2015,12,31),'10',1,u''))

loader.flush_deferred_objects()
