import logging
from logging.handlers import RotatingFileHandler

# Constant
logging_format = logging.Formatter('%(message)s')

# Logger and Logging Files
funnel_logger = logging.getLogger('FunnelLogger')
funnel_logger.setLevel(logging.INFO)
funnel_handler = RotatingFileHandler('audits.log', maxBytes=2000, backupCount=5)
funnel_handler.setFormatter(logging_format)