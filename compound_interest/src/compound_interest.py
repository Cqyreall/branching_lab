class CompoundInterest:

    def __init__(self, principal, rate, years):
        self.principal = principal
        self.rate = rate/100
        self.years = years
        self.number_of_times_per_year = 12
    
    def compound_interest_calculated(self):
        compound_interest = self.principal * (1 + self.rate/12) ** (12 * self.years)
        return round(compound_interest, 2)
    pass
