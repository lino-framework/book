# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects to table bevats_declaration...")
# fields: voucher_ptr, printed_by, partner, payment_term, start_period, end_period, your_ref, due_date, F71, F72, F73, F75, F76, F77, F78, F80, F81, F82, F83
loader.save(create_bevats_declaration(60,None,235,None,1,None,u'',None,'1341.90','703.80','0.00','3524.08','0.00','0.00','0.00','59.57','0.00','0.00','59.57'))
loader.save(create_bevats_declaration(61,None,235,None,2,None,u'',None,'1343.90','702.60','0.00','3523.88','0.00','0.00','0.00','59.46','0.00','0.00','59.46'))
loader.save(create_bevats_declaration(62,None,235,None,3,None,u'',None,'1343.10','705.10','0.00','3522.68','0.00','0.00','0.00','59.21','0.00','0.00','59.21'))

loader.flush_deferred_objects()
