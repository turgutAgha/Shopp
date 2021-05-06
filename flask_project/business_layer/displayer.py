from flask_project.business_layer import amazonScraper, tapazScraper, dataHandler, aliexpressScraper


class Displayer:
    _posts = None
    _request = None

    def __init__(self, search_term, websites, sort_type, currency, price_range):
        self._request = [websites, search_term, sort_type, currency, price_range]
        self._posts = {}

    def load_posts(self):

        for website in self._request[0]:
            flag = True
            if 'amazon' in website:
                scraper = amazonScraper.AmazonScraper()
            elif 'aliexpress' in website:
                scraper = aliexpressScraper.AliexpressScraper()
            elif 'tapaz' in website:
                scraper = tapazScraper.TapazScraper()
            else:
                flag = False

            if flag:
                scraper.scrape(self._request[1], self._request[4])
                self._posts[website] = scraper.get_records()

    def do_filtering(self):
        dh = dataHandler.DataHandler(self._posts)
        dh.do_sorting(self._request[2]).set_currency(self._request[3])

    def display(self):
        self.load_posts()
        self.do_filtering()
        return self._posts
