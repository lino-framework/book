# -*- coding: UTF-8 -*-
logger.info("Loading 6 objects to table users_user...")
# fields: id, email, language, modified, created, start_date, end_date, access_class, event_type, password, last_login, username, user_type, initials, first_name, last_name, remarks, time_zone, team, partner
loader.save(create_users_user(4,u'',u'en',dt(2018,10,24,3,48,14),dt(2018,10,24,3,47,58),None,None,u'30',None,u'pbkdf2_sha256$36000$y2slJB4cMsWh$SD92euaP2rw2uXHvCH/cIjw3aVW0xlgdrk6P3f7vVtU=',None,u'daniel',u'200',u'',u'Daniel',u'',u'','01',None,None))
loader.save(create_users_user(5,u'',u'en',dt(2018,10,24,3,48,14),dt(2018,10,24,3,47,58),None,None,u'30',None,u'pbkdf2_sha256$36000$30x7tBz19vhh$TGp7acW/83r/mH5RaIb9eEVgLwpu2aVUiuJsQVJoEnU=',None,u'elmar',u'200',u'',u'Elmar',u'',u'','01',None,None))
loader.save(create_users_user(6,u'',u'en',dt(2018,10,24,3,48,14),dt(2018,10,24,3,47,58),None,None,u'30',None,u'pbkdf2_sha256$36000$Dj8VvCWl0YuD$1Mh8917qlD4L3+cyH4H4R1Lk5ve8QtIZWCuVJ9bQkoc=',None,u'lydia',u'100',u'',u'Lydia',u'',u'','01',None,None))
loader.save(create_users_user(3,u'demo@example.com',u'fr',dt(2018,10,24,3,48,14),dt(2018,10,24,3,47,54),None,None,u'30',None,u'pbkdf2_sha256$36000$sjI3to67193r$Wee1zAxctvgu8FqvvQF8VhnSyy7rhi1icQYeSxsXL9I=',None,u'romain',u'900',u'',u'Romain',u'Raffault',u'','01',None,None))
loader.save(create_users_user(2,u'demo@example.com',u'de',dt(2018,10,24,3,48,14),dt(2018,10,24,3,47,54),None,None,u'30',None,u'pbkdf2_sha256$36000$cUUpsgeIvKio$Au4722/MlProU4AkLvZicpNLusxSR7rvY/K+8JPWrlI=',None,u'rolf',u'900',u'',u'Rolf',u'Rompen',u'','01',None,None))
loader.save(create_users_user(1,u'demo@example.com',u'en',dt(2018,10,24,3,48,14),dt(2018,10,24,3,47,54),None,None,u'30',None,u'pbkdf2_sha256$36000$w5FK5uzR06M1$rB0vxNtq3fSj2dFyoRStFKe2sB9A4HZCOxjMsupEKWw=',None,u'robin',u'900',u'',u'Robin',u'Rood',u'','01',None,None))

loader.flush_deferred_objects()
