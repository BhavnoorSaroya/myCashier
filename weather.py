#currently weather remains experimental, but this comment will be updated accordingly when weather enters into the alpha stage

#ATTENTION Weather is now in alpha

#ATTENTION Weather has entered beta phase

#We are pleased to release weather module v1



def weather(tempstate="C", city="Nanaimo"):
	import requests
	"""The weather function tells the weather, what else were you expecting...

	This uses the openweathermap api (free version, so if it stops working that means openweather map went bust)
	
	OPTIONALLY, YOU CAN PASS IT A TEMPSTATE OF C AND A DIFFERENT CITY, OTHERWISE THE DEFAULTS OF CELSIUS AND 
    NANAIMO WILL BE USED"""

	print("Weather Function called, beginning weather retrival sequence")#######


	if tempstate=="C":
		print("Selected Temperature state is default of Celsius")
		
	elif tempstate=="K":
		print("This user is chose to use Kelvin, what a Chad")
		#too bad he can't spell
	else: print("Invalid temperature unit passed, and no, Farenheit is not a valid temperature unit. For users that disagree, we recommend the guilotine. ")

	api_key = "a87d5e24ba113d24c19a7d97ed3213b7" # this is a public key and that is why it is left in a public repo
	

	url= f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"#here is the url that we can ping a maximum of once every hour I believe, if we pay for openweathermap it would be more than that. 

	response = requests.get(url).json()
	
	# the city was not found
	if response["cod"] == 404:
		return None
	
	temp = response["main"]['temp']#obtain the current temperature from openweathermap
	if tempstate=="C":
		temp-=273.15
	elif tempstate == "R":
		temp -= 273.15
		temp *= 0.8
		
	feels_like = response['main']['feels_like']#obtain current "feels like" temperature from openweathermap
	if tempstate=="C":
		feels_like-=273.15
	elif tempstate == "R":
		feels_like -= 273.15
		feels_like *= 0.8
		
	humidity = response['main']['humidity']#obtain current humidity from openweathermap

	description = response['weather'][0]['description']#Obtain current weather description from openweathermap, this one was a pain to actually get working, turns out I needed a new api key. 

	icon = response['weather'][0]['icon']#this started magically working at the same time as description, so i havent messed with it since then. 

	if tempstate == "C":
		tempstate = "°C"
	if tempstate == "R":
		tempstate = "°Ré"

#here we are returning a dictionary with each value as its own key.
	return {
		'temp' : temp, #this one is just temperature
		'feels_like' : feels_like, #the feels like temperature
		'humidity' : humidity, #humidity, again self explanatory
		'description' : description, #this one is for the description of the weather, examples include sunny, light rain, cloudy, mist, etc.
		'icon': icon,#icon code provided to set the correct icon, icons are prenamed and provided by openweathermap.
		"tempstate" : tempstate#Temp state, relevant temperature states such as Kelvin and Celsius are available, for users that prefer farenheit, there is always the huitine
	}






