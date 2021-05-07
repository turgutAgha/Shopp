# Business layer

## About

WebScraper is an interface that AliexpressScraper, TapazScraper and AmazonScraper classes inherit from it.
With the help of selenium and bs4 they parse the web pages and scrape all needed data.

DataHandler class is used for sorting scraped data by their price in either ascending or descending order and
setting the currency according to a customer's choice.

