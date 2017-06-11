# -*- coding:utf-8 -*-
from collections import Sequence


class LogLiner(Sequence):
    def __init__(self):
        self.list = []

    def __getitem__(self, index):
        if self.list is None:
            self.list = []
        return self.list[index]

    def __len__(self):
        return len(self.list) if self.list else 0

    def append(self, log):
        if self.list is None:
            self.list = []
        self.list.append(log)

    def extend(self, log_list):
        if self.list is None:
            self.list = []

        self.list.extend(log_list)

    def clear(self):
        self.list = []

    def get_sorted_list(self):
        return sorted(self.list, key=lambda x : x.date)
