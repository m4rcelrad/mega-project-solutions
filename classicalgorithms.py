def collatz_conjecture(n):
    if n <= 1:
        raise ValueError('n must be grater than 1')
    steps = 0
    while n != 1:
        if n % 2:
            n = n*3 + 1
        else:
            n /= 2
        steps += 1
    return steps

def merge(left, right):
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

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        swapped_flag = False
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped_flag = True
        if not swapped_flag:
            break
    return lst

def distance_square(p1,p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def closest_recursive(points_sorted_x, points_sorted_y):
    if len(points_sorted_x) <= 3:
        min_distance_squared = float('inf')
        closest = None
        for i in range(len(points_sorted_x)):
            for j in range(i + 1, len(points_sorted_x)):
                distance = distance_square(points_sorted_x[i], points_sorted_x[j])
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

    left_pair, left_distance = closest_recursive(left_x, left_y)
    right_pair, right_distance = closest_recursive(right_x, right_y)

    if left_distance < right_distance:
        min_pair = left_pair
        min_distance_squared = left_distance
    else:
        min_pair = right_pair
        min_distance_squared = right_distance

    strip = [p for p in points_sorted_y if abs(p[0] - midpoint) < min_distance_squared ** 0.5]
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            distance = distance_square(strip[i], strip[j])
            if distance < min_distance_squared:
                min_pair = (strip[i], strip[j])
                min_distance_squared = distance

    return min_pair, min_distance_squared

def closest_pair(points):
    points_sorted_x = sorted(points, key=lambda x: x[0])
    points_sorted_y = sorted(points, key=lambda x: x[1])
    return closest_recursive(points_sorted_x, points_sorted_y)

def sieve_of_eratosthenes(n):
    if n <= 1:
        raise ValueError('n must be grater than 1')
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, n + 1):
        if sieve[i]:
            sieve[i*i::i] = b'\x00' * len(sieve[i*i::i])
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes
