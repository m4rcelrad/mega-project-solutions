import math


class Pi:
    # Gauss–Legendre algorithm, limit = 100 digits
    def __init__(self, n):
        if n > 100:
            raise ValueError("The number of decimal places is limited to 100.")
        self.n = n
        self.accuracy = 10 ** (-n)
        self.a = 1.0
        self.b = 1.0 / (2 ** 0.5)
        self.t = 0.25
        self.p = 1.0

    def calculate(self):

        while abs(self.a - self.b) > self.accuracy:
            a_next = (self.a + self.b) / 2
            self.b = (self.a * self.b) ** 0.5
            self.t -= self.p * ((self.a - a_next) ** 2)
            self.a = a_next
            self.p *= 2

        pi = ((self.a + self.b) ** 2) / (4 * self.t)
        return round(pi, self.n)


class E:
    # Taylor series, limit = 100 digits
    def __init__(self, n):
        if n > 100:
            raise ValueError("The number of decimal places is limited to 100.")
        self.n = n
        self.accuracy = 10 ** (-n)
        self.e = 0.0
        self.factorial = 1.0
        self.k = 0

    def taylor_series(self):
        self.e += (1.0 / self.factorial)
        if (1.0 / self.factorial) < self.accuracy:
            return self.e
        self.k += 1
        self.factorial *= self.k
        return round(self.taylor_series(), self.n)


class Fibonacci:
    # Fibonacci Sequence to n
    def __init__(self, n):
        if n < 0:
            raise ValueError("The number must be a non-negative integer.")
        self.n = n
        self.fib = [0, 1]
        self.i = 2

    def calculate(self):
        while True:
            next = self.fib[self.i - 1] + self.fib[self.i - 2]
            if next > self.n:
                break
            self.fib.append(next)
            self.i += 1
        return self.fib


class FibonacciCalculator:
    # Fibonacci Sequence to nth number
    def __init__(self, limit):
        if limit < 0:
            raise ValueError("The number must be a non-negative integer.")
        self.limit = limit

    def calculate_fibonacci(self):
        if self.limit == 0:
            return []
        elif self.limit == 1:
            return [0]
        fib = [0, 1]
        while len(fib) < self.limit:
            fib.append(fib[-1] + fib[-2])
        return fib


class PrimeFactors:
    # Find all prime factors
    def __init__(self, n):
        if n < 2:
            raise ValueError("The number must be a positive integer greater than 1.")
        self.n = n
        self.factors = []

    def find_factors(self):
        while self.n % 2 == 0:
            self.factors.append(2)
            self.n //= 2
        limit = int(self.n ** 0.5) + 1
        for i in range(3, limit, 2):
            while self.n % i == 0:
                self.factors.append(i)
                self.n //= i
        return self.factors


class Tiles:
    # Find Cost of Tile to Cover W x H Floor
    def __init__(self, w, h, c):
        if w < 0 or h < 0 or c < 0:
            raise ValueError("All dimensions must be non-negative.")
        self.w = w
        self.h = h
        self.c = c

    def cost(self):
        return self.w * self.h * self.c


class MonthlyPayments:
    # Calculate monthly payments of a fixed term mortgage over given Nth terms at a given interest rate
    def __init__(self, principal, annual_rate, years, interval):
        if principal < 0 or annual_rate < 0 or years < 0:
            raise ValueError("All parameters must be non-negative.")
        if interval == "monthly":
            self.n = years * 12
            self.r = annual_rate / 12
        elif interval == "weekly":
            self.n = years * 52
            self.r = annual_rate / 52
        elif interval == "daily":
            self.n = years * 365
            self.r = annual_rate / 365
        else:
            raise ValueError("Invalid compounding interval. Choose 'monthly', 'weekly' or 'daily'.")
        self.monthly_payment = None
        self.principal = principal

    def calculate_monthly_payments(self):
        if self.r == 0:
            self.monthly_payment = self.principal / self.n
        else:
            self.monthly_payment = self.principal * (self.r * (1 + self.r) ** self.n) / (((1 + self.r) ** self.n) - 1)
        return round(self.monthly_payment, 2)


class PaybackTime:
    # Figure out the change and the number of banknotes, quarters, dimes, nickels, pennies needed for the change
    def __init__(self, principal, annual_rate, monthly_payment, interval):
        if principal < 0 or annual_rate < 0 or monthly_payment < 0:
            raise ValueError("All parameters must be non-negative.")
        if interval == "monthly":
            self.r = annual_rate / 12
        elif interval == "weekly":
            self.r = annual_rate / 52
        elif interval == "daily":
            self.r = annual_rate / 365
        else:
            raise ValueError("Invalid compounding interval. Choose 'monthly', 'weekly' or 'daily'.")
        self.monthly_payment = monthly_payment
        self.principal = principal
        self.payback_time = None

    def calculate_payback_time(self):
        if self.r == 0:
            self.payback_time = self.principal / self.monthly_payment / 12
        else:
            self.payback_time = math.log(
                self.monthly_payment / (self.monthly_payment - self.r * self.principal)) / math.log(1 + self.r)
        return self.payback_time


class ChangeCalculator:
    def __init__(self, n):
        if n < 0:
            raise ValueError("The amount must be a non-negative integer.")
        self.n = n
        self.change = {
            "hundred-dollar bills": 0, "fifty-dollar bills": 0, "twenty-dollar bills": 0, "ten-dollar bills": 0,
            "five-dollar bills": 0, "two-dollar bills": 0, "one-dollar bills": 0,
            "quarters": 0, "dimes": 0, "nickels": 0, "pennies": 0
        }
        self.values = {
            100: "hundred-dollar bills", 50: "fifty-dollar bills", 20: "twenty-dollar bills", 10: "ten-dollar bills",
            5: "five-dollar bills", 2: "two-dollar bills", 1: "one-dollar bills", 0.25: "quarters",
            0.1: "dimes", 0.05: "nickels", 0.01: "pennies"
        }

    def calculate(self):
        for value, name in self.values.items():
            if self.n >= value:
                self.change[name] = int(self.n / value)
                self.n = self.n % value
        return [[key, value] for key, value in self.change.items() if value != 0]

    def display_change(self):
        self.calculate()
        for key, value in self.change.items():
            print(f"{key}: {value}")


class UnitConverter:
    def __init__(self, conversion_type, value, from_unit, to_unit):

        self.value = value
        self.from_unit = from_unit
        self.to_unit = to_unit
        self.conversion_type = conversion_type
        if self.conversion_type == 1:
            if value < 0:
                raise ValueError("The value must be a non-negative number.")
            self.units = {
                "m": 1, "km": 1000, "cm": 0.01, "mm": 0.001, "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344
            }
        elif self.conversion_type == 3:
            if value < 0:
                raise ValueError("The value must be a non-negative number.")
            self.units = {
                "m^2": 1, "km^2": 1000, "cm^2": 0.0001, "mm^2": 0.000001, "in^2": 39.3701, "ft^2": 3.28084,
                "yd^2": 1.09361, "mi^2": 0.621371
            }
        elif self.conversion_type == 4:
            if value < 0:
                raise ValueError("The value must be a non-negative number.")
            self.units = {
                "m^3": 1, "km^3": 1000, "cm^3": 0.000001, "mm^3": 0.000000001, "in^3": 61023.74419999999,
                "ft^3": 35.3146667,
                "gal": 0.003785411784, "l": 0.001, "ml": 0.000001, "imperial pint": 0.000473176473,
                "us fluid ounce": 0.000295735296
            }

    def convert(self):
        if self.conversion_type == 1 or self.conversion_type == 3 or self.conversion_type == 4:
            if self.from_unit in self.units and self.to_unit in self.units:
                return round(self.value * self.units[self.from_unit] / self.units[self.to_unit], 2)
            else:
                raise ValueError("Invalid unit provided for conversion.")
        elif self.conversion_type == 2:
            return self.convert_temperature()

    def convert_temperature(self):
        if self.from_unit == self.to_unit:
            return self.value

        if self.from_unit == "C":
            conversions = {
                "F": (self.value * 9 / 5) + 32,
                "K": self.value + 273.15,
                "R": (self.value + 273.15) * 9 / 5,
            }
        elif self.from_unit == "F":
            conversions = {
                "C": (self.value - 32) * 5 / 9,
                "K": (self.value - 32) * 5 / 9 + 273.15,
                "R": self.value + 459.67,
            }
        elif self.from_unit == "K":
            conversions = {
                "C": self.value - 273.15,
                "F": (self.value - 273.15) * 9 / 5 + 32,
                "R": self.value * 9 / 5,
            }
        elif self.from_unit == "R":
            conversions = {
                "C": (self.value - 491.67) * 5 / 9,
                "F": self.value - 459.67,
                "K": self.value * 5 / 9,
            }
        else:
            raise ValueError("Invalid temperature unit provided.")

        return conversions.get(self.to_unit, "Invalid conversion.")


class Validator:
    # Credit card number checker using luhn algorithm
    def __init__(self, credit_card_number):
        self.credit_card_number = credit_card_number

    def check_luhn(self):
        if not self.credit_card_number:
            raise ValueError("Credit card number cannot be empty.")
        if not self.credit_card_number.isdigit():
            raise ValueError("Credit card number must contain only digits.")
        if len(self.credit_card_number) < 13 or len(self.credit_card_number) > 19:
            raise ValueError("Credit card number must be between 13 and 19 digits long.")

        digits = [int(digit) for digit in self.credit_card_number]
        # Double every second digit from the right
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9
        # Sum all digits
        total_sum = sum(digits)
        # Check if the sum is divisible by 10
        return total_sum % 10 == 0


class Taxes:
    def __init__(self, tax_rate, cost):
        if tax_rate < 0 or cost < 0:
            raise ValueError("Tax rate and cost must be non-negative.")
        self.tax_rate = tax_rate
        self.cost = cost
        self.tax = 0

    def calculate_tax(self):
        self.tax = self.cost * self.tax_rate
        return self.tax

    def calculate_total(self):
        return self.cost + self.tax


class Factorial:
    def __init__(self, n):
        if n < 0:
            raise ValueError("The number must be a non-negative integer.")
        self.n = n

    def factorial_loop(self):
        factorial = 1
        temp = self.n
        while temp > 1:
            factorial *= temp
            temp -= 1
        return factorial

    def factorial_recursion(self, n=None):
        if n is None:
            n = self.n
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial_recursion(n - 1)


if __name__ == "__main__":
    try:
        pass
        # Calculate pi to nth digit
        n = int(input("Enter the number of decimal places (up to 100): "))
        print(f"Pi to {n} decimal places: {Pi(n).calculate()}")

        # Calculate e to nth digit
        n = int(input("Enter the number of decimal places (up to 100): "))
        print(f"E to {n} decimal places: {E(n).taylor_series()}")

        # Fibonacci Sequence to n
        n = int(input("Enter the limit: "))
        print(Fibonacci(n).calculate())

        # Fibonacci Sequence to nth number
        n = int(input("Enter the limit: "))
        print(f"Fibonacci sequence: {FibonacciCalculator(n).calculate_fibonacci()}")

        # Find Cost of Tile to Cover W x H Floor
        w, h, c = map(float, input("Enter width, height, and cost of tile: ").split())
        print(f"Cost of tile is {Tiles(w, h, c).cost()}$")

        # Mortgage calculator
        principal = float(input("Enter the loan amount (principal): "))
        annual_rate = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))
        years = int(input("Enter the loan term in years: "))
        interval = input("Enter the compounding interval (monthly, weekly, daily): ")
        print(f"Monthly payment: {MonthlyPayments(principal, annual_rate, years, interval).calculate_monthly_payments()}")

        # Payback time calculator
        principal = float(input("Enter the loan amount (principal): "))
        annual_rate = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))
        monthly_payment = float(input("Enter the monthly payment: "))
        interval = input("Enter the compounding interval (monthly, weekly, daily): ")
        print(f"Payback time: {PaybackTime(principal, annual_rate, monthly_payment, interval).calculate_payback_time()} years")

        # Change calculator
        amount = float(input("Enter the amount: "))
        calculator = ChangeCalculator(amount)
        calculator.display_change()

        # Unit converter
        print("Choose conversion type:")
        choice = int(input("1. Length converter, 2. Temperature converter, 3. Area converter, 4. Volume converter: "))
        if choice not in [1, 2, 3, 4]:
            raise ValueError("Invalid choice.")

        value = float(input("Enter the value: "))
        if choice == 1:
            from_unit = input("Enter the unit (m, km, cm, mm, in, ft, yd, mi): ")
            to_unit = input("Enter the unit to convert to (m, km, cm, mm, in, ft, yd, mi): ")
        elif choice == 2:
            from_unit = input("Enter the unit (C, F, K, R, D, N, P): ")
            to_unit = input("Enter the unit to convert to (C, F, K, R, D, N, P): ")
        elif choice == 3:
            from_unit = input("Enter the unit (m^2, km^2, cm^2, mm^2, in^2, ft^2, yd^2, mi^2): ")
            to_unit = input("Enter the unit to convert to (m^2, km^2, cm^2, mm^2, in^2, ft^2, yd^2, mi^2): ")
        elif choice == 4:
            from_unit = input("Enter the unit (m^3, km^3, cm^3, mm^3, in^3, ft^3, gal, l, ml, imperial pint, us fluid ounce): ")
            to_unit = input("Enter the unit to convert to (m^3, km^3, cm^3, mm^3, in^3, ft^3, gal, l, ml, imperial pint, us fluid ounce): ")

        print(f"{value} {from_unit} is equal to {UnitConverter(choice, value, from_unit, to_unit).convert()} {to_unit}")

        # Credit card validator
        card_number = input("Enter the credit card number: ")
        print(f"Valid credit card: {Validator(card_number).check_luhn()}")

        # Tax calculator
        cost = float(input("Enter the cost: "))
        tax_rate = float(input("Enter the tax rate: "))
        print(f"Tax: {Taxes(tax_rate, cost).calculate_tax()}")
        print(f"Total: {Taxes(tax_rate, cost).calculate_total()}")

        # Factorial
        n = int(input("Enter the number: "))
        print(f"Factorial: {Factorial(n).factorial_recursion()}")
        print(f"Factorial: {Factorial(n).factorial_loop()}")

    except ValueError as e:
        print(e)
