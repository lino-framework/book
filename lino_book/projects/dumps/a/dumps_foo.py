# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects to table dumps_foo...")
# fields: id, name, last_visit
loader.save(create_dumps_foo(1,[u'First', u'Erster', u'Premier'],dt(2016,7,2,23,55,12)))
loader.save(create_dumps_foo(2,[u'January', u'Januar', u'janvier'],dt(2016,7,3,0,10,23)))
loader.save(create_dumps_foo(3,[u'Three', u'Drei', u'Trois'],dt(2016,10,30,4,34,0)))

loader.flush_deferred_objects()
