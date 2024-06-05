from mango import *

def simple_cors_middleware(app):
    def cors_wrapper(environ, start_response):
        def custom_start_response(status, response_headers, exc_info=None):
            response_headers.append(('Access-Control-Allow-Origin', '*'))
            response_headers.append(('Access-Control-Allow-Methods', 'GET, POST, OPTIONS'))
            response_headers.append(('Access-Control-Allow-Headers', 'Content-Type'))
            if environ['REQUEST_METHOD'] == 'OPTIONS':
                response_headers.append(('Content-Length', '0'))
                start_response('204 No Content', response_headers, exc_info)
                return [b'']
            return start_response(status, response_headers, exc_info)
        return app(environ, custom_start_response)
    return cors_wrapper

# Wrap the Mango app with the CORS middleware
app = simple_cors_middleware(app)


@route('/')
def index(post=None):
    if post:
        data = get_json(post)
        return f"Hello, {data['name']} !"
    return "Hello, World!"

run()
