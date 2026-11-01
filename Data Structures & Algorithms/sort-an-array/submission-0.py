class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr, left, right):
            if left < right:
                mid = (left + right) // 2
                merge_sort(arr, left, mid)
                merge_sort(arr, mid + 1, right)
                merge(arr, left, mid, right)

        def merge(arr, left, mid, right):
            L = arr[left:mid + 1]
            R = arr[mid + 1:right + 1]
            i = j = 0
            k = left

            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

        merge_sort(nums, 0, len(nums) - 1)
        return nums   