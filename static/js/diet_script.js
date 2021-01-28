var display = document.getElementById('display')


//extracting and converting it into json
var table = infos
if(table.synopsis != "")
{	
	
	table = JSON.parse(infos)	
	//bmi status
	var condition = table['synopsis'][0]

	//extracting meal
	var meals = table['synopsis'][1]

	var bmi = document.createElement('div')
	bmi.setAttribute('id','condition')
	if (condition === "Obesity" || condition === "Underweight" || condition === "Overweight"){

		bmi.style.backgroundColor = "rgb(184, 17, 2,0.9)"		
		bmi.innerHTML = "Condition : " + condition
	} 

	else{
		bmi.style.backgroundColor = "rgb(6, 99, 42,0.9)"
		bmi.innerHTML = "Condition : " + condition
	}

	display.appendChild(bmi)

	var head = document.createElement('div')
	head.setAttribute('id','meal')
	head.innerHTML = "Sample meal suggestion"
	display.appendChild(head)

	
	//boxes
	for(var i in meals){

		//to display meals
		var box = document.createElement('div')
		box.setAttribute('class','box')
		display.appendChild(box)
		var display_h1 = document.createElement('h2')
		display_h1.setAttribute('class','display_h1')
		display_h1.innerHTML = i 

		var display_meals = document.createElement('P')
		display_meals.setAttribute('class','para')
		display_meals.innerHTML = meals[i]
		box.appendChild(display_h1)
		box.appendChild(display_meals)
	}


}

var text_field = document.getElementById('calories')
var check = document.getElementById('check')

//place to display nutrients details
var display_nutrients = document.getElementById('display_nutrients')

//kinda like reverse proxy, fetching the results from the 
//backend
check.addEventListener('click',async () => {
	display_nutrients.innerHTML = ""
	const aal = await fetch(`/${text_field.value}`)
	var resp = await aal.json()
	var nutree_info = JSON.parse(resp)

	// console.log(nutree_info["items"])
	//looping through the response
	for(var i in nutree_info["items"][0]){
		// console.log(i)
		
		var display_info = document.createElement('div')
		display_info.setAttribute('class','nutri_info')
		display_info.innerHTML = i + " : " + nutree_info['items'][0][i]
		display_nutrients.appendChild(display_info)
	}

})

var height_measurment = document.getElementById('height_measurment')
var option = document.getElementById('my_option')
option.addEventListener('click',() => {

	if(option.value === 'feet'){
		height_measurment.innerHTML = " "
		var feet = document.createElement('input')
		feet.setAttribute('type','number')
		feet.setAttribute('placeholder','Enter your height')
		feet.setAttribute('name','feet')
		feet.setAttribute('class','measure')


		var inch = document.createElement('input')
		inch.setAttribute('type','number')
		inch.setAttribute('placeholder','Enter your height')
		inch.setAttribute('name','inch')
		inch.setAttribute('class','measure')

		height_measurment.appendChild(feet)
		height_measurment.appendChild(inch)

	}
	else
	{
		height_measurment.innerHTML = " "
		var text_field = document.createElement('input')
		text_field.setAttribute('type','number')
		text_field.setAttribute('placeholder','Enter your height')
		text_field.setAttribute('name','height')
		text_field.setAttribute('class','measure')
		height_measurment.appendChild(text_field)
	}
})

