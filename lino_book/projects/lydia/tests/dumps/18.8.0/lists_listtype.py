# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects to table lists_listtype...")
# fields: id, designation
loader.save(create_lists_listtype(1,['Mailing list', 'Mailing list', 'Mailing list']))
loader.save(create_lists_listtype(2,['Discussion group', 'Discussion group', 'Discussion group']))
loader.save(create_lists_listtype(3,['Flags', 'Flags', 'Flags']))

loader.flush_deferred_objects()
