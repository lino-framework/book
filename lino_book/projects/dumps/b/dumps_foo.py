# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects to table dumps_foo...")
# fields: id, designation, last_visit, bar
loader.save(create_dumps_foo(1,['First', 'Erster', 'Premier'],dt(2016,7,2,23,55,12),'10'))
loader.save(create_dumps_foo(2,['January', 'Januar', 'janvier'],dt(2016,7,3,0,10,23),'10'))
loader.save(create_dumps_foo(3,['Three', 'Drei', 'Trois'],dt(2017,10,29,3,16,6),'10'))

loader.flush_deferred_objects()
