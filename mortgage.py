def myMortgageRate (principal,rate,duration):
    d=duration * 12
    r=(rate/100)/12
    monthlyPayment = r * principal * ((1+r)**d)/(((1+r)**d)-1)
    return monthlyPayment

duration=int(input('How many years are on the loan?'))
rate=float(input('Whats the yearly interest rate?'))
principal=int(input('Whats the total amount of the loan?'))

print('Monthly Payment : {}'.format(myMortgageRate(principal,rate,duration)))
