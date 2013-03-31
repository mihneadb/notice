from notice import app

from flask import render_template
from flask.views import MethodView


class TemplateView(MethodView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        return {}

    def get(self, **kwargs):
        return render_template(self.template_name, **self.get_context_data(**kwargs))


class HomePage(TemplateView):
    template_name = 'homepage.html'

app.add_url_rule('/', view_func=HomePage.as_view('homepage'))

