class PynvestException(Exception):
    def __init__(self, message):
        self.message = message


class Pynvest:
    '''
    self.balance = [
        {
         (A może by tak - name: nazwa wpływu/wydatku)
         type: self.INCOME / self.OUTCOME
         value: float (always+)
         period: int
        }
    ]
    '''

    OUTCOME = -1
    INCOME = 1

    def __init__(self, investment, discount_rate = 0.08, balance_list = []):
        self.balance = [{'type': Pynvest.OUTCOME, 'value': investment, 'period': 0}] + balance_list
        self.discount_rate = discount_rate

    def get_discount_rate(self):
        return self.discount_rate

    def get_max_period(self):
        max_period = 0

        for i in self.balance:
            if max_period < i['period']:
                max_period = i['period']

        return max_period

    def map_balance(self, exlude = []):
        change_list = list(map(lambda flow: (flow['period'], flow['value'] * flow['type']) if flow['period'] not in exlude else None, self.balance))
        periods = {}

        for i in change_list:
            if i is None:
                continue

            if i[0] in periods:
                periods[i[0]] += i[1]
            else:
                periods[i[0]] = i[1]

        return periods

    def npv(self, cashflow, rate=None):
        nvp = 0

        if rate is None:
            rate = self.discount_rate

        for period in cashflow:
            nvp += cashflow[period] * (1.0/((1.0 + rate)**period))

        return nvp

    def get_npv(self):
        periods = self.map_balance()
        return self.npv(periods)

    def get_irr(self, iterations=100):
        periods = self.map_balance()
        for i in range(self.get_max_period()+1):
            if i not in periods:
                periods[i] = 0

        rate = 1.0
        investment = periods[0]

        for i in range(1, iterations + 1):
            rate *= (1 - self.npv(periods, rate) / investment)
        return rate

    def add_income(self, value, period):
        if value < 0:
            raise PynvestException('Income value should always be non-negative.')

        self.balance.append({'type': Pynvest.INCOME, 'value': value, 'period': period})

    def add_outcome(self, value, period):
        if value < 0:
            raise PynvestException('Outcome value should always be non-positive.')

        self.balance.append({'type': Pynvest.OUTCOME, 'value': value, 'period': period})