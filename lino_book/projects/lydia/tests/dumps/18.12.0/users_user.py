# -*- coding: UTF-8 -*-
logger.info("Loading 6 objects to table users_user...")
# fields: id, email, language, modified, created, start_date, end_date, access_class, event_type, password, last_login, username, user_type, initials, first_name, last_name, remarks, time_zone, cash_daybook, team, partner
loader.save(create_users_user(4,u'',u'en',dt(2018,12,22,12,25,41),dt(2018,12,22,12,24,58),None,None,u'30',4,u'pbkdf2_sha256$36000$xJReB18sfAvr$LoBpLwEvNlZKKEp5qDLWpRJpORRlHCJRf7HsCmTtYP0=',None,u'daniel',u'200',u'',u'Daniel',u'',u'','01',4,None,None))
loader.save(create_users_user(5,u'',u'en',dt(2018,12,22,12,25,41),dt(2018,12,22,12,24,58),None,None,u'30',5,u'pbkdf2_sha256$36000$ii2RdqzbzdWo$GG2BdtR1GIRvzCiR8cEeXo4pBQN4izqlMoEdcIwUEL8=',None,u'elmar',u'200',u'',u'Elmar',u'',u'','01',None,None,None))
loader.save(create_users_user(6,u'',u'en',dt(2018,12,22,12,25,41),dt(2018,12,22,12,24,58),None,None,u'30',None,u'pbkdf2_sha256$36000$S6OfQxNficJL$2pDyUrWnCg3dTObOnbflkVtYmLw2Y2c5E9//xYjTk5Y=',None,u'lydia',u'100',u'',u'Lydia',u'',u'','01',None,None,None))
loader.save(create_users_user(3,u'demo@example.com',u'fr',dt(2018,12,22,12,25,41),dt(2018,12,22,12,24,53),None,None,u'30',None,u'pbkdf2_sha256$36000$cDMVzaoW3aYn$xMQ7NTl+Y8IybF5SFDc0+bEkvkpr2TdyRaCOA3cFEr8=',None,u'romain',u'900',u'',u'Romain',u'Raffault',u'','01',None,None,None))
loader.save(create_users_user(2,u'demo@example.com',u'de',dt(2018,12,22,12,25,41),dt(2018,12,22,12,24,53),None,None,u'30',None,u'pbkdf2_sha256$36000$SLYuzqyz053h$e7YNA53LwCEKGk/KZTJ8Q5CgwZBAq6Z02WkAnLSit6w=',None,u'rolf',u'900',u'',u'Rolf',u'Rompen',u'','01',None,None,None))
loader.save(create_users_user(1,u'demo@example.com',u'en',dt(2018,12,22,12,25,41),dt(2018,12,22,12,24,53),None,None,u'30',None,u'pbkdf2_sha256$36000$AdCFm3twi8UF$e96Mcw3UJNWr8iRLoab69XPH9jxASXlOC5n+zMdUEv8=',None,u'robin',u'900',u'',u'Robin',u'Rood',u'','01',None,None,None))

loader.flush_deferred_objects()
