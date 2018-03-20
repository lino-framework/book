# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects (part 1 of 2) to table dumps_foo...")
# fields: id, designation, last_visit, bar
loader.save(create_dumps_foo(1,['First', 'Erster', 'Premier'],dt(2016,7,2,23,55,12),'10'))
loader.save(create_dumps_foo(2,['January', 'Januar', 'janvier'],dt(2016,7,3,0,10,23),'10'))

