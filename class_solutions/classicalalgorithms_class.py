import random
import math


class CollatzConjecture:
    """
    Implements the Collatz Conjecture algorithm which calculates the number of steps
    required to reduce a number to 1 following specific rules.
    
    Rules:
    - If n is even: divide by 2
    - If n is odd: multiply by 3 and add 1
    """

    def __init__(self, n):
        """
        Initialize the Collatz conjecture calculator.
        
        Args:
            n (int): The starting number (must be > 1)
        """
        self.n = n
        self.steps = 0

    def calculate_steps(self):
        """
        Calculate the number of steps needed to reach 1 from the initial number.
        
        Returns:
            int: Number of steps taken to reach 1
            
        Raises:
            ValueError: If initial number is <= 1
        """
        if self.n <= 1:
            raise ValueError('n must be greater than 1')
        while self.n != 1:
            if self.n % 2:
                self.n = self.n * 3 + 1
            else:
                self.n //= 2  # Changed to integer division
            self.steps += 1
        return self.steps


class MergeSorter:
    """
    Implements the Merge Sort algorithm, a divide-and-conquer sorting algorithm
    with O(n log n) time complexity.
    """

    def __init__(self, lst):
        """
        Initialize the merge sorter with a list to be sorted.
        
        Args:
            lst (list): The list of elements to sort
        """
        self.lst = lst

    def sort(self):
        """Return a new sorted list using merge sort algorithm."""
        return self.merge_sort(self.lst)

    def merge_sort(self, lst):
        """
        Recursively divide the list and merge sorted halves.
        
        Args:
            lst (list): List to be sorted
            
        Returns:
            list: Sorted list
        """
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = self.merge_sort(lst[:mid])
        right = self.merge_sort(lst[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        """
        Merge two sorted lists into one sorted list.
        
        Args:
            left (list): First sorted list
            right (list): Second sorted list
            
        Returns:
            list: Merged sorted list
        """
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged


class BubbleSorter:
    """
    Implements the Bubble Sort algorithm, a simple sorting algorithm
    with O(n²) time complexity in worst case.
    """

    def __init__(self, lst):
        """
        Initialize the bubble sorter with a list to be sorted.
        
        Args:
            lst (list): The list of elements to sort
        """
        self.lst = lst
        self.n = len(lst)

    def sort(self):
        """
        Sort the list in-place using bubble sort with early termination.
        
        Returns:
            list: The sorted list
        """
        for i in range(self.n):
            swapped_flag = False
            for j in range(self.n - i - 1):
                if self.lst[j] > self.lst[j + 1]:
                    self.lst[j], self.lst[j + 1] = self.lst[j + 1], self.lst[j]
                    swapped_flag = True
            if not swapped_flag:  # Early termination if no swaps occurred
                break
        return self.lst


class ClosestPair:
    """
    Implements a divide-and-conquer algorithm to find the closest pair of points
    in O(n log n) time complexity.
    """

    def __init__(self, n):
        """
        Initialize with randomly generated points.
        
        Args:
            n (int): Number of points to generate (must be >= 2)
            
        Raises:
            ValueError: If n < 2
        """
        if n < 2:
            raise ValueError('n must be greater than 1')
        self.points = self.generate_random_points(n)

    @staticmethod
    def distance_square(p1, p2):
        """
        Calculate squared Euclidean distance between two points.
        
        Args:
            p1, p2 (tuple): Points as (x, y) coordinates
            
        Returns:
            float: Squared distance between points
        """
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    @staticmethod
    def generate_random_points(n, x_range=(0, 100), y_range=(0, 100)):
        """
        Generate n random points within specified ranges.
        
        Args:
            n (int): Number of points to generate
            x_range (tuple): Range for x coordinates
            y_range (tuple): Range for y coordinates
            
        Returns:
            list: List of (x, y) tuples
            
        Raises:
            ValueError: If n < 1
        """
        if n < 1:
            raise ValueError('N must be greater than 1')
        return [(random.uniform(*x_range), random.uniform(*y_range)) for _ in range(n)]

    def closest_recursive(self, points_sorted_x, points_sorted_y):
        """
        Recursive function to find closest pair.
        
        Args:
            points_sorted_x (list): Points sorted by x-coordinate
            points_sorted_y (list): Points sorted by y-coordinate
            
        Returns:
            tuple: (closest_pair, squared_distance)
        """
        # Base case: use brute force for small sets
        if len(points_sorted_x) <= 3:
            min_distance_squared = float('inf')
            closest = None
            for i in range(len(points_sorted_x)):
                for j in range(i + 1, len(points_sorted_x)):
                    distance = self.distance_square(points_sorted_x[i], points_sorted_x[j])
                    if distance < min_distance_squared:
                        min_distance_squared = distance
                        closest = (points_sorted_x[i], points_sorted_x[j])
            return closest, min_distance_squared

        # Divide step
        mid = len(points_sorted_x) // 2
        left_x = points_sorted_x[:mid]
        right_x = points_sorted_x[mid:]
        midpoint = points_sorted_x[mid][0]

        left_y = [p for p in points_sorted_y if p[0] <= midpoint]
        right_y = [p for p in points_sorted_y if p[0] > midpoint]

        # Conquer step
        left_pair, left_distance = self.closest_recursive(left_x, left_y)
        right_pair, right_distance = self.closest_recursive(right_x, right_y)

        # Combine results
        if left_distance < right_distance:
            min_pair = left_pair
            min_distance_squared = left_distance
        else:
            min_pair = right_pair
            min_distance_squared = right_distance

        # Check for closer pairs that cross the division
        strip = [p for p in points_sorted_y if abs(p[0] - midpoint) < min_distance_squared ** 0.5]
        for i in range(len(strip)):
            # Only need to check next 7 points due to geometric properties
            for j in range(i + 1, min(i + 7, len(strip))):
                distance = self.distance_square(strip[i], strip[j])
                if distance < min_distance_squared:
                    min_pair = (strip[i], strip[j])
                    min_distance_squared = distance

        return min_pair, min_distance_squared

    def find_closest_pair(self):
        """
        Find the closest pair of points in the set.
        
        Returns:
            tuple: (closest_pair, squared_distance)
        """
        points_sorted_x = sorted(self.points, key=lambda x: x[0])
        points_sorted_y = sorted(self.points, key=lambda x: x[1])
        return self.closest_recursive(points_sorted_x, points_sorted_y)


class SieveOfEratosthenes:
    """
    Implements the Sieve of Eratosthenes algorithm for finding all prime numbers
    up to a given limit.
    """

    def __init__(self, n):
        """
        Initialize the sieve with upper limit n.
        
        Args:
            n (int): Upper limit for prime search (must be >= 2)
            
        Raises:
            ValueError: If n < 2
        """
        if n < 2:
            raise ValueError('N must be at least 2')
        self.n = n
        self.primes = self.sieve_of_eratosthenes()

    def sieve_of_eratosthenes(self):
        """
        Generate primes using the Sieve of Eratosthenes algorithm.
        
        Returns:
            list: List of prime numbers <= n
        """
        sieve = bytearray([1]) * (self.n + 1)
        sieve[0] = sieve[1] = 0

        for i in range(2, int(math.sqrt(self.n)) + 1):
            if sieve[i]:
                sieve[i*i::i] = b'\x00' * len(sieve[i*i::i])

        return [i for i, is_prime in enumerate(sieve) if is_prime]


if __name__ == "__main__":
    try:
        # Collatz Conjecture
        n = int(input("Enter an integer to find the collatz conjecture of: "))
        print(f"The number of steps it takes to reach one: {CollatzConjecture(n).calculate_steps()}")

        # Merge sorting
        lst = list(map(int, input("Enter a list of numbers to sort: ").split()))
        print(f"Sorted list - merge sorting: {MergeSorter(lst).sort()}")
        print(f"Sorted list - bubble sorting: {BubbleSorter(lst).sort()}")

        # Closest pair
        n = int(input("Enter a number of random points (>1): "))
        pair, distance = ClosestPair(n).find_closest_pair()
        print(f"Closest pair: {pair}\nClosest distance: {math.sqrt(distance)}")

        # Sieve of Eratosthenes
        n = int(input("Enter the limit: "))
        print(f"Primes up to {n}: {SieveOfEratosthenes(n).primes}")
    except ValueError as e:
        print(f"Error: {e}")
