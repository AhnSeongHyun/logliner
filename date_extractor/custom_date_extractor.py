# -*- coding:utf-8 -*-
from base import BaseDateExtractor
from datetime import datetime


class CustomDateExtractor(BaseDateExtractor):
    @staticmethod
    def extract(log):
        try:
            splited_log = log.split('\t')
            if len(splited_log) > 2:
                if splited_log[1]:
                    return datetime.strptime(splited_log[1],  '%Y-%m-%d %H:%M:%S,%f')
            else:
                return None
        except Exception:
            import traceback
            print(traceback.format_exc())
            return None
