# -*- coding: UTF-8 -*-
logger.info("Loading 3 objects to table topics_topic...")
# fields: id, ref, name, description
loader.save(create_topics_topic(1,u'A',['Alcoholism', 'Alcoholism', 'Alcoholism'],['<Element b at 0x7fe634ab0e18>', '', '']))
loader.save(create_topics_topic(2,u'P',['Phobia', 'Phobia', 'Phobia'],['<Element b at 0x7fe634ab0f80>', '', '']))
loader.save(create_topics_topic(3,u'I',['Insomnia', 'Insomnia', 'Insomnia'],['<Element b at 0x7fe634ab0e18>', '', '']))

loader.flush_deferred_objects()
