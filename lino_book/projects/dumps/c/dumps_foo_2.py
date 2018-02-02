# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects (part 2 of 2) to table dumps_foo...")
# fields: id, name, last_visit
loader.save(create_dumps_foo(3,[u'Three', u'Drei', u'Trois'],dt(2017,10,29,3,16,6)))

loader.flush_deferred_objects()
