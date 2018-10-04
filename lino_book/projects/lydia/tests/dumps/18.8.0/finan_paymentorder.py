# -*- coding: UTF-8 -*-
logger.info("Loading 4 objects to table finan_paymentorder...")
# fields: voucher_ptr, printed_by, item_account, item_remark, total, execution_date
loader.save(create_finan_paymentorder(63,None,None,u'','-1805.21',None))
loader.save(create_finan_paymentorder(64,None,None,u'','-1890.92',None))
loader.save(create_finan_paymentorder(65,None,None,u'','-5271.67',None))
loader.save(create_finan_paymentorder(66,None,None,u'','-3826.64',None))

loader.flush_deferred_objects()
