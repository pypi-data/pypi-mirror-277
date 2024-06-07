import importlib

import json

from anicli_api.base import BaseExtractor, BaseOngoing
from flask import Flask, render_template, request, jsonify

from anicli import get_modules
# from anicli_api.base import BaseExtractor, BaseOngoing

app = Flask('anicli-ru',
            template_folder='anicli/web/templates',
            static_folder='anicli/web', static_url_path='/')

MODULES = [m for m in get_modules()]


@app.get('/')
def index():
    return render_template('index.html',
                           modules=MODULES,
                           json=json)

@app.get('/ongoings')
def ongoings():
    extractor: BaseExtractor = app.config['EXTRACTOR']
    ongs: list[BaseOngoing] = extractor.ongoing()
    return ("<ul>" + "\n".join([f'<li><h2>{o.title}</h2><img src="{o.thumbnail}"</li><input type="button" value="{i}">' for i, o in enumerate(ongs)])
            + "</ul>")


if __name__ == '__main__':
    app.run(debug=True)
