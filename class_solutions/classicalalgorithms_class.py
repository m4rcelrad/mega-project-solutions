import random
import math


class CollatzConjecture:
    """
    Start with a number n > 1.
    Find the number of steps it takes to reach one using the following process:
        If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
    """

    def __init__(self, n):
        self.n = n
        self.steps = 0

    def calculate_steps(self):
        if self.n <= 1:
            raise ValueError('n must be grater than 1')
        while self.n != 1:
            if self.n % 2:
                self.n = self.n * 3 + 1
            else:
                self.n /= 2
            self.steps += 1
        return self.steps


class MergeSorter:
    """
        MergeSorter is a utility class that implements the Merge Sort algorithm.
        Attributes:
            data (list): The list of elements to be sorted.
        Methods:
            sort():
                Returns a sorted copy of the original list using merge sort.
        """

    def __init__(self, lst):
        self.lst = lst

    def sort(self):
        return self.merge_sort(self.lst)

    def merge_sort(self, lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = self.merge_sort(lst[:mid])
        right = self.merge_sort(lst[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
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
    def __init__(self, lst):
        self.lst = lst
        self.n = len(lst)

    def sort(self):
        for i in range(self.n):
            swapped_flag = False
            for j in range(self.n - i - 1):
                if self.lst[j] > self.lst[j + 1]:
                    self.lst[j], self.lst[j + 1] = self.lst[j + 1], self.lst[j]
                    swapped_flag = True
            if not swapped_flag:
                break
        return self.lst


class ClosestPair:

    def __init__(self, n):
        if n < 2:
            raise ValueError('n must be greater than 1')
        self.points = self.generate_random_points(n)

    @staticmethod
    def distance_square(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    @staticmethod
    def generate_random_points(n, x_range=(0, 100), y_range=(0, 100)):
        if n < 1:
            raise ValueError('N must be grater than 1')
        return [(random.uniform(*x_range), random.uniform(*y_range)) for _ in range(n)]

    def closest_recursive(self, points_sorted_x, points_sorted_y):
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

        mid = len(points_sorted_x) // 2
        left_x = points_sorted_x[:mid]
        right_x = points_sorted_x[mid:]
        midpoint = points_sorted_x[mid][0]

        left_y = [p for p in points_sorted_y if p[0] <= midpoint]
        right_y = [p for p in points_sorted_y if p[0] > midpoint]

        left_pair, left_distance = self.closest_recursive(left_x, left_y)
        right_pair, right_distance = self.closest_recursive(right_x, right_y)

        if left_distance < right_distance:
            min_pair = left_pair
            min_distance_squared = left_distance
        else:
            min_pair = right_pair
            min_distance_squared = right_distance

        strip = [p for p in points_sorted_y if abs(p[0] - midpoint) < min_distance_squared ** 0.5]
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                distance = self.distance_square(strip[i], strip[j])
                if distance < min_distance_squared:
                    min_pair = (strip[i], strip[j])
                    min_distance_squared = distance

        return min_pair, min_distance_squared

    def find_closest_pair(self):
        points_sorted_x = sorted(self.points, key=lambda x: x[0])
        points_sorted_y = sorted(self.points, key=lambda x: x[1])
        return self.closest_recursive(points_sorted_x, points_sorted_y)


class SieveOfEratosthenes:
    def __init__(self, n):
        if n < 1:
            raise ValueError('N must be greater than 1')
        self.n = n
        self.primes = self.sieve_of_eratosthenes()

    def sieve_of_eratosthenes(self):
        sieve = bytearray([1]) * (n + 1)
        sieve[0] = sieve[1] = 0

        for i in range(2, self.n + 1):
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
        print(e)

