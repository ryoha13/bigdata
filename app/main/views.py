import json
from flask import render_template
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    language = ['python', 'java', 'c', 'c++', 'c#', 'php']
    value = ['100', '150', '100', '90', '80', '90']
    data = {'language': language, 'value': value}
    data_json = json.dumps(data)
    return render_template('main/index.html', data_json=data_json, language=language, value=value)
