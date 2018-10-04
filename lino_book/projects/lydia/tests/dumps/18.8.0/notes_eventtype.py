# -*- coding: UTF-8 -*-
logger.info("Loading 1 objects to table notes_eventtype...")
# fields: id, name, remark, body
loader.save(create_notes_eventtype(1,['System note', 'System note', 'System note'],u'',['', '', '']))

loader.flush_deferred_objects()
