# -*- coding: UTF-8 -*-
logger.info("Loading 6 objects to table users_user...")
# fields: id, email, language, modified, created, start_date, end_date, access_class, event_type, password, last_login, username, user_type, initials, first_name, last_name, remarks, time_zone, team, partner
loader.save(create_users_user(4,u'',u'en',dt(2018,10,22,12,56,25),dt(2018,10,22,12,56,9),None,None,u'30',None,u'pbkdf2_sha256$36000$IBEV7XV50VZJ$VN+7gbcJxTArRYkmQNsid3KUPniOLu3hcn1C7DxjM/g=',None,u'daniel',u'200',u'',u'Daniel',u'',u'','01',None,None))
loader.save(create_users_user(5,u'',u'en',dt(2018,10,22,12,56,25),dt(2018,10,22,12,56,9),None,None,u'30',None,u'pbkdf2_sha256$36000$GY44yp9Iphg7$LJpwy/QLRrKVDTxN+ArtKoJCXsATu8UthuNgaGkWLHs=',None,u'elmar',u'200',u'',u'Elmar',u'',u'','01',None,None))
loader.save(create_users_user(6,u'',u'en',dt(2018,10,22,12,56,25),dt(2018,10,22,12,56,9),None,None,u'30',None,u'pbkdf2_sha256$36000$87VPQ5zdFo1o$XYf71nSdFzBbZvp38vGj+B/xWjnc8SQU+q918U/LwHI=',None,u'lydia',u'100',u'',u'Lydia',u'',u'','01',None,None))
loader.save(create_users_user(3,u'demo@example.com',u'fr',dt(2018,10,22,12,56,25),dt(2018,10,22,12,56,5),None,None,u'30',None,u'pbkdf2_sha256$36000$yZnOjCDx8RYK$qvhKagHXNXUjiubqRGrF6X/bWDmi/Img8PYGeILKsh0=',None,u'romain',u'900',u'',u'Romain',u'Raffault',u'','01',None,None))
loader.save(create_users_user(2,u'demo@example.com',u'de',dt(2018,10,22,12,56,25),dt(2018,10,22,12,56,5),None,None,u'30',None,u'pbkdf2_sha256$36000$ukiGlAS0kUoe$1V29QuhSS48OkUlt3f0IMiBYoVLRQgQ+5PLTUdGPMEM=',None,u'rolf',u'900',u'',u'Rolf',u'Rompen',u'','01',None,None))
loader.save(create_users_user(1,u'demo@example.com',u'en',dt(2018,10,22,12,56,25),dt(2018,10,22,12,56,5),None,None,u'30',None,u'pbkdf2_sha256$36000$0AeN832KbrQZ$vlK2D+pMkryV5BN/doL6qfRtSjRMZ8Ld1Uy+ROBcuQw=',None,u'robin',u'900',u'',u'Robin',u'Rood',u'','01',None,None))

loader.flush_deferred_objects()
