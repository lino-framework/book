# -*- coding: UTF-8 -*-
logger.info("Loading 14 objects to table households_household...")
# fields: partner_ptr, type, client_state, tariff
loader.save(create_households_household(182,1,'01','16'))
loader.save(create_households_household(183,2,'01','16'))
loader.save(create_households_household(184,3,'01','16'))
loader.save(create_households_household(185,4,'01','16'))
loader.save(create_households_household(186,5,'01','16'))
loader.save(create_households_household(187,6,'01','16'))
loader.save(create_households_household(204,1,'01','16'))
loader.save(create_households_household(205,2,'01','16'))
loader.save(create_households_household(206,1,'01','16'))
loader.save(create_households_household(207,1,'01','16'))
loader.save(create_households_household(220,1,'01','16'))
loader.save(create_households_household(221,2,'01','16'))
loader.save(create_households_household(222,2,'01','16'))
loader.save(create_households_household(223,1,'01','16'))

loader.flush_deferred_objects()
