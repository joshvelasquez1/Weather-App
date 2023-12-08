import requests
import json
from PyQt6.QtWidgets import *
from weather_main import Ui_weathermain
from weather_second import Ui_weathersecond


class MainMenu(QMainWindow, Ui_weathermain):
	def __init__(self):
		super().__init__()

		self.setupUi(self)
		self.enter_button.clicked.connect(self.submit)

	def submit(self):
		base_url = "https://api.openweathermap.org/data/2.5/weather"
		appid = "7be3619db7fadee15790446e998a140f"
		location = self.city_input.text()
		url = f"{base_url}?q={location}&units=imperial&APPID={appid}"
		response = requests.get(url)
		unformatted_data = response.json()

		if unformatted_data == {"cod": "404", "message": "city not found"}:
			self.instruction_text.setText('City not found. Enter your City.')
		elif unformatted_data == {"cod": "400", "message": "Nothing to geocode"}:
			self.instruction_text.setText('No input found. Enter your City.')
		else:
			self.show_display_menu(unformatted_data)

	def show_display_menu(self, unformatted_data):
		self.display_menu = DisplayMenu(self, unformatted_data)

		self.display_menu.show()
		self.hide()

	def closeEvent(self, event):
		if hasattr(self, 'display_menu'):
			self.display_menu.close()
		event.accept()


class DisplayMenu(QWidget, Ui_weathersecond):

	def __init__(self, parent, unformatted_data):
		super().__init__()

		self.setupUi(self)
		self.unformatted_data = unformatted_data
		self.back_button.clicked.connect(self.back_button_press)
		self.parent = parent

		city = unformatted_data["name"]
		weather_main = unformatted_data["weather"][0]["main"]
		temp = unformatted_data["main"]["temp"]
		temp_max = unformatted_data["main"]["temp_max"]
		temp_min = unformatted_data["main"]["temp_min"]

		self.city_name.setText(city)
		self.weather_type.setText(weather_main)
		self.temp_main.setText(f'Temperature: {temp}')
		self.temp_max.setText(f'Max: {temp_max}')
		self.temp_min.setText(f'Min: {temp_min}')

	def back_button_press(self):
		self.parent.show()
		self.hide()
