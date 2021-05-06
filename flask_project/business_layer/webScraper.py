class WebScraper:
    _records = None

    def __init__(self):
        self._records = []

    def get_records(self):
        return self._records

    def get_url(self, search_term, price_range):
        pass

    def extract_record(self, item):
        pass

    def get_price(self, price):
        pass

    def scrape(self, search_term, price_range):
        pass
