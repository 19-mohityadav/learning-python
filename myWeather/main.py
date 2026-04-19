import json
import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QLabel,
                             QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter your city here: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("My Weather")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: sens-serif;
                
            }
            QLabel#city_label{
                font-size: 40px;
                
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_button{
                font-size: 32px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description_label{
                font-size: 40px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "API_KEY"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            # print(data)

            if data["cod"] != "200":
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_err:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request\n Please correct city")
                case 401:
                    self.display_error("Unauthorized\n Invalid API key")
                case 403:
                    self.display_error("Forbidden\n Access Denied")
                case 404:
                    self.display_error("Not Found\n City not found")
                case 500:
                    self.display_error("Internal Server\n Please try again later")
                case 502:
                    self.display_error("Bad Gateway\n Invalid Response from server")
                case 503:
                    self.display_error("Gateway Timeout\n No response from server")
                case _:
                    self.display_error(f"HTTP Error: {http_err}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error\n Please try again later")

        except requests.exceptions.Timeout:
            self.display_error("Timeout Error\n Please try again later")

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects\n Please try again later")

        except requests.exceptions.RequestException as e:
            self.display_error(f"Request Error:\n {e}")




    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 16px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()


    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 70px;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):

        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌩️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "⛅"
        else:
            return ""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWeather = MyApp()
    myWeather.show()
    sys.exit(app.exec_())