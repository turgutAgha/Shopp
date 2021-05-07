import abc


class WebScraper(metaclass=abc.ABCMeta):
    _records = None

    def __init__(self):
        self._records = []

    def get_records(self):
        return self._records

    @abc.abstractmethod
    def get_url(self, search_term, price_range):
        pass

    @abc.abstractmethod
    def get_price(self, price):
        pass

    @abc.abstractmethod
    def extract_record(self, item):
        pass

    @abc.abstractmethod
    def scrape(self, search_term, price_range):
        pass
