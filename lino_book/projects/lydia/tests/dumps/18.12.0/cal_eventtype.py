# -*- coding: UTF-8 -*-
logger.info("Loading 5 objects to table cal_eventtype...")
# fields: id, ref, seqno, name, attach_to_email, email_template, description, is_appointment, all_rooms, locks_user, force_guest_states, start_date, event_label, max_conflicting, max_days, transparent, planner_column
loader.save(create_cal_eventtype(1,None,1,['Holidays', 'Feiertage', 'Jours f\xe9ri\xe9s'],False,u'',u'',False,True,False,False,None,['', '', ''],1,1,False,u'10'))
loader.save(create_cal_eventtype(2,None,2,['Meeting', 'Versammlung', 'R\xe9union'],False,u'',u'',True,False,False,False,None,['', '', ''],1,1,False,u'10'))
loader.save(create_cal_eventtype(3,None,3,['Internal', 'Intern', 'Interne'],False,u'',u'',True,False,False,False,None,['', '', ''],1,1,True,u'20'))
loader.save(create_cal_eventtype(4,None,4,['Individual appointment', 'Einzelgespr\xe4ch', 'Individual appointment'],False,u'',u'',True,False,False,True,None,['', '', ''],1,1,False,None))
loader.save(create_cal_eventtype(5,None,5,['Group meeting', 'Gruppengespr\xe4ch', 'Group meeting'],False,u'',u'',True,False,False,False,None,['', '', ''],1,1,False,None))

loader.flush_deferred_objects()
