# -*- coding: UTF-8 -*-
logger.info("Loading 5 objects to table contacts_roletype...")
# fields: id, name
loader.save(create_contacts_roletype(1,['Manager', 'Gesch\xe4ftsf\xfchrer', 'G\xe9rant']))
loader.save(create_contacts_roletype(2,['Director', 'Direktor', 'Directeur']))
loader.save(create_contacts_roletype(3,['Secretary', 'Sekret\xe4r', 'Secr\xe9taire']))
loader.save(create_contacts_roletype(4,['IT Manager', 'EDV-Manager', 'G\xe9rant informatique']))
loader.save(create_contacts_roletype(5,['President', 'Pr\xe4sident', 'Pr\xe9sident']))

loader.flush_deferred_objects()
