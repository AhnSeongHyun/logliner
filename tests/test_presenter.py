import unittest


class BasePresenterTestCase(unittest.TestCase):
    def test_present(self):
        pass


class BaseFilePresenterTestCase(unittest.TestCase):
    def test_present(self):
        pass


class PresenterFactoryTestCase(unittest.TestCase):
    def test_get_presenter(self):
        pass


class StreamPresenterTestCase(unittest.TestCase):
    def test_present(self):
        pass


class FilePresenterTestCase(unittest.TestCase):
    def test_present(self):
        pass

class HTMLPresenterTestCase(unittest.TestCase):
    def test_render_template(self):
        pass

    def test_present(self):
        pass


if __name__ == '__main__':
    unittest.main()
