# -*- coding:utf-8 -*-
from base import BaseDateExtractor
from datetime import datetime


class CustomDateExtractor(BaseDateExtractor):
    @staticmethod
    def extract(log):
        try:
            splitted_log = log.split('\t')
            if len(splitted_log) > 2:
                if splitted_log[1]:
                    return datetime.strptime(splitted_log[1],  '%Y-%m-%d %H:%M:%S,%f')
            else:
                return None
        except Exception:
            import traceback
            print(traceback.format_exc())
            return None
