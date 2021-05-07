# Shopp

Shopp is a product searching tool that scrapes data from three websites, namely, Amazon, TapAz, Aliexpress and displays
the products' details.

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [How to Use](#how-to-use)

## Examples

## Features

- Product searching in three websites and displaying results
- Sorting by price
- Changing currency of the product price
- Defining minimum and maximum prices

## Requirements

There are some requirements needed to be installed before running the program.

1. Installing flask for python

```sh
pip3 install flask
```

2. Installing BeautifulSoup for parsing webpage

```sh
pip3 install bs4
```

3. Installing selenium for webdriver

```sh
pip3 install selenium
```

4. This program uses Chrome webdriver for automated testing of a web application.
   [This tutorial](https://zwbetz.com/download-chromedriver-binary-and-add-to-your-path-for-automated-functional-testing/)
   shows how to download the Chrome webdriver and add it to PATH in different operating systems.

## How to use
1. Clone the project
  
```sh
git clone git@github.com:turgutAgha/Shopp.git
```

2. Run the program in CMD or Terminal

```sh
# inside the project folder
python3 run.py
```

3. Open one of the web browsers

4. Enter the following address

```sh
localhost:5000
#or
127.0.0.1:5000
```

5. Use the features of the app

