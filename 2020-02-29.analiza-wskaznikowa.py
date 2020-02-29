from pynvest import Pynvest
from pynvest_home import Home

#warszawa = Pynvest(investment=310000, discount_rate=.08)
#warszawa.add_outcome(value=30000, period=0) # Stan hard -https://www.otodom.pl/oferta/wyremontowana-kawalerka-z-balkonem-na-brodnie-ID43Yky.html, 31m2

pynvest = Pynvest(340000, discount_rate=.08)
warszawa = Home(pynvestment=pynvest, rent_price=2400, loan_installment_size=1600, loan_installment_count=15, renovation_cost=40000)
pynvest, credit_left = warszawa.sim(30)

print(f'''
    DISCOUNT RATE: {pynvest.get_discount_rate()}
    NPV: {pynvest.get_npv()}
    IRR: {pynvest.get_irr()},
    CREDIT LEFT: {credit_left}
''')

#def __init__(self, pynvestment, loan_installment_size, loan_installment_count, renovation_cost, rent_price):


# Kwota
# Wysokość raty równej: 1 597,16 zł
# Wysokość rat malejących: 2 030,97 - 975,16 zł


# Wysokość raty równej: 1 597,16 zł
# Wysokość rat malejących: 2 030,97 - 975,16 zł

# warszawa.add_outcome(value=45000, period=0) # Stan hard -https://www.otodom.pl/oferta/wyremontowana-kawalerka-z-balkonem-na-brodnie-ID43Yky.html, 31m2 -medium-hight
#kuchnia - 21, łazienka - 14, salon - 20

# Bródno 1500/32mkw; 2000/32mwk
# https://www.olx.pl/oferta/kawalerka-do-wynajecia-na-brodnie-32m-warszawa-CID3-IDDRyTh.html#eae72af2a6
# https://www.otodom.pl/oferta/kawalerka-wyposazona-na-brodnie-ul-torunska-ID44Q4d.html

# Kwota kredytu: 306 000 zł
# Wartość nieruchomości: 340 000 zł
# Okres kredytowania: 180 mies. - 2 157,61 zł
