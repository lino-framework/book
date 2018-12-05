# -*- coding: UTF-8 -*-
logger.info("Loading 6 objects to table users_user...")
# fields: id, email, language, modified, created, start_date, end_date, access_class, event_type, password, last_login, username, user_type, initials, first_name, last_name, remarks, time_zone, cash_daybook, team, partner
loader.save(create_users_user(4,u'',u'en',dt(2018,12,4,19,9,56),dt(2018,12,4,19,9,24),None,None,u'30',4,u'pbkdf2_sha256$36000$D04F2RBdBG8F$nNhVKmmrBK6gS1i4oeSewL+hio2XxW5NwR4UacFc/Bg=',None,u'daniel',u'200',u'',u'Daniel',u'',u'','01',4,None,None))
loader.save(create_users_user(5,u'',u'en',dt(2018,12,4,19,9,56),dt(2018,12,4,19,9,24),None,None,u'30',5,u'pbkdf2_sha256$36000$elyvIAc6TUaL$8mxgxLagVXEQMzmgqKjtBymTAdgDunMBdM4A0PTggZA=',None,u'elmar',u'200',u'',u'Elmar',u'',u'','01',None,None,None))
loader.save(create_users_user(6,u'',u'en',dt(2018,12,4,19,9,56),dt(2018,12,4,19,9,24),None,None,u'30',None,u'pbkdf2_sha256$36000$fjG6RiIt2DAd$5KTrF3WEMcIdkKeayhH1agbSqlCvd0t3dRezpR9E28I=',None,u'lydia',u'100',u'',u'Lydia',u'',u'','01',None,None,None))
loader.save(create_users_user(3,u'demo@example.com',u'fr',dt(2018,12,4,19,9,56),dt(2018,12,4,19,9,19),None,None,u'30',None,u'pbkdf2_sha256$36000$jV86TbFukmwk$XIJzmllDupgiWBCF6iPiPzgnc66mrJqZVQuNqhVMZGM=',None,u'romain',u'900',u'',u'Romain',u'Raffault',u'','01',None,None,None))
loader.save(create_users_user(2,u'demo@example.com',u'de',dt(2018,12,4,19,9,56),dt(2018,12,4,19,9,19),None,None,u'30',None,u'pbkdf2_sha256$36000$qvcc7XNUXJ7X$fkMg8v2wZZtrNHvd2qRBlSR2HjF4FWjKHQwkFv+TmkU=',None,u'rolf',u'900',u'',u'Rolf',u'Rompen',u'','01',None,None,None))
loader.save(create_users_user(1,u'demo@example.com',u'en',dt(2018,12,4,19,9,56),dt(2018,12,4,19,9,19),None,None,u'30',None,u'pbkdf2_sha256$36000$HFcGvFPuHPQc$i8BEakbt1XEtGYzfXpqp0Urxb9xHvXjh8kljDW4Ax5o=',None,u'robin',u'900',u'',u'Robin',u'Rood',u'','01',None,None,None))

loader.flush_deferred_objects()
