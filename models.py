# -*- coding:utf-8 -*-
from datetime import datetime


class Log(object):
    def __init__(self, date, log, log_file):
        self.log = log
        self.log_file = log_file
        if isinstance(date, datetime):
            self.date = date
        else:
            raise Exception('date parameter need datetime type.')

    def __str__(self):
        return self.log

    def __repr__(self):
        return self.log

    @property
    def base_file_name(self):
        from os.path import basename
        return basename(self.log_file)
