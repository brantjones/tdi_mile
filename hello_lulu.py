from flask import Flask,render_template,request
import pandas as pd
from bokeh.charts import Histogram
from bokeh.embed import components

# Load the Iris Data Set
iris_df = pd.read_csv("data/iris.data", 
    names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Species"])
feature_names = iris_df.columns[0:-1].values.tolist()

app_lulu = Flask(__name__)
app_lulu.vars = {}

# Create the main plot
def create_figure(current_feature_name, bins):
	p = Histogram(iris_df, current_feature_name, title=current_feature_name, color='Species', 
	 	bins=bins, legend='top_right', width=600, height=400)

	# Set the x axis label
	p.xaxis.axis_label = current_feature_name

	# Set the y axis label
	p.yaxis.axis_label = 'Count'
	return p

@app_lulu.route('/index_lulu',methods=['GET','POST'])
def index_lulu():
    if request.method == 'GET':
      return render_template('getinfo.html')
    else:
      ##return 'mpost.'
      ##request was a POST
      #app_lulu.vars['name'] = request.form['name_lulu']
      #app_lulu.vars['age'] = request.form['age_lulu']
      #return app_lulu.vars['name'] + '! posted.'

      # Create the plot
      plot = create_figure(current_feature_name, 10)
		
      # Embed plot into HTML via Flask Render
      script, div = components(plot)
      return render_template("iris_index1.html", script=script, div=div,
        feature_names=feature_names,  current_feature_name=current_feature_name)

if __name__ == "__main__":
    app_lulu.run(debug=True)
