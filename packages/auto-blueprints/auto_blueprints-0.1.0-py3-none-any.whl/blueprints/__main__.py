from flask import Flask
from blueprints import register_blueprints, parse_arguments

args = parse_arguments()
app = Flask(__name__)
register_blueprints('blueprints.txt', app)

context = {
    'host': args.host,
    'port': args.port,
}

try:
    from waitress.server import create_server
    print(f"Serving requests on http://{args.host}:{args.port}")
    server = create_server(app, **context)
    server.run()
except ImportError:
    app.run(**context)
