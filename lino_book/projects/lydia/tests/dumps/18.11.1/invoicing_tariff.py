# -*- coding: UTF-8 -*-
logger.info("Loading 2 objects to table invoicing_tariff...")
# fields: id, designation, number_of_events, min_asset, max_asset
loader.save(create_invoicing_tariff(1,['By presence', 'Pro Anwesenheit', 'By presence'],1,None,None))
loader.save(create_invoicing_tariff(2,['Maximum 10', 'Maximum 10', 'Maximum 10'],1,None,10))

loader.flush_deferred_objects()
