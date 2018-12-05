# -*- coding: UTF-8 -*-
logger.info("Loading 2 objects to table teams_team...")
# fields: id, ref, name
loader.save(create_teams_team(1,u'E',['Eupen', '', '']))
loader.save(create_teams_team(2,u'S',['St. Vith', '', '']))

loader.flush_deferred_objects()
