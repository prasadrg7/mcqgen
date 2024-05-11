import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(), 'logs')
logfile_path = os.path.join(log_path, LOG_FILE)

os.makedirs(log_path, exist_ok=True)

logging.basicConfig(level=logging.INFO,
                    filename=logfile_path,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
                    )

