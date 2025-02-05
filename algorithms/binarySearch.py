def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
        
        
if __name__ == "__main__":
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    target = 10
    print(f"Index of {target} is {binarySearch(primes, target)}")
    