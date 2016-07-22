from lino.api import dd
dd.logger.info("pinglog via dd.logger.info()")
import logging
logging.getLogger('django').info("pinglog to logger django")
logging.getLogger('lino').info("pinglog to logger lino")
logging.getLogger('lino.foo').info("pinglog to logger lino.foo")
logging.getLogger('foo.lino').info("pinglog to logger foo.lino")
