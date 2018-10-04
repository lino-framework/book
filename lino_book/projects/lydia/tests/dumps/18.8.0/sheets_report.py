# -*- coding: UTF-8 -*-
logger.info("Loading 1 objects to table sheets_report...")
# fields: id, user, today, printed_by, start_period, end_period
loader.save(create_sheets_report(1,1,date(2015,5,23),None,1,6))

loader.flush_deferred_objects()
