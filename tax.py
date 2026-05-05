"""
income = int(input("Enter your income: "))

if income > 12500:
    print("Band A ; £0")
    if income > 50000:
        b = (50000 - income)*0.2
        print(f"Band C ; £{b}")
        if income > 150000:
            c = (150000 - 50000)*0.4
            print(f"Band D ; £{c}")


income = int(input("Enter your income: "))

nonTax = 12500
if 

"""


income = int(input("Enter your annual income: "))

tax_b = 0
tax_c = 0
tax_d = 0

# Band B: 20% of income between £12,500 and £50,000
if income > 12500:
    upper_b = min(income, 50000)
    tax_b = (upper_b - 12500) * 0.2

# Band C: 40% of income between £50,000 and £150,000
if income > 50000:
    upper_c = min(income, 150000)
    tax_c = (upper_c - 50000) * 0.4


if income > 150000:
    tax_d = (income - 150000) * 0.45

# Output section
if tax_b == 0 and tax_c == 0 and tax_d == 0:
    print("No tax taken")
else:
    if tax_b > 0:
        print("Band B: £", int(tax_b))
    if tax_c > 0:
        print("Band C: £", int(tax_c))
    if tax_d > 0:
        print("Band D: £", int(tax_d))
