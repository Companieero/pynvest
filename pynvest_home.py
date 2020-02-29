class Home():
    def __init__(self, pynvestment, rent_price=0, loan_installment_size=0, loan_installment_count=0, renovation_cost=0):
        self.pynvestment = pynvestment
        self.loan_installment_size = loan_installment_size
        self.loan_installment_count = loan_installment_count
        self.renovation_cost = renovation_cost
        self.rent_price = rent_price

        self.loan_installment_count_left = loan_installment_count

    def sim(self, time=30):
        for i in range(time):
            self.pynvestment.add_income(value=12 * self.rent_price, period=i)
            print(f"Period\t{i},\tIncome\t{self.rent_price*12}\tNPV\t{self.pynvestment.get_npv()}\tIRR\t{self.pynvestment.get_irr()}")

            if i < self.loan_installment_count:
                self.pynvestment.add_outcome(value=12 * self.loan_installment_size, period=i)
                print(f"Period\t{i},\tOutcome\t{self.loan_installment_size*12}\tNPV\t{self.pynvestment.get_npv()}\tIRR\t{self.pynvestment.get_irr()}")
                self.loan_installment_count_left -= 1

        return (self.pynvestment, str(self.loan_installment_count_left*self.loan_installment_size))