import os
from pathlib import Path
import logging
import logging.config
from logging.handlers import TimedRotatingFileHandler

class SafeTimedRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, filename, when='midnight', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None, errors=None):
        #get the directory path from of the package to put log file
        config_path = Path(__file__).resolve().parent
        filePath = config_path.__str__ ()+ '\\logs\\' + filename

        # Ensure the directory exists
        os.makedirs(os.path.dirname(filePath), exist_ok=True)

        super().__init__(filePath, when, interval, backupCount, encoding, delay, utc, atTime, errors)

                # Add blank lines to separate logs from previous runs
        self._add_blank_lines()

    def _add_blank_lines(self, num_lines=5):
        with open(self.baseFilename, 'a', encoding=self.encoding) as log_file:
            log_file.write('\n' * num_lines)
