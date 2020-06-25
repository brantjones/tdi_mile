from flask import Flask,render_template,request
import pandas as pd
from bokeh.embed import components
from bokeh.plotting import figure
import numpy as np

app = Flask(__name__)
app.vars = {}

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
      return render_template('index.html')
    else:
      app.vars['name'] = request.form['name_lulu']
      app.vars['age'] = request.form['age_lulu']

      # Create the plot
      data = pd.DataFrame(np.array([1, 2, 3, int(app.vars['name']), int(app.vars['age'])  ]))
      hist, edges = np.histogram(data, density=True, bins=50)
      plot = figure()
      plot.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], line_color="white")
		
      # Embed plot into HTML via Flask Render
      script, div = components(plot)
      return render_template("iris_index1.html", script=script, div=div)

if __name__ == "__main__":
    app.run(debug=True)
