#logging is displaying msgs, i is used to log msgs
#there are 5 ways to logging

import logging
'''logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')'''


#logging basic configurations

logging.basicConfig(filename='mylog.log',level=logging.DEBUG)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')
