# -*- coding: UTF-8 -*-
logger.info("Loading 6 objects to table users_user...")
# fields: id, email, language, modified, created, start_date, end_date, access_class, event_type, password, last_login, username, user_type, initials, first_name, last_name, remarks, time_zone, cash_daybook, team, partner
loader.save(create_users_user(4,u'',u'en',dt(2018,12,16,6,19,34),dt(2018,12,16,6,19,0),None,None,u'30',4,u'pbkdf2_sha256$36000$g8Z1Ga2ojZdI$BWrIl01WQsSZMimMoOFk1QA5oZgcGO9Fec4137HkiXI=',None,u'daniel',u'200',u'',u'Daniel',u'',u'','01',4,None,None))
loader.save(create_users_user(5,u'',u'en',dt(2018,12,16,6,19,34),dt(2018,12,16,6,19,0),None,None,u'30',5,u'pbkdf2_sha256$36000$iV2NRIElhb0d$StPc/4sMKxLNrIu118qVJkBMR0/caK3rJxirWNC5fnM=',None,u'elmar',u'200',u'',u'Elmar',u'',u'','01',None,None,None))
loader.save(create_users_user(6,u'',u'en',dt(2018,12,16,6,19,34),dt(2018,12,16,6,19,0),None,None,u'30',None,u'pbkdf2_sha256$36000$Or7qyC7Fbu4J$6AFWeJyUkUVv/2lpmHcHM0MckEvCZ/LN+np9FaBkF6c=',None,u'lydia',u'100',u'',u'Lydia',u'',u'','01',None,None,None))
loader.save(create_users_user(3,u'demo@example.com',u'fr',dt(2018,12,16,6,19,34),dt(2018,12,16,6,18,55),None,None,u'30',None,u'pbkdf2_sha256$36000$eGsBXPf39n1W$xoZe7KjAhyoNIQwo/qSBPDzW0DIetMEI6hEPTN5YoN4=',None,u'romain',u'900',u'',u'Romain',u'Raffault',u'','01',None,None,None))
loader.save(create_users_user(2,u'demo@example.com',u'de',dt(2018,12,16,6,19,34),dt(2018,12,16,6,18,55),None,None,u'30',None,u'pbkdf2_sha256$36000$eiVbmajknH1z$Tujnk+oIWamsL1dkPAixHSDwC+ym+gP+YEUHlQGA204=',None,u'rolf',u'900',u'',u'Rolf',u'Rompen',u'','01',None,None,None))
loader.save(create_users_user(1,u'demo@example.com',u'en',dt(2018,12,16,6,19,34),dt(2018,12,16,6,18,55),None,None,u'30',None,u'pbkdf2_sha256$36000$KpaBJ2tIS6TD$vFygM6mRf93eH/i8PC1XjiSz9oDeCxewDh0iux5PVLc=',None,u'robin',u'900',u'',u'Robin',u'Rood',u'','01',None,None,None))

loader.flush_deferred_objects()
