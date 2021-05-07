from bs4 import BeautifulSoup

from flask_project import driver
from flask_project.business_layer import config
from flask_project.business_layer.webScraper import WebScraper


class AmazonScraper(WebScraper):

    def __init__(self):
        super().__init__()

    def get_url(self, search_term, price_range):
        template = config.get_property("amazon_url_template")
        search_term = search_term.replace(' ', '+')
        url = template.format(search_term, int(price_range[0] * 100), int(price_range[1] * 100)) + '&page={}'

        return url

    def get_price(self, price):
        p = price[1:]
        return float(p)

    def extract_record(self, item):
        try:
            price_parent = item.find('span', 'a-price')
            item_price = self.get_price(price_parent.find('span', 'a-offscreen').text)
        except AttributeError:
            return

        a_tag = item.h2.a
        item_description = a_tag.text.strip()
        item_url = 'https://www.amazon.com/' + a_tag.get('href')

        try:
            rating = item.i.text
        except:
            rating = 'No rating'

        result = [item_description, item_price, rating, item_url, 'www.amazon.com']
        return result

    def scrape(self, search_term, price_range):

        url = self.get_url(search_term, price_range)
        counter = 0
        flag = True
        for page in range(1, 5):
            driver.get(url.format(page))
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            results = soup.find_all('div', {'data-component-type': 's-search-result'})

            for item in results:
                record = self.extract_record(item)
                if record:
                    if counter < 20:
                        self._records.append(record)
                    else:
                        flag = False
                        break
                    counter += 1
            if not flag:
                break
