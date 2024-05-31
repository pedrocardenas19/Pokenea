import random
import os

def get_random_pokenea():
    from .models import POKENEAS
    return random.choice(POKENEAS)

def get_container_id():
    return os.uname().nodename
