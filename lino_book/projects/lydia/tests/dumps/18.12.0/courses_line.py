# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects to table courses_line...")
# fields: id, ref, name, excerpt_title, company, contact_person, contact_role, course_area, topic, description, every_unit, every, event_type, fee, guest_role, options_cat, fees_cat, body_template, invoicing_policy
loader.save(create_courses_line(1,None,['Individual therapies', '', ''],['', '', ''],None,None,None,'IT',None,['', '', ''],u'W',1,None,None,1,None,None,u'','00'))
loader.save(create_courses_line(2,None,['Life groups', '', ''],['', '', ''],None,None,None,'LG',None,['', '', ''],u'W',1,None,None,1,None,None,u'','00'))
loader.save(create_courses_line(3,None,['Other groups', '', ''],['', '', ''],None,None,None,'OG',None,['', '', ''],u'W',1,None,None,1,None,None,u'','00'))

loader.flush_deferred_objects()
