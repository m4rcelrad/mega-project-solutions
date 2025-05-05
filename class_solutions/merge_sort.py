import math


class Pi:
    """
    Calculates π (pi) to a specified number of decimal places using the Gauss-Legendre algorithm.
    This iterative algorithm quadratically converges to π, providing rapid digit calculation.
    """
    
    def __init__(self, n):
        """
        Initializes the π calculator with precision parameters.
        
        Args:
            n (int): Number of decimal places desired (max 100)
            
        Raises:
            ValueError: If requested precision exceeds 100 digits
        """
        if n > 100:
            raise ValueError("The number of decimal places is limited to 100.")
        self.n = n
        self.accuracy = 10 ** (-n)  # Stopping condition threshold
        self.a = 1.0  # Initial a value
        self.b = 1.0 / math.sqrt(2)  # Initial b value
        self.t = 0.25  # Initial t value
        self.p = 1.0  # Power of 2 multiplier

    def calculate(self):
        """
        Executes the Gauss-Legendre iteration until desired accuracy is achieved.
        
        Returns:
            float: π approximated to n decimal places
        """
        while abs(self.a - self.b) > self.accuracy:
            a_next = (self.a + self.b) / 2
            self.b = math.sqrt(self.a * self.b)
            self.t -= self.p * ((self.a - a_next) ** 2)
            self.a = a_next
            self.p *= 2

        pi = ((self.a + self.b) ** 2) / (4 * self.t)
        return round(pi, self.n)

class E:
    """
    Calculates Euler's number (e) using Taylor series expansion.
    The series converges to e as the number of terms approaches infinity.
    """
    
    def __init__(self, n):
        """
        Initializes the e calculator with precision parameters.
        
        Args:
            n (int): Number of decimal places desired (max 100)
            
        Raises:
            ValueError: If requested precision exceeds 100 digits
        """
        if n > 100:
            raise ValueError("The number of decimal places is limited to 100.")
        self.n = n
        self.accuracy = 10 ** (-n)  # Terminate when terms are smaller than this
        self.e = 0.0  # Current approximation
        self.factorial = 1.0  # Running factorial value
        self.k = 0  # Current term index

    def taylor_series(self):
        """
        Recursively calculates e by adding terms of the Taylor series.
        
        Returns:
            float: e approximated to n decimal places
        """
        term = 1.0 / self.factorial
        self.e += term
        
        # Base case: term smaller than desired accuracy
        if term < self.accuracy:
            return round(self.e, self.n)
            
        self.k += 1
        self.factorial *= self.k  # Update factorial for next term
        return self.taylor_series()


class Fibonacci:
    """
    Generates Fibonacci sequence up to a specified maximum value.
    The sequence is generated iteratively for efficiency.
    """
    
    def __init__(self, n):
        """
        Initializes Fibonacci sequence generator.
        
        Args:
            n (int): Upper limit for sequence values
            
        Raises:
            ValueError: For negative input values
        """
        if n < 0:
            raise ValueError("The number must be a non-negative integer.")
        self.n = n
        self.fib = [0, 1]  # Initial sequence values
        self.i = 2  # Current index

    def calculate(self):
        """
        Generates Fibonacci numbers up to the specified limit.
        
        Returns:
            list: Complete Fibonacci sequence up to n
        """
        while True:
            next_val = self.fib[self.i - 1] + self.fib[self.i - 2]
            if next_val > self.n:
                break
            self.fib.append(next_val)
            self.i += 1
        return self.fib



class FibonacciCalculator:
    """
    Generates the first n numbers in the Fibonacci sequence.
    This implementation uses an iterative approach for efficiency.
    """
    
    def __init__(self, limit):
        """
        Initializes the Fibonacci sequence generator.
        
        Args:
            limit (int): Number of Fibonacci numbers to generate
            
        Raises:
            ValueError: For negative input values
        """
        if limit < 0:
            raise ValueError("The number must be a non-negative integer.")
        self.limit = limit

    def calculate_fibonacci(self):
        """
        Generates the Fibonacci sequence.
        
        Returns:
            list: First 'limit' Fibonacci numbers
        """
        if self.limit == 0:
            return []
        elif self.limit == 1:
            return [0]
            
        fib = [0, 1]
        while len(fib) < self.limit:
            fib.append(fib[-1] + fib[-2])
        return fib


class PrimeFactors:
    """
    Computes the prime factorization of a number using trial division.
    Efficient for moderately sized numbers (up to 10^12 or so).
    """
    
    def __init__(self, n):
        """
        Initializes the prime factorizer.
        
        Args:
            n (int): Number to factor (must be > 1)
            
        Raises:
            ValueError: For numbers less than 2
        """
        if n < 2:
            raise ValueError("The number must be a positive integer greater than 1.")
        self.n = n
        self.factors = []  # List to store prime factors

    def find_factors(self):
        """
        Performs prime factorization using trial division.
        
        Returns:
            list: Prime factors in increasing order
        """
        # Handle even factors
        while self.n % 2 == 0:
            self.factors.append(2)
            self.n //= 2
            
        # Check odd divisors up to sqrt(n)
        limit = int(math.sqrt(self.n)) + 1
        for i in range(3, limit, 2):
            while self.n % i == 0:
                self.factors.append(i)
                self.n //= i
                
        # If remaining n is prime
        if self.n > 2:
            self.factors.append(self.n)
            
        return self.factors


class Tiles:
    """
    Calculates the total cost to tile a rectangular floor area.
    Supports any consistent units (meters, feet, etc.).
    """
    
    def __init__(self, w, h, c):
        """
        Initializes the tile calculator.
        
        Args:
            w (float): Floor width
            h (float): Floor height
            c (float): Cost per unit area
            
        Raises:
            ValueError: For negative dimensions
        """
        if w < 0 or h < 0 or c < 0:
            raise ValueError("All dimensions must be non-negative.")
        self.w = w
        self.h = h
        self.c = c

    def cost(self):
        """
        Computes total tiling cost.
        
        Returns:
            float: Total cost (width × height × cost per unit)
        """
        return self.w * self.h * self.c


class MonthlyPayments:
    """
    Calculates fixed-rate loan payments using standard amortization formula.
    Supports different compounding intervals (monthly, weekly, daily).
    """
    
    def __init__(self, principal, annual_rate, years, interval):
        """
        Initializes payment calculator with loan terms.
        
        Args:
            principal (float): Loan amount
            annual_rate (float): Annual interest rate (decimal)
            years (int): Loan term in years
            interval (str): 'monthly', 'weekly', or 'daily'
            
        Raises:
            ValueError: For invalid parameters or intervals
        """
        if principal < 0 or annual_rate < 0 or years < 0:
            raise ValueError("All parameters must be non-negative.")
            
        # Convert to periodic terms
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
            
        self.principal = principal
        self.monthly_payment = None

    def calculate_monthly_payments(self):
        """
        Computes fixed periodic payment amount.
        
        Returns:
            float: Payment amount rounded to 2 decimal places
        """
        if self.r == 0:  # Handle interest-free loan
            self.monthly_payment = self.principal / self.n
        else:
            # Standard amortization formula
            self.monthly_payment = (self.principal * self.r * (1 + self.r)**self.n) / ((1 + self.r)**self.n - 1)
            
        return round(self.monthly_payment, 2)


class PaybackTime:
    """
    Calculates loan payback time given periodic payments.
    Uses logarithmic solution to the amortization formula.
    """
    
    def __init__(self, principal, annual_rate, monthly_payment, interval):
        """
        Initializes payback time calculator.
        
        Args:
            principal (float): Loan amount
            annual_rate (float): Annual interest rate (decimal)
            monthly_payment (float): Fixed periodic payment
            interval (str): 'monthly', 'weekly', or 'daily'
            
        Raises:
            ValueError: For invalid parameters
        """
        if principal < 0 or annual_rate < 0 or monthly_payment < 0:
            raise ValueError("All parameters must be non-negative.")
            
        # Convert to periodic rate
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
        Computes time required to pay off loan.
        
        Returns:
            float: Time in years to pay off loan
        """
        if self.r == 0:  # Interest-free case
            self.payback_time = self.principal / self.monthly_payment / 12
        else:
            # Logarithmic solution to amortization formula
            numerator = math.log(self.monthly_payment / (self.monthly_payment - self.r * self.principal))
            denominator = math.log(1 + self.r)
            self.payback_time = numerator / denominator / 12  # Convert to years
            
        return self.payback_time


class ChangeCalculator:
    """
    Calculates optimal change breakdown for a given amount.
    Uses standard US currency denominations with greedy algorithm.
    """
    
    def __init__(self, n):
        """
        Initializes change calculator.
        
        Args:
            n (float): Amount to make change for
            
        Raises:
            ValueError: For negative amounts
        """
        if n < 0:
            raise ValueError("The amount must be a non-negative integer.")
        self.n = round(n, 2)  # Handle floating point amounts
        self.change = {
            "hundred-dollar bills": 0, "fifty-dollar bills": 0, "twenty-dollar bills": 0, 
            "ten-dollar bills": 0, "five-dollar bills": 0, "two-dollar bills": 0, 
            "one-dollar bills": 0, "quarters": 0, "dimes": 0, "nickels": 0, "pennies": 0
        }
        self.values = {
            100: "hundred-dollar bills", 50: "fifty-dollar bills", 20: "twenty-dollar bills",
            10: "ten-dollar bills", 5: "five-dollar bills", 2: "two-dollar bills", 
            1: "one-dollar bills", 0.25: "quarters", 0.10: "dimes", 0.05: "nickels", 0.01: "pennies"
        }

    def calculate(self):
        """
        Computes optimal change breakdown.
        
        Returns:
            list: List of [denomination, count] pairs
        """
        remaining = self.n
        # Process each denomination from largest to smallest
        for value in sorted(self.values.keys(), reverse=True):
            name = self.values[value]
            if remaining >= value:
                count = int(remaining // value)
                self.change[name] = count
                remaining = round(remaining - count * value, 2)
        return [[k, v] for k, v in self.change.items() if v != 0]

    def display_change(self):
        """Prints the change breakdown in human-readable format."""
        self.calculate()
        for denomination, count in self.change.items():
            if count > 0:
                print(f"{denomination}: {count}")

class UnitConverter:
    """
    Handles unit conversions for various measurement types.
    Supports length, temperature, area, and volume conversions.
    """

    def __init__(self, conversion_type, value, from_unit, to_unit):
        """
        Initializes the unit converter with input parameters.
        
        Args:
            conversion_type (int): Type of conversion (1=length, 2=temperature, 3=area, 4=volume)
            value (float): Value to convert
            from_unit (str): Source unit
            to_unit (str): Target unit

        Raises:
            ValueError: If a negative value is given for non-temperature conversions
        """
        self.value = value
        self.from_unit = from_unit
        self.to_unit = to_unit
        self.conversion_type = conversion_type

        if self.conversion_type == 1:
            if value < 0:
                raise ValueError("The value must be a non-negative number.")
            # Length units in meters
            self.units = {
                "m": 1, "km": 1000, "cm": 0.01, "mm": 0.001,
                "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344
            }

        elif self.conversion_type == 3:
            if value < 0:
                raise ValueError("The value must be a non-negative number.")
            # Area units in square meters
            self.units = {
                "m^2": 1, "km^2": 1000000, "cm^2": 0.0001, "mm^2": 0.000001,
                "in^2": 0.00064516, "ft^2": 0.092903, "yd^2": 0.836127, "mi^2": 2589988.11
            }

        elif self.conversion_type == 4:
            if value < 0:
                raise ValueError("The value must be a non-negative number.")
            # Volume units in cubic meters
            self.units = {
                "m^3": 1, "km^3": 1e+9, "cm^3": 1e-6, "mm^3": 1e-9,
                "in^3": 0.0000163871, "ft^3": 0.0283168,
                "gal": 0.00378541, "l": 0.001, "ml": 0.000001,
                "imperial pint": 0.000568261, "us fluid ounce": 0.0000295735
            }

    def convert(self):
        """
        Converts the value based on the selected conversion type.
        
        Returns:
            float: Converted value rounded to 2 decimal places
        
        Raises:
            ValueError: For invalid units or unsupported conversions
        """
        if self.conversion_type in (1, 3, 4):
            if self.from_unit in self.units and self.to_unit in self.units:
                return round(self.value * self.units[self.from_unit] / self.units[self.to_unit], 2)
            else:
                raise ValueError("Invalid unit provided for conversion.")
        elif self.conversion_type == 2:
            return self.convert_temperature()

    def convert_temperature(self):
        """
        Handles temperature conversion between Celsius, Fahrenheit, Kelvin, and Rankine.
        
        Returns:
            float: Converted temperature value
        
        Raises:
            ValueError: For invalid temperature unit
        """
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
class UnitConverter:
    """
    Handles unit conversions for various measurement types.
    Supports length, temperature, area, and volume conversions.
    """

    def __init__(self, conversion_type, value, from_unit, to_unit):
        """
        Initializes the unit converter with input parameters.
        
        Args:
            conversion_type (int): Type of conversion (1=length, 2=temperature, 3=area, 4=volume)
            value (float): Value to convert
            from_unit (str): Source unit
            to_unit (str): Target unit

        Raises:
            ValueError: If a negative value is given for non-temperature conversions
        """
        self.value = value
        self.from_unit = from_unit
        self.to_unit = to_unit
        self.conversion_type = conversion_type

        if self.conversion_type == 1:
            if value < 0:
                raise ValueError("The value must be a non-negative number.")
            # Length units in meters
            self.units = {
                "m": 1, "km": 1000, "cm": 0.01, "mm": 0.001,
                "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344
            }

        elif self.conversion_type == 3:
            if value < 0:
                raise ValueError("The value must be a non-negative number.")
            # Area units in square meters
            self.units = {
                "m^2": 1, "km^2": 1000000, "cm^2": 0.0001, "mm^2": 0.000001,
                "in^2": 0.00064516, "ft^2": 0.092903, "yd^2": 0.836127, "mi^2": 2589988.11
            }

        elif self.conversion_type == 4:
            if value < 0:
                raise ValueError("The value must be a non-negative number.")
            # Volume units in cubic meters
            self.units = {
                "m^3": 1, "km^3": 1e+9, "cm^3": 1e-6, "mm^3": 1e-9,
                "in^3": 0.0000163871, "ft^3": 0.0283168,
                "gal": 0.00378541, "l": 0.001, "ml": 0.000001,
                "imperial pint": 0.000568261, "us fluid ounce": 0.0000295735
            }

    def convert(self):
        """
        Converts the value based on the selected conversion type.
        
        Returns:
            float: Converted value rounded to 2 decimal places
        
        Raises:
            ValueError: For invalid units or unsupported conversions
        """
        if self.conversion_type in (1, 3, 4):
            if self.from_unit in self.units and self.to_unit in self.units:
                return round(self.value * self.units[self.from_unit] / self.units[self.to_unit], 2)
            else:
                raise ValueError("Invalid unit provided for conversion.")
        elif self.conversion_type == 2:
            return self.convert_temperature()

    def convert_temperature(self):
        """
        Handles temperature conversion between Celsius, Fahrenheit, Kelvin, and Rankine.
        
        Returns:
            float: Converted temperature value
        
        Raises:
            ValueError: For invalid temperature unit
        """
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
