from bs4 import BeautifulSoup

from . import driver, config
from .webScraper import WebScraper


class TapazScraper(WebScraper):

    def __init__(self):
        super().__init__()

    def get_url(self, search_term, price_range):
        template = config.get_value("tapaz_url_template")
        search_term = search_term.replace(' ', '+')
        url = template.format(search_term, price_range[0], price_range[1])

        return url

    def get_price(self, price):
        p = price.split()
        p = "".join(p)
        p = p.split(',')
        p = "".join(p)

        return float(p)

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
