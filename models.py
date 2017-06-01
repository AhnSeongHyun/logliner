
from datetime import datetime

class Log(object):
    def __init__(self, date, log):
        self.log = log
        if isinstance(date, datetime):
            self.date = date
        else:
            raise Exception('date parameter need datetime type.')

    def __str__(self):
        return self.log
