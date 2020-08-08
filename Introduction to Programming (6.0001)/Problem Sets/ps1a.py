# MIT Introduction to Programmming, Course 6.0001
# Jorge Castello, jorgio.castello@gmail.com
# https://github.com/jorgio-castello

def castInputToFloat(input: str) -> float:
    return float(input)

def calculateMonthsTilDownPayment(salary: float, houseCost: float, savingsPercentage: float, savings: float = 0, downPaymentPercentage: float = 0.25) -> int:
    downPayment = houseCost * downPaymentPercentage
    months = 0
    
    while savings < downPayment:
        # Increase savings by interest received
        savings = savings * (1 + (0.04 / 12))
        # Increase savings by (salary / 12) * portion_saved
        savings += (salary / 12) * savingsPercentage
        # Increase month counter
        months += 1
    return months


# Test Cases:
print('\nStarting with Tests...\n')

print('For salary of $120,000, price of dream house of $1,000,000, and saving percentage of 10%')
print('Expect number of months to save for down payment to be 183, output:', calculateMonthsTilDownPayment(120000, 1000000, 0.10))
print('\n')

print('For salary of $80,000, price of dream house of $500,000, and saving percentage of 15%')
print('Expect number of months to save for down payment to be 105, output: ', calculateMonthsTilDownPayment(80000, 500000, .15))
print('\n')

print('Enter your own statistics to find out how long it will take you to get your dream house: ')
annual_salary: float = castInputToFloat(input('Enter your annual salary: '))
portion_saved: float = castInputToFloat(input('Ener the percent of your salary to save, as a decimal: '))
total_cost: float = castInputToFloat(input('Enter the cost of your dream home: '))

months: int = calculateMonthsTilDownPayment(annual_salary, total_cost, portion_saved)
print ('Number of months: ' + str(months))