from bs4 import BeautifulSoup

from flask_project import driver
from flask_project.business_layer import config
from flask_project.business_layer.webScraper import WebScraper


class TapazScraper(WebScraper):

    def get_url(self, search_term, price_range):
        template = config.get_property("tapaz_url_template")
        search_term = search_term.replace(' ', '+')
        url = template.format(search_term, price_range[0], price_range[1])

        return url

    def extract_record(self, item):
        try:
            item_price = self.get_price(item.find('span', 'price-val').text)
        except AttributeError:
            return

        a_tag = item.find('a', 'products-link')
        item_url = 'https://tap.az/' + a_tag.get('href')
        item_description = item.find('div', 'products-name').text
        rating = 'No rating'

        result = [item_description, item_price, rating, item_url, 'www.tap.az']
        return result

    def get_price(self, price):
        p = price.split()
        p = "".join(p)
        p = p.split(',')
        p = "".join(p)

        return float(p)

    def scrape(self, search_term, price_range):

        url = self.get_url(search_term, price_range)
        counter = 0

        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'class': 'products-i'}, limit=50)

        for item in results:
            record = self.extract_record(item)
            if record:
                if counter < 20:
                    self._records.append(record)
                    counter += 1
                else:
                    break
