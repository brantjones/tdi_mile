from flask import Flask,render_template,request
import pandas as pd
from bokeh.embed import components
from bokeh.plotting import figure
import numpy as np
import requests
import simplejson as json

app = Flask(__name__)
app.vars = {}

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
      return render_template('index.html')
    else:
      app.vars['name'] = request.form['name_lulu']

      r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+app.vars['name']+'&interval=5min&apikey=XCXQ9NU0YYDJ5C9NXCXQ9NU0YYDJ5C9N')
      rd = r.json()
      data = rd["Time Series (5min)"]
      ret = []
      for key in data.keys():
        ret.append(data[key]["4. close"])
      #ret.pop(-1)
      #ret.pop(-1)
      #print(ret)

      df = pd.Series(ret)
      

      #df = pd.read_json('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=XCXQ9NU0YYDJ5C9NXCXQ9NU0YYDJ5C9N')
      #print "ok."

      # Create the plot
      #data = pd.DataFrame(np.array([1, 2, 3, int(app.vars['name']), int(app.vars['age'])  ]))
      #hist, edges = np.histogram(data, density=True, bins=50)
      ##khist, edges = np.histogram(df, density=True, bins=50)
      plot = figure()
      plot.line(range(len(ret)), ret)
      #plot.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], line_color="white")
		
      # Embed plot into HTML via Flask Render
      script, div = components(plot)
      #return render_template("ii.html", script=script, div=div, notes=df, name=app.vars['name'])
      return render_template("ii.html", script=script, div=div, name=app.vars['name'])

if __name__ == "__main__":
    app.run(debug=True)
