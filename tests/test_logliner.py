import unittest


class LoglinerTestCase(unittest.TestCase):
    def test_task_parser(self):
        self.assertEqual(True, False)

    def test_create_custom_date_extractor(self):
        self.assertEqual(True, False)

    def test_get_config(self):
        from logliner.logliner import get_config
        get_config(conf_file_path="not_exist.conf")
        conf1 = get_config(conf_file_path="./tests/test_conf.yaml")
        conf2 = get_config(conf_file_path="./tests/test_empty_conf.yaml")

        self.assertEqual(conf1['date_extractor'], 'test')
        self.assertEqual(len(conf2), 0)


    def test_print_conf(self):
        from logliner.logliner import print_conf
        try:
            print_conf(conf=None)
            print_conf(conf=1)
            print_conf(conf="string")
            print_conf(conf=[1, 2, 3])
            print_conf(conf={"test1": 123, "test2": 456})
        except Exception:
            import traceback
            self.fail(traceback.format_exc())


if __name__ == '__main__':
    unittest.main()
