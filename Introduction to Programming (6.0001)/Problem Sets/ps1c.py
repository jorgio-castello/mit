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

# Calculate Savings Rate
def calculateSavingsRate(salary: float, houseCost: float, semi_annual_raise: float, timeline: int, savings: float = 0, downPaymentPercentage: float = 0.25) -> [float or int] or str:
    # There may be a number of savings rates that yield 36 month, we want to find the minimum 
    possibleSavingRates: dict = {}
    # How many steps does it take to discover the optimal savings rate?
    bisectionSearchCounter = 1
    
    # Percentage represented in terms of integers, (i.e 100% == 10000)
    minSavingsPointer: int = 0
    maxSavingsPointer: int = 10000

    # Bisection Search
    while minSavingsPointer < maxSavingsPointer:
        # Calculate midpoint, test # of months based on savings rate
        midpoint:int = (minSavingsPointer + maxSavingsPointer) / 2
        midpointSavingsRate:float = midpoint / 10000
        
        # How many months does the midpointSavingsRate take to save for the down payment?
        months:int = calculateMonthsTilDownPayment(salary, houseCost, midpointSavingsRate, semi_annual_raise, savings, downPaymentPercentage)
        # If # of months == timeline, save the savingsRate, continue search to learn if there's yet a smaller, optimal savings rate
        if months == timeline:
            possibleSavingRates[midpointSavingsRate] = [midpointSavingsRate, bisectionSearchCounter]
            maxSavingsPointer = midpoint - 1 
        # If # of months > 36, re-assign minSavingsPointer to midpoint
        if months > timeline:
            minSavingsPointer = midpoint + 1
        # If # of months < 36, re-assign maxSavingsPointer to midpoint
        if months < timeline:
            maxSavingsPointer = midpoint - 1 
        # increment bisection search counter
        bisectionSearchCounter += 1

    # Find the minimum rate in the set
    min = float('inf')
    for rate in possibleSavingRates:
        if (int(rate) < min):
            min = rate

    # If there's a minimum rate in the set, return it
    if min != float('inf'):
        return possibleSavingRates[min]

    return 'It is not possible to pay the down payment in three years'


# Test Cases:
print('\nStarting with Tests...\n')
print('For salary of $150,000, dream house of $1,000,000, a semi-annual raise of 7%, the optimal savings rate to afford down payment in three year:')
result = calculateSavingsRate(150000, 1000000, 0.07, 36)
print('Expect best savings rate to be 0.441, output:', result[0])
print('Expect steps in bisection search to be 12, output:', result[1])
print('\n')

print('For salary of $300,000, dream house of $1,000,000, a semi-annual raise of 7%, the optimal savings rate to afford down payment in three year:')
result = calculateSavingsRate(300000, 1000000, 0.07, 36)
print('Expect best savings rate to be 0.2206, output:', result[0])
print('Expect steps in bisection search to be 9, output:', result[1])
print('\n')

print('For salary of $10,000, dream house of $1,000,000, a semi-annual raise of 7%, the optimal savings rate to afford down payment in three year:')
result = calculateSavingsRate(10000, 1000000, 0.07, 36)
print('Expect best savings rate to not exist, output:', result)
print('\n')

# print('Enter your own statistics to find out how long it will take you to get your dream house: ')
# annual_salary: float = castInputToFloat(input('Enter your annual salary: '))
# portion_saved: float = castInputToFloat(input('Ener the percent of your salary to save, as a decimal: '))
# total_cost: float = castInputToFloat(input('Enter the cost of your dream home: '))
# semi_annual_raise: float = castInputToFloat(input('Enter the semi-annual raise, as a decimal: '))

# months: int = calculateMonthsTilDownPayment(annual_salary, total_cost, portion_saved, semi_annual_raise)
# print ('Number of months: ' + str(months))