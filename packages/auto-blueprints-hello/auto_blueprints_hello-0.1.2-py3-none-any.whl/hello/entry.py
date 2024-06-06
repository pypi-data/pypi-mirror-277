import os

from flask import Blueprint, render_template, request
"""
Hello blueprint
"""

bp_dir = os.path.dirname(__file__)
templates_dir = os.path.join(bp_dir, 'templates')
bp = Blueprint('hello', __name__, template_folder=templates_dir)


@bp.route('/<world>', methods=['GET'])
def hello_world(world):
    context = {'hello': world}
    return render_template('hello/hello.html', **context)


@bp.route('/', methods=['POST'])
def hello():
    context = {'hello': request.form['world']}
    return render_template('hello/hello.html', **context)


@bp.route('/', methods=['GET'])
def entry():
    context = {'hello': 'world'}
    return render_template('hello/hello.html', **context)
