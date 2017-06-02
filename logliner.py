# -*- coding:utf-8 -*-
import argparse
from multiprocessing import Pool

from attrdict import AttrDict

from containers import LogLiner
from models import Log
from presenter import PresenterFactory


def task_parser(file_path, q, date_extractor):
    x = []
    with open(file_path, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            if q in line:
                d = date_extractor.extract(line)
                x.append(Log(log=line, date=d, log_file=file_path))
    return x


def task(args):
    return task_parser(*args)


def create_custom_date_extractor(class_path):

    import importlib
    class_path_splited = class_path.split('.')
    count = len(class_path_splited)
    last = count - 1
    if count > 1:
        module = importlib.import_module(".".join(class_path_splited[:last]))
        return getattr(module, class_path_splited[last])
    else:
        raise Exception('Wrong custom date extractor class path')


def get_config(conf_file_path):
    from yaml import load

    try:
        from yaml import CLoader as Loader, CDumper as Dumper
    except ImportError:
        from yaml import Loader, Dumper

    stream = file(conf_file_path, 'r')
    data = load(stream, Loader=Loader)
    return data

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", help="conf file(.yaml)")
    args = parser.parse_args()

    conf = AttrDict(get_config(args.c))

    input_file_list = conf.input
    q = str(conf.q)
    class_path = conf.date_extractor

    log_liner = LogLiner()
    custom_date_extractor_class = create_custom_date_extractor(class_path=class_path)
    if input_file_list and q and custom_date_extractor_class:
        pool = Pool(processes=len(input_file_list))
        map_result = pool.map(task, [(i, q, custom_date_extractor_class) for i in input_file_list])
        pool.close()
        pool.join()

        for result in map_result:
            log_liner.extend(result)

        sorted_result = log_liner.get_sorted_list()

        presenter = PresenterFactory.get_presenter(format=conf.output.format, path=conf.output.path)
        presenter.present(sorted_result)

    else:
        print("ERROR ")

