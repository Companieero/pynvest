from pynvest import Pynvest

test_investment = Pynvest(investment=40000, discount_rate=.08)
test_investment.add_income(value=20000, period=1)
test_investment.add_outcome(value=3000, period=2)
test_investment.add_income(value=17000, period=3)
test_investment.add_income(value=15000, period=4)
test_investment.add_income(value=16000, period=5)

print(f'''
    DISCOUNT RATE: {test_investment.get_discount_rate()}
    NPV: {test_investment.get_npv()}
    IRR: {test_investment.get_irr()}
''')