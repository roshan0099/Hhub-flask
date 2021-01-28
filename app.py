from flask import *
from tensorflow.keras.models import load_model
from flask import Flask , render_template , request, redirect,jsonify,send_from_directory
from bmi import Meal_bmi
from calories_check import req
import json
import cv2
import numpy as np
# import pandas as pd


app = Flask(__name__)


def covid_prediction(image_test):
    model = load_model("model.h5")
    model.compile(optimizer="adam", loss="bianry_crossentropy",
                  metrics=["accuracy"])
    image = cv2.imread(image_test)
    image = cv2.resize(image, (64, 64))
    image = np.reshape(image, [1, 64, 64, 3])

    all_classes = model.predict_classes(image)
    label = ["POSITIVE", "NEGATIVE"]
    return label[all_classes[0][0]]


@app.route("/covid")
def covid():
    return render_template("covid-19-index.html")


@app.route("/covid/upload-image", methods=['GET', 'POST'])
def image_upload():
    file = request.files['image']
    if request.method == "POST":
        if file:
            file.save(file.filename)
            label = covid_prediction(file.filename)
            return render_template("covid-19-result.html", name=label)

        else:
            return redirect('/covid')

def calccal(life,bmr):
    one = bmr*1.2
    two = bmr*1.375
    three = bmr*1.55
    four = bmr*1.725
    five = bmr*1.9
    if life == "1":
        return one
    elif life == "2":
        return two
    elif life == "3":
        return three
    elif life == "4":
        return four
    else:
        return five


@app.route('/',methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/workout',methods=["GET","POST"])
def work():
    return render_template('workout.html')

@app.route('/workout/calorie',methods=["GET","POST"])
def calc():
    if request.method == "POST":
        if request.form['gender'] == 'male':
            life = request.form['lifestyle']
            bmr = (13.397*int(request.form['weight'])) +( 4.799*int(request.form['height'])) - (5.677*int(request.form['age'])) + 88.362
            calorie = round(calccal(life,bmr))
            calories = [calorie,round(calorie*0.90),round(calorie*0.79),round(calorie*0.59)]
            return render_template('calorie.html',calories=calories)
        else:
            life = request.form['lifestyle']
            bmr = (9.247*int(request.form['weight'])) +( 3.098*int(request.form['height'])) - (4.330*int(request.form['age'])) + 447.593
            calorie = round(calccal(life,bmr))
            calories = [calorie,round(calorie*0.90),round(calorie*0.79),round(calorie*0.59)]
            return render_template('calorie.html',calorie=calorie)
    else:
        return redirect('/workout')


#creating an instance
info = Meal_bmi()
print(info.finding_height_cm(167))
#main page
@app.route('/diet', methods=['GET','POST'])
def home():
	if request.method == 'GET' :
		data = {
		"synopsis" : ""}
		return render_template('diet_main.html',data = data)
	else :

		weight = request.form['weight']

		try :
			#extracting height and weight from user
			height = request.form['height']

			bmi_index = info.bmi(int(weight),height = int(height))
			meals = info.response_meal(bmi_index)

			data = {
			#"synopsis" : [bmi_index,meals]
			"synopsis" : [bmi_index,meals]
			}
			return render_template('diet_main.html',data = json.dumps(data))

		except :	
			feet = request.form["feet"]
			inch = request.form["inch"]

			bmi_index = info.bmi(int(weight),ft = int(feet), inch = int(inch))
			meals = info.response_meal(bmi_index)
			data = {
			#"synopsis" : [bmi_index,meals]
			"synopsis" : [bmi_index,meals]
			}
			return render_template('diet_main.html',data = json.dumps(data))
			
@app.route('/<name>')
def calories(name):

	info = req(name)

	print(info)
	data = {
	"inna" : info
	}

	return json.dumps(data["inna"])


# @app.route('/favicon.ico')
# def fav():
#     return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')




if __name__ == "__main__":
    app.run(debug=True)
