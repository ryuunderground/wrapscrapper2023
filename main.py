def tax_calc(money):
    return money * 0.35


def pay_tax(tax):
    print("thank u 4 ur paying", tax, "$")


bank_account = 500000
to_pay = tax_calc(bank_account)
pay_tax(to_pay)
