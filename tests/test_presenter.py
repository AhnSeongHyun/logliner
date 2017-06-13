import unittest


class BasePresenterTestCase(unittest.TestCase):
    def test_present(self):
        self.assertEqual(True, False)


class BaseFilePresenterTestCase(unittest.TestCase):
    def test_present(self):
        self.assertEqual(True, False)


class PresenterFactoryTestCase(unittest.TestCase):
    def test_get_presenter(self):
        self.assertEqual(True, False)


class StreamPresenterTestCase(unittest.TestCase):
    def test_present(self):
        self.assertEqual(True, False)


class FilePresenterTestCase(unittest.TestCase):
    def test_present(self):
        self.assertEqual(True, False)


class HTMLPresenterTestCase(unittest.TestCase):
    def test_render_template(self):
        self.assertEqual(True, False)

    def test_present(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
