'''
This file is part of the flask+d3 Hello World project.
'''
import json
from flask import Flask, render_template
import numpy as np
import pandas as pd


app = Flask(__name__)


@app.route('/')
def index():
    '''
    When you request the root path, you'll get the index.html template.

    '''
    return render_template('index.html')


@app.route('/simpleGraph')
def simpleGraph():
    return render_template('simple-graph.html', data_=data(1000))


@app.route('/d3data')
def get_data(filename='data.csv'):
    data = pd.read_csv('./data/' + filename)
    return json.dumps([{'date': data.iloc[i, 0], 'close': data.iloc[i, 1]} for i in range(data.shape[0])])


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
    os.system('open http://localhost:{0}'.format(port))

    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)