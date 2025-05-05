import math


# Gauss–Legendre algorithm, limit = 100 digits
def find_pi_to_nth_digit(n):
    if n > 100:
        raise ValueError("The number of decimal places is limited to 100.")

    accuracy = 10 ** (-n)

    a = 1.0
    b = 1.0 / (2 ** 0.5)
    t = 0.25
    p = 1.0

    while abs(a - b) > accuracy:
        a_next = (a + b) / 2
        b = (a * b) ** 0.5
        t -= p * ((a - a_next) ** 2)
        a = a_next
        p *= 2

    pi = ((a + b) ** 2) / (4 * t)
    return round(pi, n)


# Taylor series, limit = 100 digits
def find_e_to_nth_digit(n):
    if n > 100:
        raise ValueError("The number of decimal places is limited to 100.")

    accuracy = 10 ** (-n)

    e = 0.0
    factorial = 1.0
    k = 0

    while True:
        e += (1.0 / factorial)
        if (1.0 / factorial) < accuracy:
            break
        k += 1
        factorial *= k

    return round(e, n)


# Fibonacci Sequence to n
def fibonacci_sequence(n):
    if n < 0:
        raise ValueError("The number must be a non-negative integer.")
    fib = [0, 1]
    i = 2
    while True:
        next = fib[i - 1] + fib[i - 2]
        if next > n:
            break
        fib.append(next)
        i += 1
    return fib


# Fibonacci Sequence to nth number
def fibonacci_nth_number(n):
    if n < 0:
        raise ValueError("The number must be a non-negative integer.")
    if n == 0:
        return []
    elif n == 1:
        return [0]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib


# Find all prime factors
def prime_factors(n):
    if n < 2:
        raise ValueError("The number must be a positive integer greater than 1.")
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)

    return factors


# Find Cost of Tile to Cover W x H Floor
def tile_cost(w, h, c):
    if w < 0 or h < 0 or c < 0:
        raise ValueError("All dimensions must be non-negative.")
    return w * h * c


# Calculate monthly payments of a fixed term mortgage over given Nth terms at a given interest rate
def mortgage_calculator_monthly_payments(principal, annual_rate, years, interval):
    if principal < 0 or annual_rate < 0 or years < 0:
        raise ValueError("All parameters must be non-negative.")
    if interval == "monthly":
        n = years * 12
        r = annual_rate / 12
    elif interval == "weekly":
        n = years * 52
        r = annual_rate / 52
    elif interval == "daily":
        n = years * 365
        r = annual_rate / 365
    else:
        raise ValueError("Invalid compounding interval. Choose 'monthly', 'weekly' or 'daily'.")

    if r == 0:
        monthly_payment = principal / n
    else:
        monthly_payment = principal * (r * (1 + r) ** n) / (((1 + r) ** n) - 1)

    return round(monthly_payment, 2)


# Calculate how long it will take the user to pay back the loan
def mortgage_calculator_payback_time(principal, annual_rate, monthly_payment, interval):
    if principal < 0 or annual_rate < 0 or monthly_payment < 0:
        raise ValueError("All parameters must be non-negative.")
    if interval == "monthly":
        r = annual_rate / 12
    elif interval == "weekly":
        r = annual_rate / 52
    elif interval == "daily":
        r = annual_rate / 365
    else:
        raise ValueError("Invalid compounding interval. Choose 'monthly', 'weekly' or 'daily'.")

    if r == 0:
        payback_time = principal / monthly_payment / 12
    else:
        payback_time = math.log(monthly_payment / (monthly_payment - r * principal)) / math.log(1 + r)

    return payback_time


# Figure out the change and the number of banknotes, quarters, dimes, nickels, pennies needed for the change
def change_return(n):
    if n < 0:
        raise ValueError("The amount must be a non-negative integer.")
    change = {
        "hundred-dollar bills": 0, "fifty-dollar bills": 0, "twenty-dollar bills": 0, "ten-dollar bills": 0,
        "five-dollar bills": 0, "two-dollar bills": 0, "one-dollar bills": 0,
        "quarters": 0, "dimes": 0, "nickels": 0, "pennies": 0
    }
    values = {
        100: "hundred-dollar bills", 50: "fifty-dollar bills", 20: "twenty-dollar bills", 10: "ten-dollar bills",
        5: "five-dollar bills", 2: "two-dollar bills", 1: "one-dollar bills", 0.25: "quarters",
        0.1: "dimes", 0.05: "nickels", 0.01: "pennies"
    }

    for value, name in values.items():
        if n >= value:
            change[name] = int(n / value)
            n = n % value

    return [[key, value] for key, value in change.items()]


