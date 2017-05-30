import argparse

from collections import Sequence
from multiprocessing import Pool

class Log(object):
    def __init__(self, log):
        self.log = log
    def __str__(self):
        return self.log

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


def task_parser(file_path, q):
    x = []
    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if q in line:
                x.append(Log(log=line))
    return x

def task(args):
    print args
    return task_parser(*args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-input", help='input file path list', nargs="*")
    parser.add_argument("-output", help='output file path')
    parser.add_argument("-q", help="searching keyword")
    args = parser.parse_args()

    input_file_list = args.input
    output_file_path = args.output
    q = args.q

    log_liner = LogLiner()

    if input_file_list and output_file_path and q:
        pool = Pool(processes=len(input_file_list))
        map_result = pool.map(task, [(i, q) for i in input_file_list])
        pool.close()
        pool.join()
        #
        # print len(map_result)
        # print type(map_result[0]), len(map_result[0])
        # print type(map_result[1]), len(map_result[1])

        for result in map_result:
            log_liner.extend(result)

        print len(log_liner)
        for l in log_liner:
            print '='*100
            print l
    else:
        print("ERROR ")



# python loglin.py -out merge.txt -in in1.txt in2.txt
# loglin -out merge.txt -in in1.txt in2.txt
# python loglin.py -output 12 -input ./log_files/a.log ./log_files/b.log -q 201705301451479331561400
