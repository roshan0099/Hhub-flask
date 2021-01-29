import requests


def req(queries) :
	api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
	# query ='3lb carrots and a chicken sandwich'
	response = requests.get(api_url + queries, headers={'X-Api-Key': 'uoub/aG1tbr8CRCGXj3RIA==gH2MUnFR5ZPw0M6j'})
	if response.status_code == requests.codes.ok:
	    return(response.text)
	else:
	    return("Error:", response.status_code, response.text)



