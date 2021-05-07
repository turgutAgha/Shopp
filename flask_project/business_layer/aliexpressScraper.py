from bs4 import BeautifulSoup

from flask_project import driver
from flask_project.business_layer import config
from flask_project.business_layer.webScraper import WebScraper


class AliexpressScraper(WebScraper):

    def __init__(self):
        super().__init__()

    def get_url(self, search_term, price_range):
        template = config.get_property("aliexpress_url_template")
        search_term = search_term.replace(' ', '+')
        url = template.format(search_term, price_range[0], price_range[1]) + '&page{}'

        return url

    def get_price(self, price):
        p = price.split('$')[1]
        p = p.split(' - ')[0]
        return float(p)

    def extract_record(self, item):
        try:
            price_parent = item.find('span', 'price-current')
            item_price = self.get_price(price_parent.text)
        except AttributeError:
            return

        a_tag = item.find('a', 'item-title')
        item_description = a_tag.text
        item_url = "https:" + a_tag.get('href')

        try:
            rating = item.find('span', 'rating-value').text
            rating += " out of 5 stars"
        except:
            rating = 'No rating'

        result = [item_description, item_price, rating, item_url, 'www.aliexpress.com']
        return result

    def scrape(self, search_term, price_range):

        url = self.get_url(search_term, price_range)
        counter = 0
        flag = True
        for page in range(1, 5):
            driver.get(url.format(page))
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            for sc in range(0, 6000, 1000):
                driver.execute_script(f"window.scrollTo({sc}, {sc + 1000});")
                results = soup.find_all('li', {'class': 'list-item'})
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
            if not flag:
                break
