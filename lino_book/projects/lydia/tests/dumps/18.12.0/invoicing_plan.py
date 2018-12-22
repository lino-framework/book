# -*- coding: UTF-8 -*-
logger.info("Loading 1 objects to table invoicing_plan...")
# fields: id, user, today, journal, max_date, partner, course
loader.save(create_invoicing_plan(1,6,date(2015,3,1),1,None,None,None))

loader.flush_deferred_objects()
