from pyramid.config import Configurator
from pyramid.response import response

def hello_world(request):
	return Response(
       'Hello world from Pyramid!\n',
       content_type='text/plain',
		)


config = Configurator()
config.add_route('hello', '/hello')
config.add_view(hellow_world, route_name='hello')
app = config.make_wsgi_app()
