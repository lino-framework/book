# -*- coding: UTF-8 -*-
logger.info("Loading 1 objects to table finan_bankstatement...")
# fields: voucher_ptr, printed_by, item_account, item_remark, last_item_date, balance1, balance2
loader.save(create_finan_bankstatement(70,None,None,u'',None,'0.00','4586.75'))

loader.flush_deferred_objects()
