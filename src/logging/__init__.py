import logging
import os
import sys


log_dir = 'log'
log_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"
filename = os.path.join(log_dir,'looping.log')
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=log_str,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(filename)
    ]
)

logger = logging.getLogger('Customer_feedback_analyser')