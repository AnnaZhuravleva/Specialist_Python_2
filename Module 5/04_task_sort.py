def quick_sort(nums):

    def partition(nums, low, high):
        pivot = nums[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while abs(nums[i]) < abs(pivot):
                i += 1

            j -= 1
            while abs(nums[j]) > abs(pivot):
                j -= 1

            if i >= j:
                return j
            nums[i], nums[j] = nums[j], nums[i]

    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]
quick_sort(numbers)
print(numbers)
print(sum(numbers[-2:]))
