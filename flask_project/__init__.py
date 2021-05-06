from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd29a114e2766085b45b2ec9a3e6d3f41'

from flask_project import routes
