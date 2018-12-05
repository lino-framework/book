# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects to table topics_topic...")
# fields: id, ref, name, description
loader.save(create_topics_topic(1,u'A',['Alcoholism', 'Alcoholism', 'Alcoholism'],['<Element b at 0x7fd2d38d28c0>', '', '']))
loader.save(create_topics_topic(2,u'P',['Phobia', 'Phobia', 'Phobia'],['<Element b at 0x7fd2d38d2cf8>', '', '']))
loader.save(create_topics_topic(3,u'I',['Insomnia', 'Insomnia', 'Insomnia'],['<Element b at 0x7fd2d38d28c0>', '', '']))

loader.flush_deferred_objects()
