# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


class Loan:

    def __init__(self, loan_amount, number_anuittet):
        self.loan_amount = loan_amount
        self.number_anuittet = number_anuittet

        self.instalments = loan_amount/number_anuittet

    def owed_amount(self, months=None):
        if months is None:
            return self.loan_amount
        else:
            return self.loan_amount - (self.instalments*months)


my_loan = Loan(100000, 120)
print(my_loan.owed_amount())
print(my_loan.owed_amount(100))