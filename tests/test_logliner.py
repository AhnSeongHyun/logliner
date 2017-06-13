

import pytest


def test_task_parser():
    pass


def test_create_custom_date_extractor():
    pass


def test_get_config():
    from logliner.logliner import get_config
    get_config(conf_file_path="not_exist.conf")
    conf1 = get_config(conf_file_path="./tests/test_conf.yaml")
    conf2 = get_config(conf_file_path="./tests/test_empty_conf.yaml")
    print(conf1)
    assert conf1['date_extractor'] == 'test'
    assert conf2 is None


def test_print_conf():
    from logliner.logliner import print_conf
    try:
        print_conf(conf=None)
        print_conf(conf=1)
        print_conf(conf="string")
        print_conf(conf=[1, 2, 3])
        print_conf(conf={"test1": 123, "test2": 456})
    except Exception:
        assert False


