import requests
import os

def req(queries) :
	api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
	# query ='3lb carrots and a chicken sandwich'
	response = requests.get(api_url + queries, headers={'X-Api-Key': os.environ.get('CALORIES')})
	if response.status_code == requests.codes.ok:
	    return(response.text)
	else:
	    return("Error:", response.status_code, response.text)



