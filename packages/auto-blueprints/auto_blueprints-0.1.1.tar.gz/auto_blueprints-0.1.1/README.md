# Blueprints

Blueprints is a library to perform auto-discovery of Flask blueprints
by scanning the installed packages for blueprints.txt files.

## Discovery

Discovery of blueprints is performed by the register_blueprints method.
All discovered blueprints are stored in a blueprints attribute of the blueprints package.
The attribute is a dictionary containing the blueprint name and associated meta data.

If a blueprint has the url_prefix specified then it is used.
Otherwise, the package name containing the blueprint is used as the url_prefix.

## Installation

    pip install --upgrade auto-blueprints

## Running

Blueprints can be run as a module.

    python -m blueprints

Blueprints can be run as a command line executable.

    blueprints --host 127.0.0.1 --port 5000

If waitress is installed then a server using waitress is started.
If waitress is not installed then the flask development server is started.

## Embedding

Blueprints can be embedded in an existing program very simply.

    from flask import Flask
    from blueprints import register_blueprints
    app = Flask(__name__)
    register_blueprints('blueprints.txt', app)
    app.run()

## blueprints.txt format

The blueprints.txt file is a multi-line file containing one line per blueprint to import.
The structure of the line is <package>.<module>.<blueprint>.

    hello.entry.bp  => imports hello.entry and retrieves the bp attribute containing a flask blueprint

## License

MIT Licensed
