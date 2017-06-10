import logging

global fh
fh = ''

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fh = logging.FileHandler('monitor.txt')
fh.setLevel(logging.INFO)

fh.setFormatter(formatter)

logger.addHandler(fh)
