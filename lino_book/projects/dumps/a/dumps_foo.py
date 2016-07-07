# -*- coding: UTF-8 -*-
logger.info("Loading 2 objects to table dumps_foo...")
# fields: id, name, last_visit
loader.save(create_dumps_foo(1,[u'First', u'', u''],dt(2016,7,2,23,55,12)))
loader.save(create_dumps_foo(2,[u'Last', u'', u''],dt(2016,7,3,0,10,23)))

loader.flush_deferred_objects()
