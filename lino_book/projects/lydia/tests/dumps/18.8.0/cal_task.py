# -*- coding: UTF-8 -*-
logger.info("Loading 0 objects to table cal_task...")
# fields: id, modified, created, project, start_date, start_time, user, owner_type, owner_id, summary, description, access_class, sequence, auto_type, due_date, due_time, percent, state

loader.flush_deferred_objects()
