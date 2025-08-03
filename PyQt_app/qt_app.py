import requests
from PyQt6.QtWidgets import QComboBox, QMainWindow, QApplication, QLabel
from PyQt6.QtCore import QThread, pyqtSignal
import sys

class APIParse(QThread):

    def parser(self, data):
        self.data_ready = pyqtSignal(list)
        self.error_occurred = pyqtSignal(str)

        #json data parse method
        country_list = [d['name'] for d in data]
        return country_list

    def run(self):
        try:
            # connect to api and get json data
            api_url = "https://www.apicountries.com/countries" 
            response = requests.get(api_url)
            data = response.json()
            # pass data thru parsing method & sort, then send off
            cl_sorted = sorted(self.parser(data))
            self.data_ready.emit(cl_sorted)

        # exceptions jic
        except requests.exceptions.RequestException as e:
            self.error_occurred.emit(f"API request failed: {e}")
        except Exception as e:
            self.error_occurred.emit(f"An unexpected error occurred: {e}")

 

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # create an empty label & combobox
        self.label = QLabel()
        self.label.setText(" ")
        self.combobox = QComboBox()

        # thread to send json data to combobox
        self.thread = APIParse()
        self.thread.data_ready.connect(self.populate_combobox)
        self.thread.error_occurred.connect(self.show_error)
        self.thread.start()

    def populate_combobox(self, country_list):
        self.combobox.addItems(country_list)
        

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()