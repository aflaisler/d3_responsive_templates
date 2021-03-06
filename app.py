import json
from flask import Flask, render_template, url_for
import numpy as np
import pandas as pd


app = Flask(__name__)


@app.route('/')
def index():
    '''
    When you request the root path, you'll get the index.html template.

    '''
    return render_template('index.html', links=all_links())


@app.route('/simpleGraph')
def simpleGraph():
    return render_template('simple-graph.html')


@app.route('/multipleLines')
def multipleLines():
    return render_template('multiple-lines.html')


@app.route('/interpolate')
def interpolate():
    return render_template('interpolate.html')


@app.route('/interactiveTree')
def interactiveTree():
    return render_template('interactive-tree.html')


@app.route('/simple_graph_plus_table_plus_addins')
def simple_graph_plus_table_plus_addins():
    return render_template('simple-graph-plus-table-plus-addins.html')


@app.route('/graphForce')
def graphForce():
    return render_template('graphForce.html')


@app.route('/d3graphData')
def d3graphData():
    with open('./data/graph.json', 'rb') as f:
        data = json.load(f)
    return json.dumps(data)


@app.route('/d3data')
def get_data(filename='data2.csv'):
    data = pd.read_csv('./data/' + filename)
    key = data.columns
    return json.dumps([{key[i]: data.loc[j, key[i]] for i in range(data.shape[1])} for j in range(data.shape[0])])


@app.route('/d3data2')
def get_data2(filename='data2.csv'):
    data = pd.read_csv('./data/' + filename)
    key = data.columns
    return json.dumps([{key[i]: data.loc[j, key[i]] for i in range(data.shape[1])} for j in range(data.shape[0])])


@app.route('/d3data3')
def get_data3(filename='data-3.csv'):
    data = pd.read_csv('./data/' + filename)
    key = data.columns
    return json.dumps([{key[i]: data.loc[j, key[i]] for i in range(data.shape[1])} for j in range(data.shape[0])])


@app.route('/d3data4')
def get_data4(filename='data-4.csv'):
    data = pd.read_csv('./data/' + filename)
    key = data.columns
    return json.dumps([{key[i]: data.loc[j, key[i]] for i in range(data.shape[1])} for j in range(data.shape[0])])


def all_links():
    links = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    return links


@app.route('/data')
@app.route('/data/<int:ndata>')
def data(ndata=500):
    '''
    On request, this returns a list of ``ndata`` randomly made data points.

    :param ndata: (optional)
        The number of data points to return.

    :returns data:
        A JSON string of ``ndata`` data points.

    '''
    x = 10 * np.random.rand(ndata) - 5
    y = 0.5 * x + 0.5 * np.random.randn(ndata)
    A = 10. ** np.random.rand(ndata)
    c = np.random.rand(ndata)
    return json.dumps([{'_id': i, 'x': x[i], 'y': y[i], 'area': A[i],
                        'color': c[i]}
                       for i in range(ndata)])


if __name__ == '__main__':
    import os

    port = 8000

    # Open a web browser pointing at the app.
    # os.system('open http://localhost:{0}'.format(port))

    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)
