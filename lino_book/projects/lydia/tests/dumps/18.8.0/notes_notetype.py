# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects to table notes_notetype...")
# fields: id, name, build_method, template, attach_to_email, email_template, important, remark, special_type
loader.save(create_notes_notetype(1,['Default', 'Standardwert', 'Default'],None,u'',False,u'',False,u'',None))
loader.save(create_notes_notetype(2,['phone report', '', ''],None,u'',False,u'',False,u'',None))
loader.save(create_notes_notetype(3,['todo', '', ''],None,u'',False,u'',False,u'',None))

loader.flush_deferred_objects()
