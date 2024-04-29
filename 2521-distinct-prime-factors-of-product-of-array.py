"""
https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/description/

Given an array of positive integers nums, return the number of distinct prime factors in the product of the elements of nums.

Note that:

A number greater than 1 is called prime if it is divisible by only 1 and itself.
An integer val1 is a factor of another integer val2 if val2 / val1 is an integer.
 

Example 1:

Input: nums = [2,4,3,7,10,6]
Output: 4
Explanation:
The product of all the elements in nums is: 2 * 4 * 3 * 7 * 10 * 6 = 10080 = 25 * 32 * 5 * 7.
There are 4 distinct prime factors so we return 4.
Example 2:

Input: nums = [2,4,8,16]
Output: 1
Explanation:
The product of all the elements in nums is: 2 * 4 * 8 * 16 = 1024 = 210.
There is 1 distinct prime factor so we return 1.
 

Constraints:

1 <= nums.length <= 104
2 <= nums[i] <= 1000

"""


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:

        # Method 1: brute force: get the product and divide by the prime iteratively
        # product = 1
        # for num in nums:
        #     product *= num

        # divider = 2
        # res = set()

        # while product > 1:
        #     if product % divider == 0:
        #         res.add(divider)
        #         product //= divider
        #     else:
        #         divider += 1
        
        # return len(res)

        # Method 2: prime factorization of the product of an array is the same as calculating prime factorization of each element in the array.
        res = set()
        for num in nums:
            for divider in range(2, int(math.sqrt(num)) + 1):  # prime factorization only goes up to square root of the number
                if num % divider == 0:
                    res.add(divider)
                    while num % divider == 0:
                        num //= divider
        
            if num > 1:  # when it's a prime number, i.e. 17, 19
                res.add(num)

        return len(res)

