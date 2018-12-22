# -*- coding: UTF-8 -*-
logger.info("Loading 4 objects to table finan_bankstatement...")
# fields: voucher_ptr, printed_by, item_account, item_remark, last_item_date, balance1, balance2
loader.save(create_finan_bankstatement(129,None,None,u'',None,'0.00','3391.30'))
loader.save(create_finan_bankstatement(130,None,None,u'',None,'3391.30','5554.11'))
loader.save(create_finan_bankstatement(131,None,None,u'',None,'5554.11','7025.87'))
loader.save(create_finan_bankstatement(132,None,None,u'',None,'7025.87','10634.71'))

loader.flush_deferred_objects()
