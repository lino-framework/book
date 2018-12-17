# -*- coding: UTF-8 -*-
logger.info("Loading 0 objects to table cal_task...")
# fields: id, modified, created, project, start_date, start_time, owner_type, owner_id, user, summary, description, access_class, sequence, auto_type, priority, due_date, due_time, percent, state

loader.flush_deferred_objects()
