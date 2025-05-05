import math


class Pi:
    """
    A class to calculate the value of π to a specified number of decimal places using the Gauss-Legendre algorithm.
    The algorithm provides quadratic convergence, doubling the number of correct digits with each iteration.

    Attributes:
        n (int): Number of decimal places to calculate (limited to 100)
        accuracy (float): The desired accuracy threshold for convergence
        a, b, t, p (float): Variables used in the Gauss-Legendre algorithm
    """

    def __init__(self, n):
        if n > 100:
            raise ValueError("The number of decimal places is limited to 100.")
        self.n = n
        self.accuracy = 10 ** (-n)  # Set precision threshold
        self.a = 1.0  # Initial value of a
        self.b = 1.0 / (2 ** 0.5)  # Initial value of b
        self.t = 0.25  # Initial value of t
        self.p = 1.0  # Initial value of power

    def calculate(self):
        """
        Iteratively applies the Gauss-Legendre algorithm until convergence is achieved.

        Returns:
            float: The calculated value of π rounded to n decimal places
        """
        while abs(self.a - self.b) > self.accuracy:
            a_next = (self.a + self.b) / 2  # Arithmetic mean
            self.b = (self.a * self.b) ** 0.5  # Geometric mean
            self.t -= self.p * ((self.a - a_next) ** 2)  # Update t
            self.a = a_next  # Update a
            self.p *= 2  # Double the power

        pi = ((self.a + self.b) ** 2) / (4 * self.t)
        return round(pi, self.n)


class E:
    """
    A class to calculate the value of e (Euler's number) to a specified number of decimal places
    using the Taylor series expansion of e^x where x=1.

    Attributes:
        n (int): Number of decimal places to calculate (limited to 100)
        accuracy (float): The desired accuracy threshold for convergence
        e (float): Current approximation of e
        factorial (float): Running factorial value
        k (int): Current term index in the series
    """

    def __init__(self, n):
        if n > 100:
            raise ValueError("The number of decimal places is limited to 100.")
        self.n = n
        self.accuracy = 10 ** (-n)
        self.e = 0.0  # Initialize e
        self.factorial = 1.0  # 0! = 1
        self.k = 0  # Term counter

    def taylor_series(self):
        """
        Recursively calculates e using Taylor series expansion until desired accuracy is achieved.

        Returns:
            float: The calculated value of e rounded to n decimal places
        """
        self.e += (1.0 / self.factorial)  # Add current term
        if (1.0 / self.factorial) < self.accuracy:  # Check for convergence
            return self.e
        self.k += 1  # Increment term counter
        self.factorial *= self.k  # Update factorial
        return round(self.taylor_series(), self.n)


class Fibonacci:
    """
    A class to generate the Fibonacci sequence up to a specified maximum value.

    Attributes:
        n (int): The upper limit for Fibonacci numbers
        fib (list): List to store the sequence
        i (int): Current index in the sequence generation
    """

    def __init__(self, n):
        if n < 0:
            raise ValueError("The number must be a non-negative integer.")
        self.n = n
        self.fib = [0, 1]  # Initialize sequence
        self.i = 2  # Current index

    def calculate(self):
        """
        Generates Fibonacci numbers until exceeding the specified limit.

        Returns:
            list: The complete Fibonacci sequence up to the limit
        """
        while True:
            next_val = self.fib[self.i - 1] + self.fib[self.i - 2]  # Calculate next term
            if next_val > self.n:  # Check if we've exceeded the limit
                break
            self.fib.append(next_val)  # Add to sequence
            self.i += 1  # Increment index
        return self.fib


class FibonacciCalculator:
    """
    A class to generate the first n numbers in the Fibonacci sequence.

    Attributes:
        limit (int): The number of Fibonacci numbers to generate
    """

    def __init__(self, limit):
        if limit < 0:
            raise ValueError("The number must be a non-negative integer.")
        self.limit = limit

    def calculate_fibonacci(self):
        """
        Generates the first 'limit' Fibonacci numbers.

        Returns:
            list: The Fibonacci sequence with 'limit' elements
        """
        if self.limit == 0:
            return []
        elif self.limit == 1:
            return [0]
        fib = [0, 1]  # Initial sequence
        while len(fib) < self.limit:
            fib.append(fib[-1] + fib[-2])  # Add next term
        return fib


class PrimeFactors:
    """
    A class to find all prime factors of a given integer using trial division.

    Attributes:
        n (int): The number to factorize (must be > 1)
        factors (list): List to store the prime factors
    """

    def __init__(self, n):
        if n < 2:
            raise ValueError("The number must be a positive integer greater than 1.")
        self.n = n
        self.factors = []

    def find_factors(self):
        """
        Performs prime factorization using trial division.

        Returns:
            list: The prime factors of the original number in ascending order
        """
        # Handle even factors
        while self.n % 2 == 0:
            self.factors.append(2)
            self.n //= 2

        # Check odd factors up to sqrt(n)
        limit = int(self.n ** 0.5) + 1
        for i in range(3, limit, 2):
            while self.n % i == 0:
                self.factors.append(i)
                self.n //= i

        # If remaining n is a prime > 2
        if self.n > 2:
            self.factors.append(self.n)
        return self.factors


class Tiles:
    """
    A class to calculate the total cost of tiling a floor area.

    Attributes:
        w (float): Width of the floor
        h (float): Height of the floor
        c (float): Cost per unit area
    """

    def __init__(self, w, h, c):
        if w < 0 or h < 0 or c < 0:
            raise ValueError("All dimensions must be non-negative.")
        self.w = w
        self.h = h
        self.c = c

    def cost(self):
        """
        Calculates the total tiling cost.

        Returns:
            float: Total cost (area × cost per unit)
        """
        return self.w * self.h * self.c


class MonthlyPayments:
    """
    A class to calculate fixed-term mortgage payments with various compounding intervals.

    Attributes:
        principal (float): Loan amount
        annual_rate (float): Annual interest rate
        years (int): Loan term in years
        interval (str): Compounding interval ('monthly', 'weekly', 'daily')
        n (int): Total number of payments
        r (float): Periodic interest rate
        monthly_payment (float): Calculated payment amount
    """

    def __init__(self, principal, annual_rate, years, interval):
        if principal < 0 or annual_rate < 0 or years < 0:
            raise ValueError("All parameters must be non-negative.")

        # Set compounding parameters based on interval
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
        """
        Calculates the fixed periodic payment amount using the standard loan formula.

        Returns:
            float: The payment amount rounded to 2 decimal places
        """
        if self.r == 0:  # Handle zero-interest case
            self.monthly_payment = self.principal / self.n
        else:
            # Standard loan payment formula
            self.monthly_payment = (self.principal * self.r * (1 + self.r) ** self.n) / \
                                   (((1 + self.r) ** self.n) - 1)
        return round(self.monthly_payment, 2)


class PaybackTime:
    """
    A class to calculate the time required to pay back a loan given periodic payments.

    Attributes:
        principal (float): Loan amount
        annual_rate (float): Annual interest rate
        monthly_payment (float): Fixed periodic payment amount
        interval (str): Compounding interval ('monthly', 'weekly', 'daily')
        r (float): Periodic interest rate
        payback_time (float): Calculated payback time in years
    """

    def __init__(self, principal, annual_rate, monthly_payment, interval):
        if principal < 0 or annual_rate < 0 or monthly_payment < 0:
            raise ValueError("All parameters must be non-negative.")

        # Set compounding parameters based on interval
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
        """
        Calculates the payback time using the logarithmic formula for loan repayment.

        Returns:
            float: The payback time in years
        """
        if self.r == 0:  # Handle zero-interest case
            self.payback_time = self.principal / self.monthly_payment / 12
        else:
            # Logarithmic formula for payback time
            self.payback_time = math.log(
                self.monthly_payment / (self.monthly_payment - self.r * self.principal)) / math.log(1 + self.r)
        return self.payback_time


class ChangeCalculator:
    """
    A class to calculate the breakdown of change into standard denominations.

    Attributes:
        n (float): The amount to break down (must be non-negative)
        change (dict): Dictionary to store denomination counts
        values (dict): Mapping of denomination values to their names
    """

    def __init__(self, n):
        if n < 0:
            raise ValueError("The amount must be a non-negative integer.")
        self.n = round(n, 2)  # Handle floating point precision
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
        """
        Calculates the optimal breakdown of change using a greedy algorithm.

        Returns:
            list: List of [denomination, count] pairs for non-zero denominations
        """
        remaining = self.n
        # Process each denomination from largest to smallest
        for value, name in sorted(self.values.items(), reverse=True):
            if remaining >= value:
                count = int(remaining / value)
                self.change[name] = count
                remaining = round(remaining % value, 2)  # Maintain precision
        return [[key, value] for key, value in self.change.items() if value != 0]

    def display_change(self):
        """Prints the change breakdown in a human-readable format."""
        self.calculate()
        for key, value in self.change.items():
            if value != 0:
                print(f"{key}: {value}")


class UnitConverter:
    """
    A class to handle various unit conversions including length, temperature, area, and volume.

    Attributes:
        conversion_type (int): Type of conversion (1=length, 2=temperature, 3=area, 4=volume)
        value (float): The value to convert
        from_unit (str): The unit to convert from
        to_unit (str): The unit to convert to
        units (dict): Conversion factors for the selected type
    """

    def __init__(self, conversion_type, value, from_unit, to_unit):
        self.value = value
        self.from_unit = from_unit
        self.to_unit = to_unit
        self.conversion_type = conversion_type

        # Initialize conversion factors based on type
        if self.conversion_type == 1:  # Length
            if value < 0:
                raise ValueError("The value must be a non-negative number.")
            self.units = {
                "m": 1, "km": 1000, "cm": 0.01, "mm": 0.001,
                "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344
            }
        elif self.conversion_type == 3:  # Area
            if value < 0:
                raise ValueError("The value must be a non-negative number.")
            self.units = {
                "m^2": 1, "km^2": 1000, "cm^2": 0.0001, "mm^2": 0.000001,
                "in^2": 39.3701, "ft^2": 3.28084, "yd^2": 1.09361, "mi^2": 0.621371
            }
        elif self.conversion_type == 4:  # Volume
            if value < 0:
                raise ValueError("The value must be a non-negative number.")
            self.units = {
                "m^3": 1, "km^3": 1000, "cm^3": 0.000001, "mm^3": 0.000000001,
                "in^3": 61023.74419999999, "ft^3": 35.3146667, "gal": 0.003785411784,
                "l": 0.001, "ml": 0.000001, "imperial pint": 0.000473176473,
                "us fluid ounce": 0.000295735296
            }

    def convert(self):
        """
        Performs the unit conversion based on the specified type.

        Returns:
            float: The converted value rounded to 2 decimal places
        """
        if self.conversion_type in [1, 3, 4]:  # Length, area, or volume
            if self.from_unit in self.units and self.to_unit in self.units:
                # Conversion formula: value × (from_unit / to_unit)
                return round(self.value * self.units[self.from_unit] / self.units[self.to_unit], 2)
            else:
                raise ValueError("Invalid unit provided for conversion.")
        elif self.conversion_type == 2:  # Temperature
            return self.convert_temperature()

    def convert_temperature(self):
        """
        Handles temperature conversions between Celsius, Fahrenheit, Kelvin, and Rankine.

        Returns:
            float: The converted temperature
        """
        if self.from_unit == self.to_unit:  # No conversion needed
            return self.value

        # Define conversion formulas for each from_unit
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
    """
    A class to validate credit card numbers using the Luhn algorithm.

    Attributes:
        credit_card_number (str): The card number to validate
    """

    def __init__(self, credit_card_number):
        self.credit_card_number = credit_card_number

    def check_luhn(self):
        """
        Validates a credit card number using the Luhn algorithm.

        Returns:
            bool: True if valid, False otherwise

        Raises:
            ValueError: If the input is invalid (empty, non-numeric, or wrong length)
        """
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
            if digits[i] > 9:  # Handle double-digit results
                digits[i] -= 9

        # Check if sum is divisible by 10
        total_sum = sum(digits)
        return total_sum % 10 == 0


class Taxes:
    """
    A class to calculate tax amounts and total costs including tax.

    Attributes:
        tax_rate (float): The tax rate (e.g., 0.05 for 5%)
        cost (float): The pre-tax cost
        tax (float): The calculated tax amount
    """

    def __init__(self, tax_rate, cost):
        if tax_rate < 0 or cost < 0:
            raise ValueError("Tax rate and cost must be non-negative.")
        self.tax_rate = tax_rate
        self.cost = cost
        self.tax = 0  # Initialize tax amount

    def calculate_tax(self):
        """Calculates and returns the tax amount."""
        self.tax = self.cost * self.tax_rate
        return self.tax

    def calculate_total(self):
        """Calculates and returns the total cost including tax."""
        return self.cost + self.tax


class Factorial:
    """
    A class to calculate factorials using both iterative and recursive methods.

    Attributes:
        n (int): The number to compute factorial for (must be non-negative)
    """

    def __init__(self, n):
        if n < 0:
            raise ValueError("The number must be a non-negative integer.")
        self.n = n

    def factorial_loop(self):
        """
        Calculates factorial using an iterative approach.

        Returns:
            int: The factorial of n
        """
        factorial = 1
        temp = self.n
        while temp > 1:
            factorial *= temp
            temp -= 1
        return factorial

    def factorial_recursion(self, n=None):
        """
        Calculates factorial using recursion.

        Args:
            n (int, optional): Current value for recursive calculation

        Returns:
            int: The factorial of the original n
        """
        if n is None:  # Initial call
            n = self.n
        if n == 0 or n == 1:  # Base case
            return 1
        else:  # Recursive case
            return n * self.factorial_recursion(n - 1)


if __name__ == "__main__":
    try:
        # Calculate pi to nth digit
        n = int(input("Enter the number of decimal places (up to 100): "))
        print(f"Pi to {n} decimal places: {Pi(n).calculate()}")

        # Calculate e to nth digit
        n = int(input("Enter the number of decimal places (up to 100): "))
        print(f"E to {n} decimal places: {E(n).taylor_series()}")

        # Fibonacci Sequence to n
        n = int(input("Enter the limit: "))
        print(f"Fibonacci sequence: {Fibonacci(n).calculate()}")

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
        print(
            f"Monthly payment: {MonthlyPayments(principal, annual_rate, years, interval).calculate_monthly_payments()}")

        # Payback time calculator
        principal = float(input("Enter the loan amount (principal): "))
        annual_rate = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))
        monthly_payment = float(input("Enter the monthly payment: "))
        interval = input("Enter the compounding interval (monthly, weekly, daily): ")
        print(
            f"Payback time: {PaybackTime(principal, annual_rate, monthly_payment, interval).calculate_payback_time()} years")

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
            from_unit = input(
                "Enter the unit (m^3, km^3, cm^3, mm^3, in^3, ft^3, gal, l, ml, imperial pint, us fluid ounce): ")
            to_unit = input(
                "Enter the unit to convert to (m^3, km^3, cm^3, mm^3, in^3, ft^3, gal, l, ml, imperial pint, us fluid ounce): ")

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
