class ConverterLogic():
    def __init__(self):
        self.rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'UAN': 41.1,
            'GBP': 0.75
        }

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        
        return amount * self.rates[to_currency] / self.rates[from_currency]