# -*- coding: UTF-8 -*-
logger.info("Loading 6 objects to table households_household...")
# fields: partner_ptr, type, client_state
loader.save(create_households_household(182,1,'01'))
loader.save(create_households_household(183,2,'01'))
loader.save(create_households_household(184,3,'01'))
loader.save(create_households_household(185,4,'01'))
loader.save(create_households_household(186,5,'01'))
loader.save(create_households_household(187,6,'01'))

loader.flush_deferred_objects()
