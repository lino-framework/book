# -*- coding: UTF-8 -*-
logger.info("Loading 16 objects to table sheets_accountentry...")
# fields: id, report, old_d, old_c, during_d, during_c, account
loader.save(create_sheets_accountentry(1,1,'0.00','0.00','18500.00','13836.75',2))
loader.save(create_sheets_accountentry(2,1,'0.00','0.00','9250.00','22044.44',3))
loader.save(create_sheets_accountentry(3,1,'0.00','0.00','22044.44','27556.94',4))
loader.save(create_sheets_accountentry(4,1,'0.00','0.00','178.24','297.46',7))
loader.save(create_sheets_accountentry(5,1,'0.00','0.00','0.00','178.24',6))
loader.save(create_sheets_accountentry(6,1,'0.00','0.00','0.00','4586.75',12))
loader.save(create_sheets_accountentry(7,1,'0.00','0.00','17620.40','0.00',15))
loader.save(create_sheets_accountentry(8,1,'0.00','0.00','3520.00','0.00',16))
loader.save(create_sheets_accountentry(9,1,'0.00','0.00','6714.00','0.00',14))
loader.save(create_sheets_accountentry(10,1,'0.00','0.00','0.00','9620.00',19))
loader.save(create_sheets_accountentry(11,1,'0.00','0.00','0.00','8880.00',27))
loader.save(create_sheets_accountentry(12,1,'0.00','0.00','49972.68','63913.83',21))
loader.save(create_sheets_accountentry(13,1,'0.00','0.00','0.00','4586.75',22))
loader.save(create_sheets_accountentry(14,1,'0.00','0.00','27854.40','0.00',23))
loader.save(create_sheets_accountentry(15,1,'0.00','0.00','27854.40','0.00',24))
loader.save(create_sheets_accountentry(16,1,'0.00','0.00','0.00','18500.00',26))

loader.flush_deferred_objects()
