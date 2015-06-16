# -*- coding utf-8 -*-
import json
import logging
import logging.handlers

LOG_FILE='autoDeploy.log'

# 实例化handler
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5)   
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'  

