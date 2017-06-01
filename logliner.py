# -*- coding:utf-8 -*-
import argparse
from multiprocessing import Pool

from containers import LogLiner
from models import Log


def task_parser(file_path, q, date_extractor):
    x = []
    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if q in line:
                d = date_extractor.extract(line)
                x.append(Log(log=line, date=d))
    return x


def task(args):
    print args
    return task_parser(*args)


def create_custom_date_extractor(class_path):

    import importlib
    class_path_splitted = class_path.split('.')
    count = len(class_path_splitted)
    last = count -1
    if count > 1:
        module = importlib.import_module(".".join(class_path_splitted[:last]))
        custom_date_extractor_class = getattr(module, class_path_splitted[last])
        return custom_date_extractor_class
    else:
        raise Exception('Wrong custom date extractor class path')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-input", help='input file path list', nargs="*")
    parser.add_argument("-output", help='output file path')
    parser.add_argument("-q", help="searching keyword")
    parser.add_argument("-c", help="data extractor class, my_package.my_module.MyClass")
    args = parser.parse_args()

    input_file_list = args.input
    output_file_path = args.output
    q = args.q
    class_path = args.c
    log_liner = LogLiner()
    custom_date_extractor_class = create_custom_date_extractor(class_path=class_path)
    if input_file_list and output_file_path and q:
        pool = Pool(processes=len(input_file_list))
        map_result = pool.map(task, [(i, q, custom_date_extractor_class) for i in input_file_list])
        pool.close()
        pool.join()

        for result in map_result:
            log_liner.extend(result)

        sorted = log_liner.get_sorted_list()
        for s in sorted:
            print s

    else:
        print("ERROR ")

# python logliner.py -output 12 -input ./log_files/a.log ./log_files/b.log -q 201705301451479331561400 -c date_extractor.custom_date_extractor.CustomDateExtractor
