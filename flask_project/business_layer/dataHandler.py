from flask_project.business_layer import config

AZN_TO_USD = config.get_property('AZN_TO_USD')
AZN_TO_EUR = config.get_property('AZN_TO_EUR')
USD_TO_EUR = config.get_property('USD_TO_EUR')


class DataHandler:
    _data = None

    def __init__(self, data):
        self._data = data

    def do_sorting(self, mode):
        if mode == 'ascending':
            for website in self._data:
                self._data[website].sort(key=lambda item: item[1])
        elif mode == 'descending':
            for website in self._data:
                self._data[website].sort(key=lambda item: item[1], reverse=True)
        return self

    def set_currency(self, currency):
        for website in self._data:
            for record in self._data[website]:
                if website == 'tapaz':
                    if currency == 'AZN':
                        record[1] = str(record[1]) + " " + currency
                    elif currency == 'USD' or currency == 'EUR':
                        record[1] = currency + " " + str(round(record[1] * eval(f"AZN_TO_{currency}"), 2))

                elif website == 'amazon' or website == 'aliexpress':
                    if currency == 'AZN':
                        record[1] = str(round(record[1] / AZN_TO_USD, 2)) + " " + currency
                    elif currency == 'USD':
                        record[1] = currency + " " + str(record[1])
                    elif currency == 'EUR':
                        record[1] = currency + " " + str(round(record[1] * USD_TO_EUR, 2))
