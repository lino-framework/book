# -*- coding: UTF-8 -*-
logger.info("Loading 6 objects to table invoicing_salesrule...")
# fields: partner, invoice_recipient, paper_type
loader.save(create_invoicing_salesrule(115,None,None))
loader.save(create_invoicing_salesrule(124,121,None))
loader.save(create_invoicing_salesrule(126,127,None))
loader.save(create_invoicing_salesrule(140,138,None))
loader.save(create_invoicing_salesrule(149,147,None))
loader.save(create_invoicing_salesrule(163,162,None))

loader.flush_deferred_objects()
