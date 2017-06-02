
class BasePresenter(object):

    def present(self, result):
        raise NotImplementedError


class BaseFilePresenter(BasePresenter):
    def __init__(self, path):
        self.path = path

    def present(self, result):
        super(BaseFilePresenter, self).present(result)
        raise NotImplementedError


class PresenterFactory(object):

    @staticmethod
    def get_presenter(format='file', path=None):

        d = dict()
        d['file'] = FilePresenter(path=path)
        d['html'] = HTMLPresenter(path=path)
        d['stdout'] = StreamPresenter()
        return d[format]


class StreamPresenter(BasePresenter):

    def present(self, result):
        for r in result:
            print r


class FilePresenter(BaseFilePresenter):

    def present(self, result):
        with open(self.path, 'w') as f:
            f.writelines(str(result))


class HTMLPresenter(BaseFilePresenter):
    def present(self, result):
        with open(self.path, 'w') as f:
            f.writelines(result)





