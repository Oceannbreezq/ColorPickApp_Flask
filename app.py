from flask import Flask, render_template, request
import plotly.express as px
from skimage import io
import json
import plotly

app = Flask(__name__)

# routes
@app.route("/", methods=['GET', 'POST'])
def home():
	return render_template("HOME.html")

@app.route("/picker/")
def picker():
	return render_template("PICKER.html")

@app.route("/popular/")
def popular():
	return render_template("POPULAR.html")

@app.route("/about/")
def about():
	return render_template("ABOUT.html")

@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
    if request.method == 'POST':
                img = request.files['my_image']
                img_path = "static/" + img.filename	
                img.save(img_path)
                iiimg = io.imread(img_path)
                fig = px.imshow(iiimg)
                fig.update_layout(coloraxis_showscale=True, width=400, height=400, margin=dict(l=20, r=20, b=20, t=20))
                fig.update_xaxes(showticklabels=False).update_yaxes(showticklabels=False)
                graph = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("PICKER.html", graph = graph)

if __name__ =='__main__':
	app.run(debug = True)