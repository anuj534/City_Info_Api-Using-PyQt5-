import os
import sys
import requests
from dotenv import load_dotenv
from PyQt5.QtWidgets import QLabel, QApplication , QWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

load_dotenv()

class City_Timezone_Api(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Enter a city name :", self)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Get Info", self)
        self.label2 = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("City Info App")
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.line_edit)
        vbox.addWidget(self.button)
        vbox.addWidget(self.label2)
        self.setLayout(vbox)
        self.label.setAlignment(Qt.AlignCenter)
        self.line_edit.setAlignment(Qt.AlignCenter)
        self.label2.setAlignment(Qt.AlignCenter)

        self.label.setObjectName("label")
        self.line_edit.setObjectName("input")
        self.button.setObjectName("button")
        self.label2.setObjectName("label2")
        self.setStyleSheet("""
            QWidget {
                background-color: #18181b;
                color: #f4f4f5;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QLabel#label {
                font-size: 35px;
                font-weight: bold;
                color: #ffffff;
                margin-bottom: 5px;
                font-style: italic;
            }
            QLineEdit#input {
                background-color: #27272a;
                border: 2px solid #3f3f46;
                border-radius: 8px;
                padding: 10px 14px;
                font-size: 35px;
                color: #ffffff;
                font-family: Arial;
                font-weight: bold;
                selection-background-color: #3b82f6;
                selection-color: #ffffff;
            }

            QLineEdit#input:focus {
                border: 2px solid #3b82f6;
                background-color: #2e2e32;
            }

            QPushButton#button{
                background-color: hsl(194, 87%, 49%);
                color: #ffffff;
                border: none;
                border-radius: 8px;
                padding: 11px;
                font-size: 40px;
                font-weight: bold;
            }
            QPushButton#button:hover {
                background-color: hsl(194, 87%, 59%);
            }
            QPushButton#button:pressed {
                background-color: hsl(194, 87%, 69%);
            }
            QLabel#label2 {
                border-radius: 8px;
                padding: 14px;
                font-size: 49px;
                color: #93c5fd;
                margin-top: 5px;
                font-family: calibri;
                font-weight: bold;
            }
        """)

        self.button.clicked.connect(self.get_info)

    def get_info(self):
        api_key = os.getenv("OPENTRIPMAP_API_KEY")
        if not api_key:
            self.display_error("API key missing:\nAdd it to your .env file")
            return
        city_name = self.line_edit.text()
        url = f"https://api.opentripmap.com/0.1/en/places/geoname?name={city_name}&apikey={api_key}"
        
        try:
           response = requests.get(url)
           response.raise_for_status()
           data = response.json()
           if response.status_code == 200:
               self.display(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API Key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not Found:\nCity is not found")
                case 500:
                    self.display_error("Inertnal Server Error:\nPlease try again late")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from server")
                case 503:
                    self.display_error("Service Unavaiblable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occuried:\n{http_error}")
        except requests.exceptions.ConnectionError:
           self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
           self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
           self.display_error("Too many Redirects:\nCheck the url")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")
        
    def display_error(self, message):
        self.label2.setText(message)
    
    def display(self, data):
        
        time = data["timezone"]
        co_ord1 = data["lat"]
        co_ord2 = data["lon"]
        self.label2.setText(f"TimeZone: {time}\nLatitude: {co_ord1}\nLongitude: {co_ord2}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    city = City_Timezone_Api()
    city.show()
    sys.exit(app.exec_())
