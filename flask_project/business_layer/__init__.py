from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from . import config_parser

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
config = config_parser.Config("config.json")
