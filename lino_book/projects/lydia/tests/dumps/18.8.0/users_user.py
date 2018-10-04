# -*- coding: UTF-8 -*-
logger.info("Loading 6 objects to table users_user...")
# fields: id, email, language, modified, created, start_date, end_date, password, last_login, username, user_type, initials, first_name, last_name, remarks, time_zone, access_class, event_type, team, partner
loader.save(create_users_user(4,u'',u'en',dt(2018,10,4,3,54,53),dt(2018,10,4,3,54,30),None,None,u'pbkdf2_sha256$36000$qITN9xBM6KLI$DePqioDrvFXNkfHtAINMHnZTBk02M2YIbckkoi7htso=',None,u'daniel',u'200',u'',u'Daniel',u'',u'','01',u'30',None,None,None))
loader.save(create_users_user(5,u'',u'en',dt(2018,10,4,3,54,53),dt(2018,10,4,3,54,30),None,None,u'pbkdf2_sha256$36000$wArBY3sd43yH$7vx++YPQfomESh4cqqcrFzYBsalW1buQjTDLSS3MyOM=',None,u'elmar',u'200',u'',u'Elmar',u'',u'','01',u'30',None,None,None))
loader.save(create_users_user(6,u'',u'en',dt(2018,10,4,3,54,53),dt(2018,10,4,3,54,30),None,None,u'pbkdf2_sha256$36000$tekXSXsCCzf8$RQy6HsMXg6h1nBHKHLkmEasiX6B66hyFBZ43hwa2Qjs=',None,u'lydia',u'100',u'',u'Lydia',u'',u'','01',u'30',None,None,None))
loader.save(create_users_user(3,u'demo@example.com',u'fr',dt(2018,10,4,3,54,53),dt(2018,10,4,3,54,22),None,None,u'pbkdf2_sha256$36000$sB2Ib0ocCZlv$+CtHGdPvTOnXrlsVXn41GlHvA/NMEGFkeK/iMxMv7Jk=',None,u'romain',u'900',u'',u'Romain',u'Raffault',u'','01',u'30',None,None,None))
loader.save(create_users_user(2,u'demo@example.com',u'de',dt(2018,10,4,3,54,53),dt(2018,10,4,3,54,22),None,None,u'pbkdf2_sha256$36000$xNfU8xYju778$+NdtSxLjC+eVR28UvgSfFL4qd8XmkNL0JO78DwiOn0c=',None,u'rolf',u'900',u'',u'Rolf',u'Rompen',u'','01',u'30',None,None,None))
loader.save(create_users_user(1,u'demo@example.com',u'en',dt(2018,10,4,3,54,53),dt(2018,10,4,3,54,22),None,None,u'pbkdf2_sha256$36000$JBKchPRunBr4$nSHzZdeD+GdXKr3uq89SQosBTSkRKs73nwrQx9JlCpk=',None,u'robin',u'900',u'',u'Robin',u'Rood',u'','01',u'30',None,None,None))

loader.flush_deferred_objects()
