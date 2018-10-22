# -*- coding: UTF-8 -*-
logger.info("Loading 1 objects to table system_siteconfig...")
# fields: id, default_build_method, simulate_today, site_company, default_event_type, site_calendar, max_auto_events, hide_events_before, next_partner_id, system_note_type
loader.save(create_system_siteconfig(1,None,None,198,None,1,72,date(2015,4,1),200,1))

loader.flush_deferred_objects()
