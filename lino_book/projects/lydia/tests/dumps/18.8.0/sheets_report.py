# -*- coding: UTF-8 -*-
logger.info("Loading 1 objects to table sheets_report...")
# fields: id, printed_by, user, today, start_period, end_period
loader.save(create_sheets_report(1,None,1,date(2015,5,23),1,6))

loader.flush_deferred_objects()
