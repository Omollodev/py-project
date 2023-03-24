
def interest_payment_calculator():
    print("This is a monthly payement loan calculator")
    print("")

    principal = float(input("Input loan amount: "))
    anual_interest_rate = float(input("Enter the annual rate: "))
    years = int(input("Enter amount of years: "))

    monthly_interest_rate = anual_interest_rate / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / \
        (1 - (1 + monthly_interest_rate) ** (- amount_of_months))

    print(f"The monthly payement for this loan is: {round(monthly_payment)} ")


interest_payment_calculator()
