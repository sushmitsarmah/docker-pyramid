# pyramid hello_world/app.py

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

print("started",__name__)

def hello_world(request):
    print('Request inbound!')
    return Response('Docker works with Pyramid!')

if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 5000, app)
    print("sushmit")
    server.serve_forever()
