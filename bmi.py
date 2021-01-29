from pymongo import MongoClient 
import random
# import os


class Meal_bmi :

	def __init__(self) :

		#connecting to db
		self.client = MongoClient(os.environ.get('MONGO'))
		self.db = self.client["checking"]

		self.collection = self.db["diet"]



	#function that has a dictionary which has ctegories to know if its over/under weight and so on...
	def indexing(self,body_mass_index):
		#dictionary
		categories = {
		(0,18.5) : "Underweight",
		(18.5,25) : "Normal", (25,30): "Overweight",
		(30,200) : "Obesity"
		}

		dict_keys = categories.keys()
		for i in range(len(dict_keys)) :
			lower,upper = list(dict_keys)[i]
			if body_mass_index > lower and body_mass_index <= upper :
				return(categories[(lower,upper)])
				break

	#function that returns height meter square when 
	#given in inch and feet
	def finding_height_ftInch(self,ft,inch):
		
		#total inches
		total_inch = inch + (ft * 12)

		#converting it into meter 
		total_meter = total_inch * 0.0254

		return round(total_meter**2,4)

	#function that returns height in meter square when given
	#in cm
	def finding_height_cm(self,cm) :
		return (cm/100)**2


	#function to find bmi and return an adequate response 
	def bmi(self,weight,height = 0,ft = 0,inch = 0):

		#if given height is not in cm 
		if height == 0 :

			meter_square = self.finding_height_ftInch(ft,inch)
			#calculating body_mass_index
			body_mass_index	= weight/meter_square

		#if given heigh is in cm	
		else :
			
			meter_square = self.finding_height_cm(height)
			
			#calculating body mass index
			body_mass_index = weight/meter_square	

		return self.indexing(body_mass_index)

	def	response_meal(self,bmi_status) :

		weight = 0

		if bmi_status == 'Overweight' :
			bmi_status = 'Obesity'
			meals = self.collection.find_one({"BMI" : bmi_status})

		else :
			meals = self.collection.find_one({"BMI" : bmi_status})	

		return meals['meal_plans'][random.randint(1,6)]




# jam = Meal_bmi()

# for i in jam.response_meal("overweight") :
# 	print(i, " ",jam.response_meal("overweight")[i])

	
