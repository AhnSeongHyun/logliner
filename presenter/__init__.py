
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
    def get_presenter(format='file', path=None, q=''):

        d = dict()
        d['file'] = FilePresenter(path=path)
        d['html'] = HTMLPresenter(path=path, q=q)
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

    template = """
    <html>
    <meta charset=utf-8> <meta content="IE=edge" http-equiv=X-UA-Compatible> <meta content="width=device-width,initial-scale=1" name=viewport>
    <head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    </head>
    <body>
    <div class='container'>
    <h3> Report<h3>
    <hr/>
    <h4> - created at :  {{ created_at }}</h4>
    <h4> - log files :  {{ log_file_list }}</h4>
    <hr/>
    <br/>

    {% for log in result %}
        <div class="panel panel-info">
            <div class="panel-heading"><strong>date</strong>: {{ log.date }}    <strong>file</strong>:{{ log.base_file_name }}</div>
            <div class="panel-body" style="word-break:break-all">
                {{ log | code_tag }}
            </div>
        </div>
    {%endfor%}
    </div>
    </body>
    <html>
    """

    def __init__(self, path, q):
        super(HTMLPresenter, self).__init__(path=path)
        self.q = q

    def _render_template(self, result):
        from jinja2 import Environment
        from datetime import datetime
        log_file_list = set()
        for log in result:
            log_file_list.add(log.log_file)

        env = Environment()

        def code_tag(input):
            s = str(input).split(self.q)
            return ('<code>' + self.q + '</code>').join(s)
        env.filters['code_tag'] = code_tag

        return env.from_string(self.template).render(log_file_list=", ".join(log_file_list),
                                                               result=result,
                                                               created_at = datetime.now()
                                                               )

    def present(self, result):
        html = self._render_template(result)
        with open(self.path, 'w') as f:
            f.write(html)





