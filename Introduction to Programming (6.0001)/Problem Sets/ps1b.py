# MIT Introduction to Programmming, Course 6.0001
# Jorge Castello, jorgio.castello@gmail.com
# https://github.com/jorgio-castello

def castInputToFloat(input: str) -> float:
    return float(input)

def calculateMonthsTilDownPayment(salary: float, houseCost: float, savingsPercentage: float, semi_annual_raise: float, savings: float = 0, downPaymentPercentage: float = 0.25) -> int:
    downPayment = houseCost * downPaymentPercentage
    months = 0
    
    while savings < downPayment:
        # Increase savings by interest received
        savings = savings * (1 + (0.04 / 12))
        # Increase savings by (salary / 12) * portion_saved
        savings += (salary / 12) * savingsPercentage
        # If next month is when the semi-annual raise occurs, increase the salary before the next iteration of while-loop
        if (months + 1) % 6 == 0:
            salary *= (1 + semi_annual_raise)
        # Increase month counter
        months += 1
    return months


# Test Cases:
print('\nStarting with Tests...\n')

print('For salary of $120,000, price of dream house of $500,000, saving percentage of 5%, and a semi-annual raise of 3%')
print('Expect number of months to save for down payment to be 142, output:', calculateMonthsTilDownPayment(120000, 500000, 0.05, .03))
print('\n')

print('For salary of $80,000, price of dream house of $800,000, saving percentage of 10%, and a semi-annual raise of 3%')
print('Expect number of months to save for down payment to be 159, output: ', calculateMonthsTilDownPayment(80000, 800000, .1, .03))
print('\n')

print('For salary of $75,000, price of dream house of $1,500,000, saving percentage of 5%, and a semi-annual raise of 5%')
print('Expect number of months to save for down payment to be 261, output: ', calculateMonthsTilDownPayment(75000, 1500000, .05, .05))
print('\n')

print('Enter your own statistics to find out how long it will take you to get your dream house: ')
annual_salary: float = castInputToFloat(input('Enter your annual salary: '))
portion_saved: float = castInputToFloat(input('Ener the percent of your salary to save, as a decimal: '))
total_cost: float = castInputToFloat(input('Enter the cost of your dream home: '))
semi_annual_raise: float = castInputToFloat(input('Enter the semi-annual raise, as a decimal: '))

months: int = calculateMonthsTilDownPayment(annual_salary, total_cost, portion_saved, semi_annual_raise)
print ('Number of months: ' + str(months))