# -*- coding: UTF-8 -*-
logger.info("Loading 2 objects to table courses_pricerule...")
# fields: id, seqno, fee, tariff, event_type, pf_residence, pf_composition, pf_income
loader.save(create_courses_pricerule(1,1,1,None,5,None,None,None))
loader.save(create_courses_pricerule(2,2,2,None,4,None,None,None))

loader.flush_deferred_objects()
