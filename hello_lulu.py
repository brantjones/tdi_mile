from flask import Flask,render_template,request
import pandas as pd
from bokeh.embed import components
from bokeh.plotting import figure
#from bkcharts import Histogram
import numpy as np
#from bokeh import Histogram

# Load the Iris Data Set
#iris_df = pd.read_csv("data/iris.data", 
#    names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
#feature_names = iris_df.columns[0:-1].values.tolist()

app_lulu = Flask(__name__)
app_lulu.vars = {}

@app_lulu.route('/index_lulu',methods=['GET','POST'])
def index_lulu():
    if request.method == 'GET':
      return render_template('getinfo.html')
    else:
      app_lulu.vars['name'] = request.form['name_lulu']
      app_lulu.vars['age'] = request.form['age_lulu']

      # Create the plot
      data = pd.DataFrame(np.array([1, 2, 3, int(app_lulu.vars['name']), int(app_lulu.vars['age'])  ]))
      hist, edges = np.histogram(data, density=True, bins=50)
      plot = figure()
      plot.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], line_color="white")
		
      # Embed plot into HTML via Flask Render
      script, div = components(plot)
      return render_template("iris_index1.html", script=script, div=div)

if __name__ == "__main__":
    app_lulu.run(debug=True)
