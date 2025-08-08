from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0 and len(nums2) > 0:
            if len(nums2) % 2 == 0:
                return float( ( nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1] ) / 2)
            else:
                return float(nums2[len(nums2) // 2])
        elif len(nums2) == 0 and len(nums1) > 0:
            if len(nums1) % 2 == 0:
                return float( ( nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1] ) / 2)
            else:
                return float(nums1[len(nums1) // 2])
        elif len(nums1) == 0 and len(nums2) == 0:
            return 0.0

        i = 0
        j = 0

        while ( (len(nums1) + len(nums2) + 1) // 2 - 1 ) != (i + j):
            if i == len(nums1) - 1:
                j += 1
            elif j == len(nums2) - 1:
                i += 1
            else:
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1

        print("final i: ", i, " final j: ", j)
        print("number1: ", nums1[i], " number2: ", nums2[j])
        if ( ( len(nums1) + len(nums2) ) % 2 == 0 ):
            print("out: ", nums1[i], nums2[j])
            return float( ( nums1[i] + nums2[j] ) / 2)
        else:
            if ( nums1[i] > nums2[j]):
                return float(nums2[j])
            return float(nums1[i])


if __name__ == "__main__":
    nums1 = [1,2,3,4,5]
    nums2 = [6,7,8,9,10,11,12,13,14,15,16,17]
    solution = Solution()
    print("array 1: ", nums1)
    print("array 2: ", nums2)
    print("length of array 1: ", len(nums1))
    print("length of array 2: ", len(nums2))
    print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 2.0

    print("--" * 20)

    # nums1 = [1, 2]
    # nums2 = [3, 4]
    # print("array 1: ", nums1)
    # print("array 2: ", nums2)
    # print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 2.5

    # nums1 = []
    # nums2 = [0]
    # print("array 1: ", nums1)
    # print("array 2: ", nums2)
    # print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 0.0


    # nums1 = [0]
    # nums2 = []
    # print("array 1: ", nums1)
    # print("array 2: ", nums2)
    # print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 0.0

    # nums1 = []
    # nums2 = []
    # print("array 1: ", nums1)
    # print("array 2: ", nums2)
    # print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 0.0

    # nums1 = [0, 0, 2, 3]
    # nums2 = []
    # print("array 1: ", nums1)
    # print("array 2: ", nums2)
    # print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 0.0

    # nums1 = [0, 0, 2, 3, 10]
    # nums2 = []
    # print("array 1: ", nums1)
    # print("array 2: ", nums2)
    # print(solution.findMedianSortedArrays(nums1, nums2))  # Output: 0.0
