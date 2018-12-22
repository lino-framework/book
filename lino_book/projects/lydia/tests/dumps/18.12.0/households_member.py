# -*- coding: UTF-8 -*-
logger.info("Loading 12 objects to table households_member...")
# fields: id, start_date, end_date, title, first_name, middle_name, last_name, gender, birth_date, role, person, household, dependency, primary
loader.save(create_households_member(1,None,None,u'',u'J\xe9r\xf4me',u'',u'Jean\xe9mart',u'M',u'','01',181,182,'02',False))
loader.save(create_households_member(2,None,None,u'',u'Lisa',u'',u'Lahm',u'F',u'','03',176,182,'02',False))
loader.save(create_households_member(3,None,None,u'',u'Denis',u'',u'Denon',u'M',u'','01',180,183,'02',False))
loader.save(create_households_member(4,None,None,u'',u'Marie-Louise',u'',u'Vandenmeulenbos',u'F',u'','03',174,183,'02',False))
loader.save(create_households_member(5,None,date(2002,3,4),u'',u'Robin',u'',u'Dubois',u'M',u'','01',179,184,'02',False))
loader.save(create_households_member(6,None,None,u'',u'Erna',u'',u'\xc4rgerlich',u'F',u'','03',169,184,'02',False))
loader.save(create_households_member(7,None,None,u'',u'Karl',u'',u'Keller',u'M',u'','01',178,185,'02',False))
loader.save(create_households_member(8,None,None,u'',u'\xd5ie',u'',u'\xd5unapuu',u'F',u'','03',167,185,'02',False))
loader.save(create_households_member(9,None,None,u'',u'Bernd',u'',u'Brecht',u'M',u'','01',177,186,'02',False))
loader.save(create_households_member(10,None,None,u'',u'Inge',u'',u'Radermacher',u'F',u'','03',162,186,'02',False))
loader.save(create_households_member(11,None,None,u'',u'Robin',u'',u'Dubois',u'M',u'','01',179,187,'02',False))
loader.save(create_households_member(12,None,None,u'',u'Hedi',u'',u'Radermacher',u'F',u'','03',161,187,'02',False))

loader.flush_deferred_objects()
