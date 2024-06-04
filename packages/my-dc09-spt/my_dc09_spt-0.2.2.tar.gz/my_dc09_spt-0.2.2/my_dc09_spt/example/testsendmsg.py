# ----------------------------
# Test dialler to show use of dc09_msg class
# (c 2018 van Ovost Automatisering b.v.
# Author : Jacq. van Ovost
# ----------------------------
import sys

sys.path.append('../')
from my_dc09_spt import dc09_spt

import logging
logging.basicConfig(format='%(module)-12s %(asctime)s %(levelname)-8s %(message)s')
logger = logging.getLogger()
#handler = logging.StreamHandler()
#logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

ACCOUNT_ID = "YA247940"

spt1 = dc09_spt.dc09_spt(ACCOUNT_ID)
spt1.set_path('main', 'primary', "localhost", 1001, account=ACCOUNT_ID, type='TCP')
spt1.set_path('main', 'secondary', "localhost", 1001, account=ACCOUNT_ID, type='TCP')

try:
    spt1.send_msg('ADM-CID', {
        'account': 'YA247940',
        'code': 121,
        'q': 1,
        'event_ts': 1717428918000,
        'alt': 0,
        'gps_position': 'N00.00.00,0 E00.00.00,0'
    })
except Exception as e:
    print(e)
    logging.error('Error sending message')