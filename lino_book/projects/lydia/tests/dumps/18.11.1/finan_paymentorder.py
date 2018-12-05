# -*- coding: UTF-8 -*-
logger.info("Loading 4 objects to table finan_paymentorder...")
# fields: voucher_ptr, printed_by, item_account, item_remark, total, execution_date
loader.save(create_finan_paymentorder(125,None,None,u'','-2400.21',None))
loader.save(create_finan_paymentorder(126,None,None,u'','-2250.92',None))
loader.save(create_finan_paymentorder(127,None,None,u'','-5231.67',None))
loader.save(create_finan_paymentorder(128,None,None,u'','-4181.64',None))

loader.flush_deferred_objects()
