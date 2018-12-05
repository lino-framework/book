# -*- coding: UTF-8 -*-
logger.info("Loading 8 objects to table lists_list...")
# fields: id, ref, designation, list_type, remarks
loader.save(create_lists_list(1,None,['Announcements', 'Ank\xfcndigungen', 'Announcements'],1,u''))
loader.save(create_lists_list(2,None,['Weekly newsletter', 'Weekly newsletter', 'Weekly newsletter'],1,u''))
loader.save(create_lists_list(3,None,['General discussion', 'General discussion', 'General discussion'],2,u''))
loader.save(create_lists_list(4,None,['Beginners forum', 'Beginners forum', 'Beginners forum'],2,u''))
loader.save(create_lists_list(5,None,['Developers forum', 'Developers forum', 'Developers forum'],2,u''))
loader.save(create_lists_list(6,None,['PyCon 2014', 'PyCon 2014', 'PyCon 2014'],3,u''))
loader.save(create_lists_list(7,None,['Free Software Day 2014', 'Free Software Day 2014', 'Free Software Day 2014'],3,u''))
loader.save(create_lists_list(8,None,['Schools', 'Schulen', 'Schools'],3,u''))

loader.flush_deferred_objects()
