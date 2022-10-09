import json, requests
#function for weather
def output_display():
	temp = unformated_data["main"]["temp"]
	print(f"The current temperature is: {temp}")

	temp_min = unformated_data["main"]["temp_min"]
	print(f"The minimum temperature is: {temp_min}")

	temp_max = unformated_data["main"]["temp_max"]
	print(f"The maximum temperature is: {temp_max}")

	weather_main = unformated_data["weather"][0]["main"]
	print(f"The weather looks like: {unformated_data['weather'][0]['main']}")


while True:
	print("Welcome! Please enter your ZIP Code or City Name to see the temperature or type quit to quit!")

	#URL building components
	base_url = "https://api.openweathermap.org/data/2.5/weather"
	appid = "7be3619db7fadee15790446e998a140f"
	location = input()

	if location == "quit": 
		print("Goodbye!")
		break
	else:
		url = f"{base_url}?q={location}&units=imperial&APPID={appid}"
		response = requests.get(url)
		unformated_data = response.json()
		if unformated_data == {"cod":"404","message":"city not found"}:
			print()
			print("Sorry the entered information is incorrect")
			print()
		else:
			output_display()
			print()

# key: 7be3619db7fadee15790446e998a140f