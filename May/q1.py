#### Question : Average Salary Excluding the Minimum and Maximum Salary

## Level : Easy
## https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

import sys
from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:

        minimum = sys.maxsize
        maximum = -sys.maxsize

        total_sum = 0

        for sal in salary:
            if sal < minimum:
                minimum = sal
            
            if sal > maximum:
                maximum = sal

            total_sum += sal

        return (total_sum - minimum - maximum) / (len(salary) - 2)


## Test
s = Solution()
print(s.average([4000,3000,1000,2000]))
print(s.average([1000,2000,3000]))

        