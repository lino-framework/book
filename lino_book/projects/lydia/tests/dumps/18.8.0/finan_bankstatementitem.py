# -*- coding: UTF-8 -*-
logger.info("Loading 6 objects to table finan_bankstatementitem...")
# fields: id, seqno, match, amount, dc, remark, account, partner, date, voucher
loader.save(create_finan_bankstatementitem(1,1,u'SLS 13/2015','450.00',True,u'',2,113,None,70))
loader.save(create_finan_bankstatementitem(2,2,u'SLS 14/2015','880.00',True,u'',2,114,None,70))
loader.save(create_finan_bankstatementitem(3,3,u'SLS 15/2015','1370.00',True,u'',2,115,None,70))
loader.save(create_finan_bankstatementitem(4,4,u'SLS 16/2015','240.00',True,u'',2,115,None,70))
loader.save(create_finan_bankstatementitem(5,5,u'SLS 17/2015','726.75',True,u'',2,116,None,70))
loader.save(create_finan_bankstatementitem(6,6,u'SLS 18/2015','920.00',True,u'',2,117,None,70))

loader.flush_deferred_objects()
