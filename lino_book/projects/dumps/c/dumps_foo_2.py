# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects (part 2 of 2) to table dumps_foo...")
# fields: id, designation, last_visit, bar
loader.save(create_dumps_foo(3,['Three', 'Drei', 'Trois'],dt(2017,10,29,3,16,6),'10'))

loader.flush_deferred_objects()
