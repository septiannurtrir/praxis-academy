from flask import Flask, request

from flask.views import MethodView

class GenericRequest(MethodView):
    def get(self):
        name = request.args.get('name', 'Damyan')
        return 'Hello GET from %s!' % name

    def post(self):
        name = request.form.get('name', 'Damyan')
        return 'Hello POST from %s' % name

app.add_url_rule(
    '/generic_request',
    view_func=GenericRequest.as_view('generic_request')
)
